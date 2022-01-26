import websocket, json

#BTC live price
ccBTC = 'btcusd' #index of coin
interval = '1m' #here we change computation time, 1/3/15/30/60m
socketBTC = f'wss://stream.binance.com:9443/ws/{ccBTC}t@kline_{interval}' #socket of BTC api

def on_message(ws, message):
    print(message)

def on_close(ws):
    print('### CLOSED CONNECTION ###')

wsBTC = websocket.WebSocketApp(socketBTC,on_message = on_message, on_close = on_close)

#ETH live price
ccETH = 'ethusd'
socketETH = f'wss://stream.binance.com:9443/ws/{ccETH}t@kline_{interval}' # socket of eth api

def on_messageETH(ws, message):
    print(message)

def on_closeETH(ws):
    print('### CLOSED CONNECTION ###')

wsETH = websocket.WebSocketApp(socketETH, on_message = on_message, on_close = on_close)

#BNB live price
ccBNB = 'bnbusd'
socketBNB = f'wss://stream.binance.com:9443/ws/{ccBNB}t@kline_{interval}' # socket of bnb api

def on_messageBNB(ws, message):
    print(message)

def on_closeBNB(ws):
    print('### CLOSED CONNECTION ###')

wsETH = websocket.WebSocketApp(socketBNB, on_message = on_message, on_close = on_close)