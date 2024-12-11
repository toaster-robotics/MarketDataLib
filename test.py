import MarketDataLib as mdl


with open('key') as f:
    mdl.API_KEY = f.readlines()[0].strip()


df = mdl.get_stock_historical(
    symbol='AAPL',
    start_date='2021-01-01',
    end_date='2021-01-31',
)
print(df)

df = mdl.get_stock_quote(
    symbol='TSLA',
    cached=True
)
print(df)

df = mdl.get_stock_historicals(
    symbols=['AAPL', 'TSLA', 'MSTR'],
    start_date='2021-01-01',
    end_date='2021-01-31',
)
print(df)

symbols = ['AAPL', 'AMC', 'AMD', 'AMZN', 'COIN']
df = mdl.get_stock_quotes(symbols)
print(df)

df = mdl.get_option_historical(
    symbol='TSLA250117C00360000',
    start_date='2024-11-01',
    end_date='2024-11-10',
)
print(df)

df = mdl.get_option_quote(
    symbol='TSLA250117C00360000',
    cached=True
)
print(df)


symbols = ['TSLA250117C00360000', 'PLTR250117C00050000', 'MSTR241220C00190000']
df = mdl.get_option_historicals(
    symbols,
    start_date='2024-11-01',
    end_date='2024-11-10',
)
print(df)

symbols = ['TSLA250117C00360000', 'PLTR250117C00050000', 'MSTR241220C00190000']
df = mdl.get_option_quotes(symbols)
print(df)
