from binance.client import Client
import config
import csv

client = Client(config.API_KEY, config.API_SECRET)

prices = client.get_all_tickers()

# for price in prices:
#     print(price)

candles = client.get_klines(
    symbol="ETHUSDT", interval=Client.KLINE_INTERVAL_15MINUTE)

eth_weekly_klines = open("ethusdt-weekly-klines.csv", "w", newline="")

candlestick_writer = csv.writer(eth_weekly_klines, delimiter=",")

candlesticks = client.get_historical_klines(
    "ETHUSDT", Client.KLINE_INTERVAL_1WEEK, "1 Jan, 2017"
)

for candlestick in candlesticks:
    candlestick_writer.writerow((candlestick))


eth_weekly_klines.close()

# csvfile2 = open("btcusdt-weekly-klines.csv", "w", newline="")
# csvfile3 = open("dogeusdt-weekly-klines.csv", "w", newline="")
# csvfile4 = open("xrpusdt-weekly-klines.csv", "w", newline="")
# csvfile5 = open("algousdt-weekly-klines.csv", "w", newline="")
# csvfile6 = open("adausdt-weekly-klines.csv", "w", newline="")
# csvfile7 = open("linkusdt-weekly-klines.csv", "w", newline="")


# candlestick_writer2 = csv.writer(csvfile2, delimiter=",")
# candlestick_writer3 = csv.writer(csvfile3, delimiter=",")
# candlestick_writer4 = csv.writer(csvfile4, delimiter=",")
# candlestick_writer5 = csv.writer(csvfile5, delimiter=",")
# candlestick_writer6 = csv.writer(csvfile6, delimiter=",")

# fetch weekly klines eth since it listed


# def get_csv(symbol):
#     csvfile = open("{symbol}usdt-weekly-klines.csv", "w", newline="")
#     candlestick_writer = csv.writer(csvfile, delimiter=",")
#     return
