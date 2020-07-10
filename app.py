from weatherData import weather
from web_scraping import scrape
from flask import Flask,render_template,url_for
app=Flask(__name__)
init=weather(weather.url,weather.api)
obj=scrape(scrape.url1)
# print(len(product) ,"\n\n\n\n")


@app.route('/')
def index():
   print("index func")
   weather=init.json_parser(init.get_request())
   product=obj.json_parser()
   data={"weather":weather,"product":product}
   # print(data["product"])
   return render_template("index.html",data=data)

@app.route('/trend')
def trend():
      print("trend func")
    # show the form, it wasn't submitted
      return render_template('trend.html')
@app.route('/calender')
def calender():
      print("calender func")
    # show the form, it wasn't submitted
      return render_template('calender.html')


if __name__ == "__main__":
    app.run(debug=True)