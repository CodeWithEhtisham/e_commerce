from weatherData import weather
from web_scraping import scrape
from flask import Flask,render_template,url_for
app=Flask(__name__)
init=weather(weather.url,weather.api)
obj=scrape(scrape.url1)
# print(len(product) ,"\n\n\n\n")
# product,trend=None,None
weather=init.json_parser(init.get_request())
# product=obj.json_parser()
@app.route('/')
def index():
   print("index func")
   product=obj.json_parser("home")
   data={"weather":weather,"product":product}
   # print(data["product"])
   return render_template("index.html",data=data)

@app.route('/wine')
def wine():
      print("wine func")
      wine_Data=obj.json_parser("wine")
    # show the form, it wasn't submitted
      print(wine_Data)
      data={"wine":wine_Data}
      return render_template('wine.html',data=data)



@app.route('/bakery')
def bakery():
      wine_Data=obj.json_parser("bakery")
    # show the form, it wasn't submitted
      print(wine_Data)
      data={"wine":wine_Data}
      # return render_template('wine.html',data=data)
      return render_template('bakery.html',data=data)
@app.route('/calender')
def calender():
      print("calender func")
    # show the form, it wasn't submitted
      return render_template('calender.html')



@app.route('/beverages')
def beverages():
      wine_Data=obj.json_parser("beverages")
    # show the form, it wasn't submitted
      print(wine_Data)
      data={"wine":wine_Data}
      return render_template('beverages.html',data=data)

@app.route('/dairy')
def dairy():
      wine_Data=obj.json_parser("dairy")
    # show the form, it wasn't submitted
      print(wine_Data)
      data={"wine":wine_Data}
      return render_template('dairy.html',data=data)

@app.route('/frozen')
def frozen():
      wine_Data=obj.json_parser("frozen")
    # show the form, it wasn't submitted
      print(wine_Data)
      data={"wine":wine_Data}
      return render_template('frozen.html',data=data)

@app.route('/fruit')
def fruit():
      wine_Data=obj.json_parser("fruit")
    # show the form, it wasn't submitted
      print(wine_Data)
      data={"wine":wine_Data}
      return render_template('fruit.html',data=data)

@app.route('/health')
def health():
      wine_Data=obj.json_parser("health")
    # show the form, it wasn't submitted
      print(wine_Data)
      data={"wine":wine_Data}
      return render_template('health.html',data=data)

@app.route('/household')
def household():
      wine_Data=obj.json_parser("household")
    # show the form, it wasn't submitted
      print(wine_Data)
      data={"wine":wine_Data}
      return render_template('household.html',data=data)

@app.route('/meat')
def meat():
      wine_Data=obj.json_parser("meat")
    # show the form, it wasn't submitted
      print(wine_Data)
      data={"wine":wine_Data}
      return render_template('meat.html',data=data)

@app.route('/mother')
def mother():
      wine_Data=obj.json_parser("mother")
    # show the form, it wasn't submitted
      print(wine_Data)
      data={"wine":wine_Data}
      return render_template('mother.html',data=data)


@app.route('/new')
def new():
      wine_Data=obj.json_parser("new")
    # show the form, it wasn't submitted
      print(wine_Data)
      data={"wine":wine_Data}
      return render_template('new.html',data=data)

@app.route('/rice')
def rice():
      wine_Data=obj.json_parser("rice")
    # show the form, it wasn't submitted
      print(wine_Data)
      data={"wine":wine_Data}
      return render_template('rice.html',data=data)

@app.route('/party')
def party():
      wine_Data=obj.json_parser("party")
    # show the form, it wasn't submitted
      print(wine_Data)
      data={"wine":wine_Data}
      return render_template('party.html',data=data)

@app.route('/snacks')
def snacks():
      wine_Data=obj.json_parser("snacks")
    # show the form, it wasn't submitted
      print(wine_Data)
      data={"wine":wine_Data}
      return render_template('snacks.html',data=data)



if __name__ == "__main__":
    app.run(debug=True)