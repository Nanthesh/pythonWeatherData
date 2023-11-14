from flask import Flask, render_template, request
import requests

api='a100ec5bbbf4342bd17fc58b72c801ab'
app = Flask(__name__)

@app.route('/')
def homePage():
    return render_template("index.html")
@app.route('/weatherapp', method=["POST"])
def weather_data():
    url1='https://api.openweathermap.org/data/2.5/weather'

    param={
        'q':request.form.get("cityName"),
        'units':request.form.get("units"),
        'appid':request.form.get('apiid')
    }
    res=requests.get(url1,params=param)
    data=res.json()
    return f"Data: {data}"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004)
