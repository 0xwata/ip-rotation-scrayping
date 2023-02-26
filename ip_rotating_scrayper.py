import requests
import os
from dotenv import load_dotenv


class IpRotatingScraper:
    def __init__(self, url):
        load_dotenv()
        # os.environを用いて環境変数を表示させます
        USER_NAME = os.environ['USER_NAME']
        PASSWORD = os.environ['PASSWORD']
        DOMAIN = os.environ['DOMAIN']
        PORT = os.environ['PORT']

        self.url = url
        self.proxies = {
            "http": "http://{0}:${1}@${2}:{3}".format(USER_NAME, PASSWORD, DOMAIN, PORT),
            "https": "http://{0}:{1}@{2}:{3}".format(USER_NAME, PASSWORD, DOMAIN, PORT),
        }

    def request(self) -> bytes:
        res = requests.get(self.url, proxies=self.proxies)
        print(res.status_code, ', your global ip: ' + self.__get_gip_addr())
        return res.content

    def __get_gip_addr(self) -> str:
        res = requests.get('https://ifconfig.me', proxies=self.proxies)
        return res.text
