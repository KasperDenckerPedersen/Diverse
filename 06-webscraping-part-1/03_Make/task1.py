import requests
import bs4


while True:
    tickers = ['UBER', 'AAPL', 'NVDA', 'AMD', 'MBG.DE']
    
    searchName = int(input("Choose a company:\n1. For Uber\n2. for Apple\n3. for Nvidia\n4. for AMD\n5. for Mercedes Benz\n>"))
    if searchName == 1:
        ticker = tickers[0]
    elif searchName == 2:
        ticker = tickers[1]
    elif searchName == 3:
        ticker = tickers[2]
    elif searchName == 4:
        ticker = tickers[3]
    elif searchName == 5:
        ticker = tickers[4]
    else: 
        print("Error, not a valid number")

    userAgent = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
    }

    url = f'https://finance.yahoo.com/quote/{ticker}?p={ticker}'
    r = requests.get(url, headers=userAgent)
    if r.status_code == 200:
        htmlText = r.text
        htmlDocument = bs4.BeautifulSoup(htmlText, 'html.parser')
        search = {'data-field': 'regularMarketPrice'}
        searchPriceChange = {'data-field': 'regularMarketChange'}
        searchPreviousClose = {'data-field': 'regularMarketPreviousClose'}
        searchOpen = {'data-field': 'regularMarketOpen'}
        searchMarketCap = {'data-field': 'marketCap'}
        searchPE = {'data-field': 'trailingPE'}

        price = htmlDocument.find('fin-streamer', search).text.strip()
        priceChange = htmlDocument.find('fin-streamer', searchPriceChange).text.strip()
        PreviousClose = htmlDocument.find('fin-streamer', searchPreviousClose).text.strip()
        OpenRate = htmlDocument.find('fin-streamer', searchOpen).text.strip()
        MarketCap = htmlDocument.find('fin-streamer', searchMarketCap).text.strip()
        PE = htmlDocument.find('fin-streamer', searchMarketCap).text.strip()

        print(f'{ticker}: {price}')
        print(f'Price Change: {priceChange}')
        print(f'Previous Close: {PreviousClose}')
        print(f'Open: {OpenRate}')
        print(f'Market Cap: {MarketCap}')
        print(f'PE: {PE}')
    else:
        print(f'{ticker}: failed (Status Code: {r.status_code})')
    break
