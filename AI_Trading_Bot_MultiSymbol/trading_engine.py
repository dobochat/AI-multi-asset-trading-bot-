import os
from kiteconnect import KiteConnect
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("Z_API_KEY")
api_secret = os.getenv("Z_API_SECRET")
access_token = os.getenv("Z_ACCESS_TOKEN")

kite = KiteConnect(api_key=api_key)
kite.set_access_token(access_token)

def run_trading_engine(mode, symbol, quantity):
    logs = []
    if mode == "real":
        logs.append(f"🔁 REAL MODE: Placing order for {symbol}, Qty: {quantity}")
        try:
            order_id = kite.place_order(
                variety=kite.VARIETY_REGULAR,
                exchange=kite.EXCHANGE_NSE if symbol.isalpha() else kite.EXCHANGE_NFO,
                tradingsymbol=symbol.upper(),
                transaction_type=kite.TRANSACTION_TYPE_BUY,
                quantity=int(quantity),
                order_type=kite.ORDER_TYPE_MARKET,
                product=kite.PRODUCT_MIS
            )
            logs.append(f"✅ Order placed successfully. Order ID: {order_id}")
        except Exception as e:
            logs.append(f"❌ Error placing order: {str(e)}")
    else:
        logs.append(f"📘 PAPER MODE: Simulating order for {symbol}, Qty: {quantity}")
        for i in range(3):
            logs.append(f"🧪 Simulated trade {i+1} for {symbol}...")
    return logs