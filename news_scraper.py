import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

url = "https://news.ycombinator.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

titles = soup.select(".titleline")

data = []

for title in titles:
    text = title.text
    link = title.find("a")["href"]

    data.append({
        "title": text,
        "link": link,
        "scraped_time": datetime.now()
    })

df = pd.DataFrame(data)

df.to_csv("news.csv", index=False)

print("Scraping complete! Data saved to news.csv")