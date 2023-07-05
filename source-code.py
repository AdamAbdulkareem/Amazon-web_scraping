# import libraries
from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime

# connect to amazon website
URL = "https://www.amazon.com/Apple-MacBook-Pro-Early-2023/dp/B0BZFNLQ4B/ref=sr_1_3?crid=769U42S0EEX9&keywords=macbook+pro+2023&qid=1688547724&sprefix=macbook+pro+2023%2Caps%2C287&sr=8-3"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Upgrade-Insecure-Requests": "1",
}

page = requests.get(URL, headers=headers)

soup_1 = BeautifulSoup(page.content, "html.parser")
soup_2 = BeautifulSoup(soup_1.prettify(), "html.parser")

title = soup_2.find(id='productTitle').get_text()

print(title)