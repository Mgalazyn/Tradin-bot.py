# from typing import Text
# import requests, lxml, bs4 
# import re, time, sys
# import random


# def realtimePriceBTC():  #binance api for taking live price of BTC
#     urlBTC = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
#     result = requests.get(urlBTC)
#     soup = bs4.BeautifulSoup(result.text,'lxml')
#     priceBTC = soup.text[29:37]
#     return f'Acctual price of BTC is: {priceBTC}'

# def realtimePriceETH(): #binance api for taking live price of ETH
#     urlETH = 
#     resultETH = requests.get(urlETH)
#     soupETH = bs4.BeautifulSoup(resultETH.text, 'lxml')
#     priceETH = 
#     return f' Actuall price of ETH is : {priceETH}'

# def realtimePriceBNB(): #binance api for taking live price of BNB
#     urlBNB = 
#     resultBNB = requests.get(urlBNB)
#     soupBNB = bs4.BeautifulSoup(resultBNB.text, 'lxml')
#     priceBNB = 
#     return f'Actuall price of BNB is {priceBNB}'

# def timeloop(): # func for checking price every 60 sec
#     looptime = 300
#     start_time = time.time()
#     while (looptime != 0):
#         #Computation for 60 second
#         time.sleep(60)
        
#         startshowing = True
#         start_time = time.time()
#         while startshowing == True:
#             print('Price after 60 seconds: ' + realtimePrice()) 
#             startshowing = False
        
#         looptime -= 1
    
# timeloop()

