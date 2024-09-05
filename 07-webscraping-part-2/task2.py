import requests
import json

def get_data(start):

    url = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing"

    querystring = {"start": start,"limit":"1000","sortBy":"market_cap","sortType":"desc","convert":"USD,BTC,ETH","cryptoType":"all","tagType":"all","audited":"false","aux":"ath,atl,high24h,low24h,num_market_pairs,cmc_rank,date_added,max_supply,circulating_supply,total_supply,volume_7d,volume_30d,self_reported_circulating_supply,self_reported_market_cap"}
    payload = ""
    headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    data = json.loads(response.text)
    data = data['data']['cryptoCurrencyList']
    return data

#print(data['data'].keys())
#print(f" Found a total of {data['data']['totalCount']} coins on the website")

cryptoCurrencies = []
for i in range(1, 100, 100):
    data = get_data(i)
    cryptoCurrencies = cryptoCurrencies + data

#cryptoCurrencies = get_data(1)

for coin in cryptoCurrencies:
    print(coin['name'])