# Stock Notifier
A `Python` powered tool to send push notifications if certain stocks hit configured marks.

`Stock Notifier` checks if a set of stocks that you can provide in a json file hit marks you can
specify for each of these stocks. If yes, it sends a push notification to your phone.


## Prerequisites
`Stock Notifier` requires Python version `3.9.1`.  
`Stock Notifier` downloads further required packages during setup.


## Installation
Review and run the file `setup.sh`:
```bash
bash setup.sh
```

The script sets up a Python virtual environment and installs further dependencies.


## Usage
To run the `Stock Notifier`, review and run the script `notify.sh`:
```bash
bash notify.sh
```

The script expects a file with name `stocks.json` in the current working directory.
The contents of the `stocks.json` should look like follows:
```json
{
    "my_stock": {
        "ticker_symbol": "ABC1.DE",
        "high": 100.1,
        "low": 50.05,
        "currency":"EUR"
    },
    ...
}
```
The top-level keys are readable names for a stock.  
The key `ticker_symbol` denotes the stock's ticker symbol. Search your stock via
https://finance.yahoo.com to find the ticker symbols that you need.  
The keys `high` and `low` denote the high and low marks in Euros that the stock notifier uses to
determine whether it should notify you.  
The key `currency` denotes the currency of the stock/ticker. The notifier uses this currency to
calculate the value of the stock to Euros.  


## Contributing
Work on your stuff locally, branch, commit and modify to your heart's content.
If there is anything you can extend, fix or improve, please do so!
Happy coding!


## LICENSE
See LICENSE file.


## Roadmap
1. Find a way to easily get realtime stock information
