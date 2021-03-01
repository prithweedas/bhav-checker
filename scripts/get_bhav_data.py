import requests
from datetime import datetime
import csv
from zipfile import ZipFile
from io import BytesIO, TextIOWrapper
from redisearch import Client, IndexDefinition, TextField, NumericField


def get_redis_client() -> Client:
    client = Client('bhav-index', host='127.0.0.1', port=6379)
    definition = IndexDefinition(prefix=['bhav:'])
    try:
        client.create_index(
            (TextField('code', no_stem=True),
             TextField('name'),
             NumericField('open', sortable=True),
             NumericField('high', sortable=True),
             NumericField('low', sortable=True),
             NumericField('close', sortable=True)),
            definition=definition)
    except Exception as e:
        # INFO: index already exists
        print(e)
    return client


def get_file_name() -> str:
    '''get prev day's file name if current hour < 18'''
    current_date = datetime.now()
    hour = current_date.hour
    weekday = current_date.weekday()
    if weekday == 5:
        day = current_date.day - 1
    if weekday == 6:
        day = current_date.day - 2
    elif hour < 18:
        day = current_date.day - 1
    else:
        day = current_date.day
    return f'EQ{str(day).zfill(2)}{current_date.strftime("%m%y")}'


def get_data(filename: str) -> csv.DictReader:
    '''
    - Download zip from bse
    - extract the csv'''
    url = f'https://www.bseindia.com/download/BhavCopy/Equity/{filename}_CSV.ZIP'
    headers = {
        'user-agent': 'Bhav App'
    }
    response = requests.get(url=url, stream=True, headers=headers)
    zipfile = ZipFile(BytesIO(response.content))
    return csv.DictReader(TextIOWrapper(zipfile.open(f'{filename}.CSV', 'r'), 'utf-8'))


def main():
    filename = get_file_name()
    data = get_data(filename)
    client = get_redis_client()
    for item in data:
        client.redis.hset(f'bhav:{item.get("SC_CODE")}',
                          mapping={
                              'code': item.get('SC_CODE'),
                              'name': item.get('SC_NAME').strip(),
                              'open': item.get('OPEN'),
                              'high': item.get('HIGH'),
                              'low': item.get('LOW'),
                              'close': item.get('CLOSE')
                          })

    print(f'done >> {filename}')


if __name__ == '__main__':
    main()
