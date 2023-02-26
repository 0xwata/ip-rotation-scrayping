import requests
import os
from dotenv import load_dotenv

load_dotenv()
# os.environを用いて環境変数を表示させます
USER_NAME = os.environ['USER_NAME']
PASSWORD = os.environ['PASSWORD']
DOMAIN = os.environ['DOMAIN']
PORT = os.environ['PORT']
URL = ""

proxies = {
    "http": "http://{0}:${1}@${2}:{3}".format(USER_NAME, PASSWORD, DOMAIN, PORT),
    "https": "http://{0}:{1}@{2}:{3}".format(USER_NAME, PASSWORD, DOMAIN, PORT),
}


def main():
    for i in range(10):
        res = requests.get(URL, proxies=proxies)
        print(res.status_code)
        print('your globalip: ' + get_gip_addr())


def get_gip_addr():
    res = requests.get('https://ifconfig.me', proxies=proxies)
    return res.text


if __name__ == '__main__':
    main()
