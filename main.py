import argparse
import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv
from requests.exceptions import HTTPError


def count_clicks(token, bitlink):

    bitlink_parsed = urlparse(bitlink)
    bitlink_body = bitlink_parsed.netloc + bitlink_parsed.path
    headers = {'Authorization': token}
    params = {'units': '-1'}
    source = 'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    response = requests.get(source.format(bitlink=bitlink_body), headers=headers, params=params)
    response.raise_for_status()
    response_decoded = response.json()
    return response_decoded['total_clicks']


def is_bitlink(token, url):

    url_parsed = urlparse(url)
    url_body = url_parsed.netloc + url_parsed.path
    source = 'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'
    headers = {'Authorization': token}
    response = requests.get(source.format(bitlink=url_body), headers=headers)
    return response.ok


def shorten_link(token, url):

    headers = {'Authorization': token}
    user_url = {'long_url': url}
    source = 'https://api-ssl.bitly.com/v4/bitlinks'
    response = requests.post(source, json=user_url,  headers=headers)
    response.raise_for_status()
    response_decoded = response.json()
    return response_decoded['link']


def main():

    load_dotenv()
    token = os.getenv("BITLY_TOKEN")
    parser = argparse.ArgumentParser()
    parser.add_argument('user_url', help='Вставьте ссылку')
    arguments = parser.parse_args()
    bitly_token = 'Bearer {token}'
    formated_bitly_token = bitly_token.format(token=token)

    try:
        if is_bitlink(formated_bitly_token, arguments.user_url):
            transitions_quantity = count_clicks(formated_bitly_token, arguments.user_url)
            print(f'Количество переходов: {transitions_quantity}')
        else:
            bitlink = shorten_link(formated_bitly_token, arguments.user_url)
            print(f'Битлинк: {bitlink}')

    except HTTPError as http_error:
        print(f'HTTP error occurred: {http_error}')


if __name__ == '__main__':
    main()

