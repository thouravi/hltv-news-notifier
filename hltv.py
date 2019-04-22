import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

url = 'https://www.hltv.org/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
result = requests.get(url, headers=headers)

src = result.content
soup = BeautifulSoup(src, 'lxml')

news = (soup.find(lambda tag: tag.name == 'div' and 
                                   tag.get('class') == ['newstext']))

time = (soup.find(lambda tag: tag.name == 'div' and 
                                   tag.get('class') == ['newsrecent']))

toaster = ToastNotifier()
toaster.show_toast("Latest HLTV Post - " + time.text,
                   news.text + ".",
                   icon_path="hltv.ico",duration=10)
