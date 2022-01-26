from typing import Text
import requests
import lxml
import bs4 
import re 
import time 
import sys
import random

def realtimePrice():  #binance api for taking live price
    url = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
    result = requests.get(url)
    soup = bs4.BeautifulSoup(result.text,'lxml')
    price = soup.text[29:37]
    return price

def timeloop():
    looptime = 300
    start_time = time.time()
    while (looptime != 0):
        #Computation for 60 second
        time.sleep(60)
        
        startshowing = True
        start_time = time.time()
        while startshowing == True:
            print('Price after 60 seconds: ' + realtimePrice()) 
            startshowing = False
        
        looptime -= 1
    
timeloop()

