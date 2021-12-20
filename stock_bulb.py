import logging
import sys
import time
from datetime import date, timedelta
from datetime import datetime
import investpy
import numpy as np
from yeelight import Bulb, BulbException

BULB_IP = '192.168.0.9'
STOCK_TICKER = 'AAPL'         #Stock uses tickers
ETF_TICKER = 'SPDR S&P 500'   #ETF uses names
IS_ETF = True

def daily_pnl():
    if IS_ETF:
	    stock_data = investpy.etfs.get_etf_historical_data(ETF_TICKER, 'united states', from_date=(date.today() +
            timedelta(days=-1)).strftime("%d/%m/%Y"), to_date=date.today().strftime("%d/%m/%Y"))
    else:
	    stock_data = investpy.get_stock_historical_data(STOCK_TICKER, 'united states', from_date=(date.today() +
            timedelta(days=-1)).strftime("%d/%m/%Y"), to_date=date.today().strftime("%d/%m/%Y"))           
    stock_data.index = stock_data.index + timedelta(days=1)
    ytd = stock_data.iloc[0].Close
    tdy = stock_data.iloc[1].Close
    return ((tdy-ytd)/ytd)*100

def refresh_bulb_color(bulb):

    pnl_to_color = {-1.0: '#ff1100',  # <1%+ loss
                    -0.5: '#ff6a00',
                    0.0: '#ffffff',  # neutral
                    0.5: '#00ff73',
                    1.0: '#00ff00',}  # >+0.5% gain

    pnl = daily_pnl()
    print("{:.2f}%".format(pnl))
    pnl_idx = np.searchsorted(list(pnl_to_color.keys()), pnl, 'left').clip(0,4)
    color = list(pnl_to_color.values())[pnl_idx]
    rgb = tuple(int(color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))

    try:
        bulb.set_rgb(rgb[0], rgb[1], rgb[2])
    except BulbException:
        logging.error('bulb disconnected')
        return False

    return True

def isInvestLiveToday(is_new_day):
    if is_new_day:
        # Latest date available on Invest.com
        stock_data = investpy.get_stock_historical_data('AAPL', 'united states', from_date=(date.today() +
                                                                                           timedelta(days=-1)).strftime(
            "%d/%m/%Y"), to_date=date.today().strftime("%d/%m/%Y"))
        stock_data.index = stock_data.index + timedelta(days=1)
        latest = stock_data.iloc[1].Close
        is_new_day = False

        return (stock_data.index[0].date() == date.today())
    else:
        return True

def check_bulb_state(bulb, condition):
    try:
        return (bulb.get_properties(requested_properties=['power', ])['power'] == condition)
    except BulbException:
        logging.error('bulb disconnected')
        return None

def getBulb(bulb):
    if (check_bulb_state(bulb, True) != None):
        return bulb
    else:
        # try to reconnect
        logging.error('trying to reconnect')
        try:
            bulb = Bulb(BULB_IP)
            bulb.get_properties(requested_properties=['power', ])
            return bulb
        except Exception:
            logging.error('could not reconnect')
            return None

def isMktOpen(now, mkt_close_time, mkt_open_time):
    # is weekend?
    if now.date().isoweekday() > 5:
        return False
    else:
        return (now.time()<mkt_close_time.time() and now.time()>mkt_open_time.time())

def sleepUntilOpens(now, mkt_open_time):
    # Between 16:00 and 00:00
    if (now.time().hour > 16):
        mysleep = (mkt_open_time + timedelta(days=1) - now).total_seconds() - 60
    # Between 00:00 and 09:00
    elif (now.time().hour < 9):
        mysleep = (mkt_open_time - now).total_seconds() - 60
    # Between 09:00 and 09:30
    else:
        mysleep = 30
    logging.info('sleepig until ' + str(now + timedelta(seconds=mysleep)))
    time.sleep(mysleep)

def run():
    logging.basicConfig(
        format = '%(asctime)s %(levelname)-8s %(message)s',
        level = logging.INFO,
        datefmt = '%Y-%m-%d %H:%M:%S')

    bulb = getBulb(Bulb(BULB_IP))

    if bulb is None:
        return

    now = datetime.now()
    mkt_open_time = now.replace(hour=9, minute=30, second=0, microsecond=0)
    mkt_close_time = now.replace(hour=16, minute=30, second=0, microsecond=0)
    new_day = True

    while True:
        now = datetime.now()

        # Market is closed
        if (not isMktOpen(now,mkt_close_time,mkt_open_time)):
            new_day = True

            logging.info('market closed')
            bulb = getBulb(bulb)
            if (bulb is not None):
                if (check_bulb_state(bulb,'on')):
                    logging.info('turn bulb off')
                    bulb.turn_off() #change color here instead of turning off

            # Gotta sleep until market opens
            sleepUntilOpens(now, mkt_open_time)
        # Market is open
        else:
            if isInvestLiveToday(new_day):
                new_day = False

                # print('today is live')
                if (check_bulb_state(bulb, 'off')):
                    logging.info('turn on')
                    bulb.turn_on()
                    time.sleep(5)
                logging.info('atualiza')
                bulb = getBulb(bulb)
                if (bulb is not None):
                    refresh_bulb_color(bulb)
            else:
                logging.info('invest.com is not live or up to date')
        time.sleep(15)


while True:
    try:
        run()
    except KeyboardInterrupt:
        break
    except:
        logging.error("Unexpected error:", sys.exc_info()[0])

    # some error ocurred, wait for 10 mins
    time.sleep(60*10)
