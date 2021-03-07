from bs4 import BeautifulSoup
import requests
import lxml

url = "https://www.amazon.de/-/en/dp/B07YCRQBB9/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/88.0.4324.190 Safari/537.36",
    "Accept-Language": "de-DE,de;q=0.9,en;q=0.8,en-US;q=0.7"
}

response = requests.get(url, headers=headers).text

soup = BeautifulSoup(response, "lxml")

price = soup.find(name="span", class_="priceBlockBuyingPriceString")

price = price.getText()

price = float(price[1:])

target = 10.00

if price <= target:
    print(f"The price is now {price}. You should consider buying.")
