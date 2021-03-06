# Yeelight-Code
## Useful links
1. List of stocks https://docs.google.com/spreadsheets/d/1QV63hHqSDQafKVfRkSZBbN12q8SXKQQOgwtPGaVfs5U/edit?usp=sharing

2. List of ETFs https://docs.google.com/spreadsheets/d/1XO4pIg8YBDohYh1dGS6i-L4l9qaMz4FBnJGfcTb_zew/edit?usp=sharing

3. The Free Udemy Course explaining this https://www.udemy.com/course/stock-market-color-lamp-in-python/



## Setting up yo Light

1. follow the instructions on the little pamphlet to install your yeelight.
        
        -It has you download an app called “Mi Home App”. I ended up downloading an app called “Yeelight”. The app has instructions on how to set up the light.
        
2. Once the light is connected, find the IP address for it on your yeelight app
        
        -Click the bulb on your app
        
        -Click the 3 lines with circles on them in top right corner
        
        -Click device info
        
        -Ip address should be listed there

2.Assign your bulb’s IP to the BULB_IP variable in the code on line 10

3.Turn the light on and Run the code(make sure you download the one python file in this repository)
        
        -Make sure you have python3 installed
        
        -Once python3 is installed, you may need to install the dependencies from lines 1-8. To do so, just run the command: pip install library_name
        
        -If you use an IDE like geany you can run it through that.
        
        -If not, go to your command prompt and change directories to where you saved the  code. Then type the command: python3 stock_bulb.py

4. Your command prompt should be displaying messages about if the bulb is connected, if the market is open, if the code has been put to sleep and so on. If the market is open, your bulb should currently turn some shade of green or red depending on the profit/loss of S & P 500.

## Editing the Code

1. The three variables in lines 11-13
    
    -STOCK_TICKER is used to determine which ticker you want the light to reflect(set IS_ETF to false)
    
                - use the list of stocks file to see all valid stocks, you can copy/paste the ticker name 
    
    -ETF_TICKER is used to determine which ETF you want the light to reflect(set IS_ETF to true)
    
                - use the list of ETFs file to see all valid ETFs, you can copy/paste the ETF name 
    
    -IS_ETF set to true if you want the light to reflect the ETF_TICKER you defined. Set to false if you want the light to reflect the STOCK_TICKER

2. If you want to understand the code better, I followed the free Udemy course located here. https://www.udemy.com/course/stock-market-color-lamp-in-python/


4. If you want to set up the code to follow multiple stocks or track something else instead of profit and loss, just let me know and I can make those changes.

5. Lines 25-29 are where the colors are set. If you want different colors just change the hex values(#ff1100) to the corresponding colors you want.
