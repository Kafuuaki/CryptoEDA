import ccxt

binance = ccxt.binance()
markets = binance.load_markets()

ticker = binance.fetch_ticker('BTC/USDT')

USDTPair = 0

for markets in markets:
    if markets.split('/')[1] == 'USDT':
        USDTPair += 1

print(f'Binance has {USDTPair} USDT trading pairs')