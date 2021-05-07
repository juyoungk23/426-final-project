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


@app.route("/index")
def index():
    title = "Juyoung's Final Project"
    # info = client.get_account()
    # balances = info["balances"]

    return render_template("index.html", title=title)


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/chart", methods=["post"])
def chart():

    symbol = request.form["symbol"]
    lowercaseSymbol = symbol.lower()
    myFile = symbol + "chart.html"

    srcName = "{{ url_for('static', filename='" + symbol + "chart.js')}}"
    if request.method == "POST":

        print(symbol)
    title = symbol + " / USD"

    return render_template(myFile, title=title, symbol=symbol, srcName=srcName)


@app.route("/ethusdt")
def ethusdt():
    title = "Ethereum"
    return render_template("ETHchart.html", title=title)


@app.route("/btcusdt")
def btcusdt():
    title = "Bitcoin"
    return render_template("BTCchart.html", title=title)


@app.route("/adausdt")
def adausdt():
    title = "Cardano"
    return render_template("ADAchart.html", title=title)


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


if __name__ == "__main__":
    app.debug = True
    app.run()
