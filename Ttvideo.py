import re
import requests
from bs4 import BeautifulSoup
from aiogram import Bot, Dispatcher, types

headers = {
    'Accept-language': 'en',
    'User-Agent': 'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) '
                  'Version/4.0.4 Mobile/7B334b Safari/531.21.102011-10-16 20:23:10'
}
def fetch_video_id(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    link = soup.find_all('link')
    print(link)
    video_id = link.get("href")
    #video_id = link.split('/')[-1:][0]
    return print(link)

fetch_video_id("https://vm.tiktok.com/ZMjm6Ec7j/")
