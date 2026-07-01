from binance.enums import *
from bot.client import client
from bot.logging_config import logger


def place_order(symbol, side, order_type, quantity, price=None):
    try:

        logger.info(
            f"Request -> Symbol:{symbol}, Side:{side}, Type:{order_type}, Qty:{quantity}, Price:{price}"
        )

        if order_type == "MARKET":

            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=FUTURE_ORDER_TYPE_MARKET,
                quantity=quantity
            )

        elif order_type == "LIMIT":

            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=FUTURE_ORDER_TYPE_LIMIT,
                quantity=quantity,
                price=price,
                timeInForce=TIME_IN_FORCE_GTC
            )

        logger.info(f"Response -> {response}")

        return response

    except Exception as e:

        logger.error(str(e))

        raise