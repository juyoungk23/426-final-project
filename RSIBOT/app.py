from flask import Flask, render_template, request, flash, redirect, jsonify
from binance.client import Client
import config
import csv


app = Flask(__name__)
client = Client(config.API_KEY, config.API_SECRET, tld="us")


@app.route("/")
def index():
    title = "Charting Website"
    info = client.get_account()
    balances = info["balances"]
    print(balances)
    return render_template("index.html", title=title, balances=balances)


@app.route("/login")
def login():
    return "<h1>This is the Login page</h1>"


@app.route("/tokens/<ticker>")
def tokens(ticker):
    return "The coin is %s" % ticker


@app.route("/post/<int:post_id>")
def post(post_id):
    return "<h2>Post ID is %s</h2>" % post_id


@app.route("/history")
def history():
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


if __name__ == "__main__":
    app.run(debug=False)
