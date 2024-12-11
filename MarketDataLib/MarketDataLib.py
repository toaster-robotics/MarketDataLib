import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
import time
from typing import Optional, List, Tuple, Union
import random

BASE_URL = 'https://api.marketdata.app'
API_KEY = ''


def fetch_url(url: str, params: Optional[dict] = None, headers: Optional[dict] = None, max_retries: int = 3, sleep: float = 2):
    attempts = 0
    while attempts < max_retries:
        try:
            response = requests.get(url, params, headers=headers)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            attempts += 1
            if attempts < max_retries:
                time.sleep(sleep)


def get_stock_historical(symbol: str, start_date: str, end_date: str, resolution: Union[str, int] = 'D') -> pd.DataFrame:
    endpoint = '/v1/stocks/candles/%s/%s/' % (resolution, symbol.upper())
    params = {
        'from': start_date,
        'to': end_date,
    }
    headers = {
        'Authorization': 'Bearer %s' % API_KEY,
        'Accept': 'application/json'
    }
    response = fetch_url(BASE_URL + endpoint, params, headers)
    if response is None:
        print('no data found')
        return pd.DataFrame()
    if response.status_code in [200, 203]:
        data = response.json()
        df = pd.DataFrame(data)
        if df.empty:
            print('no data found for %s - %s' % (start_date, end_date))
            return pd.DataFrame()
        df['date'] = pd.to_datetime(df['t'], unit='s')
        df = df.rename(columns={'o': 'open', 'h': 'high',
                                'l': 'low', 'c': 'close', 'v': 'volume'})
        df['symbol'] = symbol
        df = df[['date', 'symbol', 'open', 'high', 'low',
                'close', 'volume']].reset_index(drop=True)
        return df
    else:
        print(response.text)
        return pd.DataFrame()


def get_stock_quote(symbol: str, cached: bool = True) -> pd.DataFrame:
    endpoint = '/v1/stocks/quotes/%s' % symbol.upper()
    params = {
        'feed': 'cached' if cached else 'live'
    }
    headers = {
        'Authorization': 'Bearer %s' % API_KEY,
        'Accept': 'application/json'
    }
    response = fetch_url(BASE_URL + endpoint, params, headers)
    if response is None:
        print('no data found')
        return pd.DataFrame()
    if response.status_code in [200, 203]:
        data = response.json()
        df = pd.DataFrame(data)
        if df.empty:
            print('no data found')
            return pd.DataFrame()
        df['date'] = pd.to_datetime(df['updated'], unit='s')
        df = df.rename(columns={'bidSize': 'bid_size',
                       'askSize': 'ask_size', 'changepct': 'change_pct'})
        df = df[['date', 'symbol', 'bid', 'bid_size', 'mid', 'ask',
                 'ask_size', 'last', 'change', 'change_pct', 'volume']]
        return df
    else:
        print(response.text)
        return pd.DataFrame()


def get_stock_historicals(symbols: List[str], start_date: str, end_date: str, resolution: Union[str, int] = 'D') -> pd.DataFrame:
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(lambda symbol: get_stock_historical(
            symbol, start_date, end_date, resolution), symbols))
    df = pd.concat(results, ignore_index=True)
    return df


def get_stock_quotes(symbols: List[str], cached: bool = True) -> pd.DataFrame:
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(
            lambda symbol: get_stock_quote(symbol, cached), symbols))
    df = pd.concat(results, ignore_index=True)
    return df


def get_option_historical(symbol: str, start_date: str, end_date: str) -> pd.DataFrame:
    endpoint = '/v1/options/quotes/%s/' % symbol.upper()
    params = {
        'from': start_date,
        'to': end_date,
    }
    headers = {
        'Authorization': 'Bearer %s' % API_KEY,
        'Accept': 'application/json'
    }
    response = fetch_url(BASE_URL + endpoint, params, headers)
    if response is None:
        print('no data found')
        return pd.DataFrame()
    if response.status_code in [200, 203]:
        data = response.json()
        df = pd.DataFrame(data)
        if df.empty:
            print('no data found')
            return pd.DataFrame()
        df['date'] = pd.to_datetime(df['updated'], unit='s')
        df = df.rename(columns={'optionSymbol': 'symbol', 'bidSize': 'bid_size', 'askSize': 'ask_size',
                       'openInterest': 'open_interest', 'extrinsicValue': 'extrinsic_value', 'underlyingPrice': 'underlying_price'})
        df = df[['date', 'symbol', 'underlying', 'strike', 'bid', 'bid_size', 'mid', 'ask',
                 'ask_size', 'last', 'open_interest', 'volume', 'extrinsic_value', 'underlying_price']]
        return df
    else:
        print(response.text)
        return pd.DataFrame()


def get_option_quote(symbol: str, cached: bool = True) -> pd.DataFrame:
    endpoint = '/v1/options/quotes/%s/' % symbol.upper()
    params = {
        'feed': 'cached' if cached else 'live'
    }
    headers = {
        'Authorization': 'Bearer %s' % API_KEY,
        'Accept': 'application/json'
    }
    response = fetch_url(BASE_URL + endpoint, params, headers)
    if response is None:
        print('no data found')
        return pd.DataFrame()
    if response is None:
        print('no data found')
        return pd.DataFrame()
    if response.status_code in [200, 203]:
        data = response.json()
        df = pd.DataFrame(data)
        if df.empty:
            print('no data found')
            return pd.DataFrame()
        df['date'] = pd.to_datetime(df['updated'], unit='s')
        df = df.rename(columns={'optionSymbol': 'symbol', 'bidSize': 'bid_size', 'askSize': 'ask_size',
                       'openInterest': 'open_interest', 'extrinsicValue': 'extrinsic_value', 'underlyingPrice': 'underlying_price'})
        df = df[['date', 'symbol', 'underlying', 'strike', 'bid', 'bid_size', 'mid', 'ask', 'ask_size', 'last',
                 'open_interest', 'volume', 'extrinsic_value', 'underlying_price', 'iv', 'delta', 'gamma', 'theta', 'vega', 'rho']]
        return df
    else:
        print(response.text)
        return pd.DataFrame()


def get_option_historicals(symbols: List[str], start_date: str, end_date: str) -> pd.DataFrame:
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(lambda symbol: get_option_historical(
            symbol, start_date, end_date), symbols))
    df = pd.concat(results, ignore_index=True)
    return df


def get_option_quotes(symbols: str, cached: bool = True) -> pd.DataFrame:
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(
            lambda symbol: get_option_quote(symbol, cached), symbols))
    df = pd.concat(results, ignore_index=True)
    return df
