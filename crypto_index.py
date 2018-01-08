import coinmarketcap
import threading
import datetime

REFRESH_RATE_SECS=5.0
ANONYMITY_COINS=["monero",
				 "zcash",
				 "pivx",
				 "zcoin",
				 "komodo",
				 "nav-coin",
				 "verge",
				 "dash"]

def fetch_coin_data(coin_name):
	return (market.ticker(coin_name))

def fetch_all_coins_data():
	coins=market.ticker()
	return coins

def index_calculation(coins):
	market_cap_total=0
	cap_index=0;
	for i in range(0,len(coins)):
		market_cap_total+=float(coins[i]["market_cap_usd"])

	for i in range(0,len(coins)):
		cap_index+=((float(coins[i]["market_cap_usd"])/market_cap_total)
					*float(coins[i]["price_usd"]))
	return cap_index


def calculate_all_indices():
	threading.Timer(REFRESH_RATE_SECS,calculate_all_indices).start()		#Timer to call function every X secs
	coins=fetch_all_coins_data()
	top_10_index=index_calculation(coins[0:9])								#Calculate index for top 10 coins
	coins=[]
	for i in range(0,len(ANONYMITY_COINS)):									#Fetch anonymity based coins 
		coins+=fetch_coin_data(ANONYMITY_COINS[i])
		print("Fetched : " + ANONYMITY_COINS[i])							#Because this API is slow I dont know if the program has hanged
	anonymity_index=index_calculation(coins)

	print("Top 10 Index Price @ "+ str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + " : $" + '%.2f' %top_10_index)
	print("Anonymity Index @ "+ str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + " : $" + '%.2f \n' %anonymity_index)

market=coinmarketcap.Market()
calculate_all_indices()						
