#!/usr/bin/env python3
import requests
import json
import os
from datetime import datetime

STOCKS = [
    {'symbol': 'GALP.LS', 'name': 'Galp'},
    {'symbol': 'EDP.LS',  'name': 'EDP'},
    {'symbol': 'JMT.LS',  'name': 'Jerónimo Martins'},
    {'symbol': 'BCP.LS',  'name': 'BCP Millennium'},
    {'symbol': 'NVG.LS',  'name': 'Navigator'},
    {'symbol': 'SEM.LS',  'name': 'Semapa'},
    {'symbol': 'ALTR.LS', 'name': 'Altri'},
    {'symbol': 'MOTA.LS', 'name': 'Mota-Engil'},
    {'symbol': 'CTT.LS',  'name': 'CTT'},
    {'symbol': 'SON.LS',  'name': 'Sonae'},
    {'symbol': 'EDPR.LS', 'name': 'EDP Renováveis'},
    {'symbol': 'REN.LS',  'name': 'REN'},
]

def fetch_psi():
    symbols = ','.join(s['symbol'] for s in STOCKS)
    url = f'https://query1.finance.yahoo.com/v7/finance/quote?symbols={symbols}&lang=pt&region=PT'
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        r = requests.get(url, headers=headers, timeout=30)
        data = r.json()
        quotes = data['quoteResponse']['result']
    except Exception as e:
        print(f'Error fetching data: {e}')
        return None

    name_map = {s['symbol']: s['name'] for s in STOCKS}
    result = []
    for q in quotes:
        sym = q.get('symbol', '')
        price = q.get('regularMarketPrice')
        change = q.get('regularMarketChange')
        pct = q.get('regularMarketChangePercent')
        volume = q.get('regularMarketVolume')
        result.append({
            'symbol': sym,
            'name': name_map.get(sym, sym),
            'price': round(price, 3) if price else None,
            'change': round(change, 3) if change else None,
            'changePct': round(pct, 2) if pct else None,
            'volume': volume,
        })

    return {
        'updated': datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
        'stocks': result
    }

if __name__ == '__main__':
    data = fetch_psi()
    if data:
        os.makedirs('data', exist_ok=True)
        with open('data/psi.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Saved {len(data['stocks'])} stocks to data/psi.json")
        print(f"Updated at: {data['updated']}")
    else:
        print("Failed to fetch data")
        exit(1)
