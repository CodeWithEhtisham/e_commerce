import requests
import urllib
import urllib3
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup
import re
import json

class scrape:
    url1="https://www.fairprice.com.sg/product-listing?hasStock=1&loadMoreType=SEEALL&sorting=POPULARITY&tag=best-sellers&title=Best%20Sellers&loc=ProductWidget-BestSellers&pageType=Home"
    def __init__(self,url):
        self.url=url
    def scrape_1(self):
        try:
            res=Request(self.url,headers={'User-Agent': 'Mozilla/5.0'})
            request=urlopen(res).read()
            html=BeautifulSoup(request,"html.parser")
            print(type(html))
            product_container=html.find_all('div', class_ ='sc-1plwklf-4 nUisu')
            print(len(product_container))
            pass
        except Exception as e:
            print("request ",e)
            # pass
    def json_parser(self):
        with open('data.json') as f:
            data = json.load(f)
            my_data={}
            data=data["individualSalesProductGrid"]['data']
            for index,value in enumerate(data):
                my_data[index]=[value['itemTitle'],
                value["itemImg"],value["itemPackageSize"],value["itemPrice"]+"$",value['itemReviews']]
            return my_data




if __name__ == "__main__":
    obj=scrape(scrape.url1)
    print(obj.scrape_1())
    print(obj.json_parser())