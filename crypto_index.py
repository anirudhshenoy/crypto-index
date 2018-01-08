import coinmarketcap
import threading
import datetime

REFRESH_RATE_SECS=5.0

def fetch_coins_data():
	coins=market.ticker()
	return coins

def calculate_index():
	threading.Timer(REFRESH_RATE_SECS,calculate_index).start()		#Timer to call function every X secs
	coins=fetch_coins_data()
	market_cap_top10=0
	cap_index=0;
	for i in range(0,9):
		market_cap_top10+=float(coins[i]["market_cap_usd"])

	for i in range(0,9):
		cap_index+=((float(coins[i]["market_cap_usd"])/market_cap_top10)
					*float(coins[i]["price_usd"]))
		
	print("Index Price @ "+ str(datetime.datetime.now()) + " : $" + str(cap_index))

market=coinmarketcap.Market()
calculate_index()						
