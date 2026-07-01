# Binance Futures Testnet Trading Bot

## Overview

This is a Python CLI application that places BUY and SELL orders on Binance Futures Testnet (USDT-M).

## Features

- Place MARKET orders
- Place LIMIT orders
- BUY and SELL support
- Command-line interface using argparse
- Input validation
- Logging of requests, responses, and errors
- Exception handling

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│   └── __init__.py
│
├── logs/
├── cli.py
├── requirements.txt
├── README.md
└── .env
```

## Installation

```bash
pip install -r requirements.txt
```

## Configure API Keys

Create a `.env` file:

```
API_KEY=your_api_key
API_SECRET=your_api_secret
```

## Run Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

## Run Limit Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000
```

## Assumptions

- Binance Futures Testnet is used.
- API credentials are stored in `.env`.
- Python 3.14 or later.

## Logs

Logs are stored inside:

```
logs/trading.log
```
