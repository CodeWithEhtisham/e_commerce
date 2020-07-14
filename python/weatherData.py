import requests
import datetime
import calendar

class weather:
    url="https://api.openweathermap.org/data/2.5/onecall?lat=1.290270&lon=103.851959&exclude=hourly,minutely&"
    api="appid=c2b5aa85cc6bb0bf577456f468c78b21"
    def __init__(self,url,api,json=None):
        self.url=url
        self.api=api
        self.json=json
    def get_request(self):
        try:
            self.json=requests.get(self.url+self.api)
            return self.json.json()
        except Exception as identifier:
            print("get request",identifier)
        else:
            print("request Error")
    def json_parser(self,json):
        try:
            current={}
            current['city']=json["timezone"]
            current["date"]=datetime.datetime.utcfromtimestamp(int(json["current"]["dt"])).strftime('%d-%B-%Y')
            current["day"]=datetime.datetime.utcfromtimestamp(int(json["current"]["dt"])).strftime('%A')
            current["temp"]=round(json["current"]['temp']-273.15,2)
            current["cloud"]=json["current"]['clouds']
            current["wind"]=json["current"]["wind_speed"]
            daily={}
            for index,value in enumerate( json["daily"][1:7]): 
                daily[index]={
                    "day":datetime.datetime.utcfromtimestamp(int(value["dt"])).strftime('%A'),
                    "temp":round(value["temp"]["max"]-273.15,2),
                    "wind":value["wind_deg"]
                }
            weather={}
            weather["current"]=current
            weather["daily"]=daily
            return weather

        except Exception as identifier:
            print("json parser ",identifier)
if __name__ == "__main__":
    init=weather(weather.url,weather.api)
    init.json_parser(init.get_request())