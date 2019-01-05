#This program will get GE stock price
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://stocktwits.com/symbol/GE")
res = BeautifulSoup(html.read(), 'html.parser')
span_box = res.find("span", attrs={"class" : "StockHeader__bid___2BF7L"})
span = span_box.text
print("GE stock price is " + span)
