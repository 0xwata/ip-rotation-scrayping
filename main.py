import requests
import os
from dotenv import load_dotenv
from ip_rotating_scrayper import IpRotatingScraper
from bs4 import BeautifulSoup

URL = "https://www.0xwata.com/"


def main():
    scraper = IpRotatingScraper(url=URL)
    content = scraper.request()
    soup = BeautifulSoup(content, "html.parser")
    # タグなどを指定して抽出する


def get_gip_addr():
    res = requests.get('https://ifconfig.me', proxies=proxies)
    return res.text


if __name__ == '__main__':
    main()
