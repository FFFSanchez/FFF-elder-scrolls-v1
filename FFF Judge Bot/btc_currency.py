import requests
from datetime import datetime

def get_data():
    req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
    response = req.json()
    sell_price = response["btc_usd"]["sell"]
    return f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price}"


#print(get_data())