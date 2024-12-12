# Python Market Data API
## Reference
[Market Data HTML Docs](https://www.marketdata.app/docs/api)
## Examples

### Loading API Key
```python
import MarketDataLib as mdl

mdl.API_KEY = '420.69'
```

### Downloading Historical Data
```python
symbols = ['AAPL', 'TSLA', 'TSLA250117C00360000', 'PLTR250117C00050000', 'MSTR241220C00190000']
mdl.get_historicals(
    symbols=symbols,
    start_date='2024-11-01',
    end_date='2024-11-05',
)

print(df)
```

### Downloading Quote Data
```python
mdl.get_quotes(['TSLA', 'TSLA250117C00360000'])
print(df)
```


### Downloading Single Stock Historical Data
```python
df = mdl.get_stock_historical(
    symbol='MSFT',
    start_date='2021-01-01',
    end_date='2021-01-31',
    resolution='2W',
)
print(df)
```

### Downloading Single Stock Quote Data
```python
df = mdl.get_stock_quote(
    symbol='TSLA',
    cached=True
)
print(df)
```

### Downloading Multiple Stock Historical Data
```python
df = mdl.get_stock_historicals(
    symbols=['AAPL', 'TSLA', 'MSTR'],
    start_date='2021-01-01',
    end_date='2021-01-31',
    resolution='1W',
)
print(df)
```

### Downloading Multiple Stock Quote Data
```python
symbols = ['AAPL', 'AMC', 'AMD', 'AMZN', 'COIN']
df = mdl.get_stock_quotes(symbols)
print(df)
```

### Downloading Single Option Historical Data
```python
df = mdl.get_option_historical(
    symbol='TSLA250117C00360000',
    start_date='2024-11-01',
    end_date='2024-11-10',
)
print(df)
```

### Downloading Multiple Option Historical Data
```python
symbols = ['TSLA250117C00360000', 'PLTR250117C00050000', 'MSTR241220C00190000']
df = mdl.get_option_historicals(
    symbols,
    start_date='2024-11-01',
    end_date='2024-11-10',
)
print(df)
```

### Downloading Single Option Quote Data
```python
df = mdl.get_option_quote(
    symbol='TSLA250117C00360000',
    cached=True
)
print(df)
```

### Downloading Multiple Option Quote Data
```python
symbols = ['TSLA250117C00360000', 'PLTR250117C00050000', 'MSTR241220C00190000']
df = mdl.get_option_quotes(symbols)
print(df)
```
