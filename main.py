import argparse
import json
import requests
import os

from dotenv import load_dotenv
from urllib.parse import urlparse


def shorten_url(token, url):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }
    url = {"long_url": url}
    response = requests.post('https://api-ssl.bitly.com/v4/shorten',
                             json=url, headers=headers)
    response.raise_for_status()
    return response.json()['id']


def count_clicks(token, url):
    headers = {'Authorization': f'Bearer {token}'}
    url = urlparse(url)
    response = requests.get(
            f'https://api-ssl.bitly.com/v4/bitlinks/'
            f'{url.netloc}{url.path}/clicks/summary',
            headers=headers
    )
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(token, url):
    headers = {'Authorization': f'Bearer {token}'}
    url = urlparse(url)
    response = requests.get(
            f'https://api-ssl.bitly.com/v4/bitlinks/{url.netloc}{url.path}',
            headers=headers
    )
    return response.ok


def main():
    load_dotenv()
    token = os.getenv('BITLY_TOKEN')
    parser = argparse.ArgumentParser()
    parser.add_argument(
            "url",
            help="Shorten entered url using bit.ly API",
            type=str
    )
    args = parser.parse_args()
    try:
        if not is_bitlink(token, args.url):
            bitlink = shorten_url(token, args.url)
            print(f"Битлинк {bitlink}")
            return
        count = count_clicks(token, args.url)
        print(f"По вашей ссылке прошли {count} раз(а)")
    except requests.exceptions.RequestException as e:
        print(f"Проверьте ссылку на правильность.\n{e}")


if __name__ == '__main__':
    main()
