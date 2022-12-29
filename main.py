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
    data = {"long_url": url}
    response = requests.post('https://api-ssl.bitly.com/v4/shorten',
                             json=data, headers=headers)
    response.raise_for_status()
    return response.json()['id']


def clean_url_for_bitly_api(url):
    data = urlparse(url)
    if data.fragment:
        return f'{data.netloc}{data.path}#{data.fragment}'
    return f'{data.netloc}{data.path}'


def count_clicks(token, url):
    headers = {'Authorization': f'Bearer {token}'}
    url = clean_url_for_bitly_api(url)
    response = requests.get(
            f'https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks/summary',
            headers=headers
    )
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(token, url):
    headers = {'Authorization': f'Bearer {token}'}
    url = clean_url_for_bitly_api(url)
    response = requests.get(
            f'https://api-ssl.bitly.com/v4/bitlinks/{url}',
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
    user_input = args.url
    try:
        if not is_bitlink(token, user_input):
            bitlink = shorten_url(token, user_input)
            print(f"Битлинк {bitlink}")
            return
        count = count_clicks(token, user_input)
        print(f"По вашей ссылке прошли {count} раз(а)")
    except requests.exceptions.RequestException as e:
        print(f"Проверьте ссылку на правильность.\n{e}")


if __name__ == '__main__':
    main()
