import sys

# setting path
sys.path.append('..')

import requests
import classified


def get_wx_articles(num=100):
    response = requests.get("{}/crawl-articles/{}".format(classified.BACKEND_ADDRESS, num), timeout=600)
    print(response.content.decode("unicode_escape"))


if __name__ == '__main__':
    get_wx_articles()
