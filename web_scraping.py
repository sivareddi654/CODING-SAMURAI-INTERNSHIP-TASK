import requests
from bs4 import BeautifulSoup
import csv

url = "https://news.ycombinator.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.select("span.titleline a")

with open("news_headlines.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Headline"])
    for title in titles:
        writer.writerow([title.text])

print("Data scraped successfully and saved to news_headlines.csv")
