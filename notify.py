"""A tool that sends a push notification if certain stocks hit certain marks."""
import datetime as dt
import json
import logging
import pathlib
from typing import Any, Dict

import currency_converter as cc
import requests
import urllib3
import yfinance as yf

logging.basicConfig(
    format="%(asctime)s [%(levelname)s]: %(message)s",
    datefmt="%a %b %d %H:%M:%S %Y",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def read_stocks(json_file: pathlib.Path) -> Dict[str, Any]:
    """Load the stocks entries from the given json file."""
    with open(json_file, "r+") as file:
        return json.load(file)


def send_pushover(message: str):
    """Log the given message nad send a push notification with the message
    via the service `pushover.net`."""
    logger.info(message)
    data = {
        "message": message,
        "token": "agna4fob6wu7e7t2ofhz1drt7ptngq",
        "user": "ucw67xi5r5mqgqo8arh3p64xkj39wu",
    }
    try:
        return requests.post("https://api.pushover.net/1/messages.json", data)
    except urllib3.exceptions.MaxRetryError:
        logger.error("Post to pushover encountered MaxRetryError. Giving up.")


def main():
    """Check the courses of some stocks and send a push notification if these
    stocks cross certain high or low marks."""
    stocks = read_stocks("stocks.json")
    currency_converter = cc.CurrencyConverter()

    today_date = dt.datetime.now().date()
    today = str(dt.datetime.now().date())
    tomorrow = str(today_date + dt.timedelta(days=1))

    for stock, details in stocks.items():
        ticker = yf.Ticker(details["ticker_symbol"])
        df = ticker.history(period="1d", start=today, end=tomorrow)

        rate = currency_converter.convert(1, details.get("currency", "EUR"), "EUR")
        price_euros = df.iloc[0]["Open"] * rate

        if price_euros < details["low"]:
            send_pushover(f"Price for {stock} is low: {price_euros:0.2f}€")
        elif price_euros > details["high"]:
            send_pushover(f"Price for {stock} is high: {price_euros:0.2f}€")


if __name__ == "__main__":
    logger.info("Checking...")
    try:
        main()
    except Exception:
        logger.exception("Stock Notifier encountered an uncaught exception")
