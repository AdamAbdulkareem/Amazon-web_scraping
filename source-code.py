# import libraries
from bs4 import BeautifulSoup
import requests
import csv
import os
import smtplib
import time
import datetime



def check_price():
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
    ratings = soup_2.find(class_="a-icon-alt").get_text()
    num_reviews = soup_2.find(id="acrCustomerReviewText").get_text()

    today = datetime.date.today()

    title = title.strip()
    price = price.strip()
    ratings = ratings.strip()
    num_reviews = num_reviews.strip()

    header = ["Title", "Price", "Rating", "Number of reviews", "Date"]
    data = [title, price, ratings, num_reviews, today]

    
    file_path = "./AmazonWebDataset.csv"
    if os.path.exists(file_path):
        # Now we are appending data to the csv file
        with open("AmazonWebDataset.csv", mode="a+", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(data)
        return
    else:
        with open("AmazonWebDataset.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerow(data)
        return

check_price()