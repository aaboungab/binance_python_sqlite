import os
import json
from datetime import datetime
from binance import Client
import pprint
import sqlite3

connection = sqlite3.connect('btc_usdt.db')
cursor = connection.cursor()

try:
    cursor.execute("""
        CREATE TABLE btc_usdt (
            timestamp text,
            symbol text,
            openPrice int,
            highPrice int,
            lowPrice int,
            symbol_price int,
            priceChange int,
            priceChangePercent int
        )
    """)
except:
    pass

# Set up the Binance client
api_key = os.getenv('binance_api_key')
api_secret = os.getenv('binance_api_secret')
client = Client(api_key,api_secret)

# symbol to focus on
symbol = "BTCUSDT"

ticker = client.get_ticker(symbol=symbol)
current_timestamp = datetime.now().replace(second=0, microsecond=0).isoformat()
price_change = float(ticker['priceChangePercent'])
symbol_ticker = client.get_symbol_ticker(symbol=symbol)
symbol_ticker_price = symbol_ticker['price']

data = (current_timestamp, symbol, ticker['openPrice'], ticker['highPrice'], ticker['lowPrice'], symbol_ticker_price ,ticker['priceChange'], f"{price_change:.2f}%") 

print(",".join(map(str, data)))

cursor.execute("""
        INSERT INTO btc_usdt (
            timestamp, symbol, openPrice, highPrice, lowPrice, symbol_price, priceChange, priceChangePercent
        ) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, data)

connection.commit()
connection.close()
