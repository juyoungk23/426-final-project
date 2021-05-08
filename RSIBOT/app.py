from flask import Flask, render_template, request, flash, redirect, jsonify
from binance.client import Client

# import config
import csv
import os
from os import environ

API_KEY = environ["API_KEY"]
API_SECRET = environ["API_SECRET"]

app = Flask(__name__)
client = Client(API_KEY, API_SECRET, tld="us")

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/signout")
def signout():
    return render_template("signout.html")

@app.route("/home")
def index():
    title = "Juyoung's Final Project"
    # info = client.get_account()
    # balances = info["balances"]

    return render_template("index.html", title=title)

@app.route("/chart")
def chart():

    return render_template('chart.html')

@app.route("/chartCrypto", methods=['post'])
def chartCrypto():

    symbol = request.form["symbol"].upper()
    lowercaseSymbol = symbol.lower()
    # myFile = symbol + "chart.html"

    switcher = {
        "ETH": ethusdt(),
        "BTC": btcusdt(),
        "ADA": adausdt(),
        "ALGO": algousdt(),
        "DOGE": dogeusdt()
    }


    return switcher.get(symbol, "Invalid Symbol")


@app.route("/aboutProject")
def aboutProject():
    return render_template("aboutProject.html")


@app.route("/aboutCrypto")
def aboutCrypto():
    return render_template("aboutCrypto.html")


@app.route("/ethusdt")
def ethusdt():
    return render_template("ETHchart.html", title="Ethereum", symbol="ETH")


@app.route("/btcusdt")
def btcusdt():
    return render_template("BTCchart.html", title="Bitcoin", symbol="BTC")


@app.route("/adausdt")
def adausdt():
    return render_template("ADAchart.html", title="Cardano", symbol="ADA")

@app.route("/algousdt")
def algousdt():
    return render_template("ALGOchart.html", title="Algorand", symbol="ALGO")

@app.route("/dogeusdt")
def dogeusdt():
    return render_template("DOGEchart.html", title="Dogecoin", symbol="DOGE")



@app.route("/tokens/<ticker>")
def tokens(ticker):
    return "The coin is %s" % ticker


@app.route("/post/<int:post_id>")
def post(post_id):
    return "<h2>Post ID is %s</h2>" % post_id


@app.route("/ethusdthistory")
def ethusdthistory():
    # candles = client.get_klines(
    #     symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)
    # processed_candles = []

    # for data in candles:
    #     candlestick = {"time": data[0] / 1000, "open": data[1],
    #                    "high": data[2], "low": data[3], "close": data[4]}
    #     processed_candles.append(candlestick)
    # return jsonify(processed_candles)

    candlesticks = client.get_historical_klines(
        "ETHUSDT", Client.KLINE_INTERVAL_1WEEK, "1 Jan, 2017"
    )

    processed_candlesticks = []

    for data in candlesticks:
        candlestick = {
            "time": data[0] / 1000,
            "open": data[1],
            "high": data[2],
            "low": data[3],
            "close": data[4],
        }

        processed_candlesticks.append(candlestick)

    return jsonify(processed_candlesticks)


@app.route("/btcusdthistory")
def btcusdthistory():
    # candles = client.get_klines(
    #     symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)
    # processed_candles = []

    # for data in candles:
    #     candlestick = {"time": data[0] / 1000, "open": data[1],
    #                    "high": data[2], "low": data[3], "close": data[4]}
    #     processed_candles.append(candlestick)
    # return jsonify(processed_candles)

    candlesticks = client.get_historical_klines(
        "BTCUSDT", Client.KLINE_INTERVAL_1WEEK, "1 Jan, 2017"
    )

    processed_candlesticks = []

    for data in candlesticks:
        candlestick = {
            "time": data[0] / 1000,
            "open": data[1],
            "high": data[2],
            "low": data[3],
            "close": data[4],
        }

        processed_candlesticks.append(candlestick)

    return jsonify(processed_candlesticks)


@app.route("/adausdthistory")
def adausdthistory():
    # candles = client.get_klines(
    #     symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)
    # processed_candles = []

    # for data in candles:
    #     candlestick = {"time": data[0] / 1000, "open": data[1],
    #                    "high": data[2], "low": data[3], "close": data[4]}
    #     processed_candles.append(candlestick)
    # return jsonify(processed_candles)

    candlesticks = client.get_historical_klines(
        "ADAUSDT", Client.KLINE_INTERVAL_1WEEK, "1 Jan, 2017"
    )

    processed_candlesticks = []

    for data in candlesticks:
        candlestick = {
            "time": data[0] / 1000,
            "open": data[1],
            "high": data[2],
            "low": data[3],
            "close": data[4],
        }

        processed_candlesticks.append(candlestick)

    return jsonify(processed_candlesticks)


@app.route("/algousdthistory")
def algousdthistory():
    # candles = client.get_klines(
    #     symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)
    # processed_candles = []

    # for data in candles:
    #     candlestick = {"time": data[0] / 1000, "open": data[1],
    #                    "high": data[2], "low": data[3], "close": data[4]}
    #     processed_candles.append(candlestick)
    # return jsonify(processed_candles)

    candlesticks = client.get_historical_klines(
        "ALGOUSD", Client.KLINE_INTERVAL_1WEEK, "1 Jan, 2017"
    )

    processed_candlesticks = []

    for data in candlesticks:
        candlestick = {
            "time": data[0] / 1000,
            "open": data[1],
            "high": data[2],
            "low": data[3],
            "close": data[4],
        }

        processed_candlesticks.append(candlestick)

    return jsonify(processed_candlesticks)



@app.route("/dogeusdthistory")
def dogeusdthistory():
    # candles = client.get_klines(
    #     symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)
    # processed_candles = []

    # for data in candles:
    #     candlestick = {"time": data[0] / 1000, "open": data[1],
    #                    "high": data[2], "low": data[3], "close": data[4]}
    #     processed_candles.append(candlestick)
    # return jsonify(processed_candles)

    candlesticks = client.get_historical_klines(
        "DOGEUSDT", Client.KLINE_INTERVAL_1WEEK, "1 Jan, 2017"
    )

    processed_candlesticks = []

    for data in candlesticks:
        candlestick = {
            "time": data[0] / 1000,
            "open": data[1],
            "high": data[2],
            "low": data[3],
            "close": data[4],
        }

        processed_candlesticks.append(candlestick)

    return jsonify(processed_candlesticks)


if __name__ == "__main__":
    app.debug = True
    app.run()
