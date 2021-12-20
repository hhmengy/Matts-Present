# Yeelight-Code
Useful links
List of stocks
https://docs.google.com/spreadsheets/d/1QV63hHqSDQafKVfRkSZBbN12q8SXKQQOgwtPGaVfs5U/edit?usp=sharing
List of ETFs
https://docs.google.com/spreadsheets/d/1XO4pIg8YBDohYh1dGS6i-L4l9qaMz4FBnJGfcTb_zew/edit?usp=sharing
Code



Setting up yo Light

follow the instructions on the little pamphlet to install your yeelight.
It has you download an app called “Mi Home App”. I ended up downloading an app called “Yeelight”. The app has instructions on how to set up the light.
Once the light is connected, find the IP address for it on your yeelight app
Click the bulb on your app
Click the 3 lines with circles on them in top right corner
Click device info
Ip address should be listed there
Assign your bulb’s IP to the BULB_IP variable in the code on line 10
Turn the light on and Run the code
If you use an IDE like geany you can run it through that.
If not, go to your command prompt and change directories to where you saved the  code. Then type the command python3 stock_bulb.py\

Editing the Code

The three variables in lines 11-13
STOCK_TICKER is used to determine which ticker you want the light to reflect(set IS_ETF to false)
ETF_TICKER is used to determine which ETF you want the light to reflect(set IS_ETF to true)
IS_ETF set to true if you want the light to reflect the ETF_TICKER you defined. Set to false if you want the light to reflect the STOCK_TICKER
If you want to understand the code better, I followed the free Udemy course located here. https://www.udemy.com/course/stock-market-color-lamp-in-python/
I was going to put the code on the Raspberry pi to run constantly without having to worry about having to start up the code every time you turn on a computer, but the micro SD card got corrupted when I was setting it up :(
I don’t think it would be too hard to figure out how to do that, I can help with that if needed.
If you want to set up the code to follow multiple stocks or track something else instead of profit and loss, just let me know and I can make those changes.  
