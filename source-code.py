# import libraries
from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime

# connect to amazon website
URL = "https://www.amazon.com/Apple-MacBook-Laptop-12%E2%80%91core-19%E2%80%91core/dp/B0BSHDT7F5/ref=psdc_565108_t1_B0BZFNLQ4B"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Upgrade-Insecure-Requests": "1",
}

page = requests.get(URL, headers=headers)

soup_1 = BeautifulSoup(page.content, "html.parser")
soup_2 = BeautifulSoup(soup_1.prettify(), "html.parser")

title = soup_2.find(id="productTitle").get_text()
price = soup_2.find(class_="a-offscreen").get_text()
rating = soup_2.find(class_="a-icon-alt").get_text()

print(title.encode('utf-8'))
print(price)
print(rating)