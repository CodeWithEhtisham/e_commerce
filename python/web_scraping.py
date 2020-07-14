import requests
import urllib
import urllib3
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup
import re
import numpy as np
import json
from operator import itemgetter
import random
from pathlib import Path

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
    def json_parser(self,name):
        base_path = Path(__file__).parent
        file_path = (base_path / "../data/label.json").resolve()
        with open(file_path) as f:
            data = json.load(f)
            recommendation=random.sample(range(0, 800), 100)
            my_data={}
            # trend_data={}
            if name!="home":
                data=data[str(name)]['data']
                for index,value in enumerate(data):
                    my_data[index]=[value['itemTitle'],
                    value["itemImg"],value["itemPackageSize"],value["itemPrice"]+"$",str(value['itemReviews'])]
            else:
                    
                data=data[str(name)]['data']
                for index,value in enumerate(data):
                    if index in recommendation:
                        my_data[index]=[value['itemTitle'],
                        value["itemImg"],value["itemPackageSize"],value["itemPrice"]+"$",str(value['itemReviews'])]
            
            # print(len(trend_data))
            print(len(my_data))

            
            return my_data




if __name__ == "__main__":
    obj=scrape(scrape.url1)
    obj.scrape_1()
    obj.json_parser("bakery")