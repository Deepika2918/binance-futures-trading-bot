import argparse

from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)


def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True, help="Example: BTCUSDT")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:

        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price, order_type)

        print("\n========== ORDER REQUEST ==========")
        print(f"Symbol   : {args.symbol}")
        print(f"Side     : {side}")
        print(f"Type     : {order_type}")
        print(f"Quantity : {quantity}")

        if price:
            print(f"Price    : {price}")

        print("===================================")

        response = place_order(
            symbol=args.symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        print("\n✅ Order Placed Successfully!\n")

        print("Order ID      :", response.get("orderId"))
        print("Status        :", response.get("status"))
        print("Executed Qty  :", response.get("executedQty"))
        print("Average Price :", response.get("avgPrice"))

    except Exception as e:

        print("\n❌ Error:", e)


if __name__ == "__main__":
    main()