# import libraries
from bs4 import BeautifulSoup
import requests
import csv
import os
import smtplib
from datetime import date
from datetime import datetime
import re

def check_price(identifier):
            URL = f"https://www.amazon.com/dp/{str(identifier)}"
            
            headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Upgrade-Insecure-Requests": "1",
            }
            
            page = requests.get(URL, headers=headers)
            page.raise_for_status()

            soup = BeautifulSoup(page.content, "html.parser")
            
            if price_element := soup.find(class_="a-offscreen"):
                
                    pattern = r'^\$\d'   
                    
                    if re.match(pattern, price_element.get_text()):
                        price = price_element.get_text()
                        
                    else:
                        price = "N/A"
                                
            if ratings_element:= soup.find(class_="a-icon-alt"):
                
                    pattern = r"\d\.\d out of \d stars"
                    
                    if re.match(pattern, ratings_element.get_text()):
                        ratings = ratings_element.get_text()
                        
                    else:
                        ratings = "N/A"
            
            num_reviews_element = soup.find(id="acrCustomerReviewText", class_="a-size-base")
            num_reviews = num_reviews_element.get_text() if num_reviews_element else "N/A"
            
            current_date = date.today().strftime("%B %d, %Y")
            current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            
            return price, ratings, num_reviews, current_date, current_time
        
def extract_product_names():
    for num in range(1, 2):
        URL = (
            "https://www.amazon.com/s?k=macbook&i=electronics&rh=n%3A172282%2Cp_89%3AApple%2Cp_n_availability%3A2661601011&page="
            + str(num)
        )
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Upgrade-Insecure-Requests": "1",
        }

        try:
            page = requests.get(URL, headers=headers)
            page.raise_for_status()

            soup = BeautifulSoup(page.content, "html.parser")

            title_elements = soup.select("[data-component-type='s-product-image'] img")
            id_elements = soup.select("[data-asin][data-component-type='s-search-result']")
            
            file_path = "./Amazon_Web_Dataset.csv"
            
            
            if not os.path.exists(file_path):
                header = ["Title", "ID", "Price", "Ratings", "Number of reviews", "Date", "Time"] 
                with open("Amazon_Web_Dataset.csv", mode="w", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerow(header)
                    
                    
            for title_element, element in zip(title_elements, id_elements):
                
                product_name = title_element.get("alt")
                identifier = element["data-asin"]
                
                price, ratings, num_reviews, date = check_price(identifier)
                
                data = [product_name, identifier, price, ratings, num_reviews, date]   
                with open("Amazon_Web_Dataset.csv", mode="a+", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerow(data)
            
        except requests.RequestException as e:
            return f"An error occurred: {type(e).__name__} - {str(e)}"
        
    
            
extract_product_names()

# while(True):
#     check_price()
#     time.sleep(10)
