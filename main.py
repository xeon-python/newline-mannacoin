import requests
def manna():
    url = 'https://api.coinmarketcap.com/v1/ticker/manna/'
    response = requests.get(url)
    value = response.json()[0]["price_usd"]
    rank = response.json()[0]["rank"]
    supply = response.json()[0]["total_supply"]
    change1 = response.json()[0]["percent_change_1h"]
    change24 = response.json()[0]["percent_change_24h"]
    change72 = response.json()[0]["percent_change_7d"]
    vol24 = response.json()[0]["24h_volume_usd"]
    sym = response.json()[0]["symbol"]
    print("Manna Coin's' price is: $" + value+"\nManna Coin's rank is: " + rank+"\nManna Coin's total supply is: " + supply+"\nManna Coin's percent change in the past hour is: "+change1+"\nManna Coin's percent change in the past 24 hours is: "+change24+"\nManna Coin's percent change in the past 7 days is: "+ change72+"\nManna Coin's 24 hour volume is: " + vol24+"\nManna Coin's symbol is: " + sym)
    print("MANNA EXECUTED")
