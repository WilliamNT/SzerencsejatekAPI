from distutils.log import debug
from bs4 import BeautifulSoup
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.get("/api/v1/current/otoslotto/")
async def otoslotto():
    req = requests.get(url="https://bet.szerencsejatek.hu/jatekok/otoslotto", headers={"User-Agent": "Lozilla/5.0 (Doors NT 11.0; Win69; x69; rv:90.0) Python/20220101 Lottofox/90.0"})
    soup = BeautifulSoup(req.text.encode("utf-8"), "html.parser")

    current = soup.find("section", {"class": "top-banner-container top-banner-lotto5"})
    response = jsonify( 
        {   
            "drawDate": current.find("div", {"class": "draw-date"}).getText().strip(),
            "week": current.find("div", {"class": "week"}).find("span").getText().strip(),
            "expectedPrice": current.find("div", {"class": "expected-price"}).find("h3").getText(),
            "logoImage": "https://bet.szerencsejatek.hu/assets/a5e3dce5/e99c1120/img/top-banner/lotto5.png"
        }
    )
    
    # https://dev.to/matheusguimaraes/fast-way-to-enable-cors-in-flask-servers-42p0
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.get("/api/v1/current/hatoslotto/")
async def hatoslotto():
    req = requests.get(url="https://bet.szerencsejatek.hu/jatekok/hatoslotto", headers={"User-Agent": "Lozilla/5.0 (Doors NT 11.0; Win69; x69; rv:90.0) Python/20220101 Lottofox/90.0"})
    soup = BeautifulSoup(req.text.encode("utf-8"), "html.parser")

    current = soup.find("section", {"class": "top-banner-container top-banner-lotto6"})
    response = jsonify( 
        {   
            "drawDate": current.find("div", {"class": "draw-date"}).getText().strip(),
            "week": current.find("div", {"class": "week"}).find("span").getText().strip(),
            "expectedPrice": current.find("div", {"class": "expected-price"}).find("h3").getText(),
            "logoImage": "https://bet.szerencsejatek.hu/assets/a5e3dce5/e99c1120/img/top-banner/lotto6.png"
        }
    )
    
    # https://dev.to/matheusguimaraes/fast-way-to-enable-cors-in-flask-servers-42p0
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.get("/api/v1/current/skandinavlotto/")
async def skandinavlotto():
    req = requests.get(url="https://bet.szerencsejatek.hu/jatekok/skandinavlotto", headers={"User-Agent": "Lozilla/5.0 (Doors NT 11.0; Win69; x69; rv:90.0) Python/20220101 Lottofox/90.0"})
    soup = BeautifulSoup(req.text.encode("utf-8"), "html.parser")

    current = soup.find("section", {"class": "top-banner-container top-banner-lotto7"})
    response = jsonify( 
        {   
            "drawDate": current.find("div", {"class": "draw-date"}).getText().strip(),
            "week": current.find("div", {"class": "week"}).find("span").getText().strip(),
            "expectedPrice": current.find("div", {"class": "expected-price"}).find("h3").getText(),
            "logoImage": "https://bet.szerencsejatek.hu/assets/a5e3dce5/e99c1120/img/top-banner/lotto7.png"
        }
    )
    
    # https://dev.to/matheusguimaraes/fast-way-to-enable-cors-in-flask-servers-42p0
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.get("/api/v1/current/eurojackpot/")
async def eurojackpot():
    req = requests.get(url="https://bet.szerencsejatek.hu/jatekok/eurojackpot", headers={"User-Agent": "Lozilla/5.0 (Doors NT 11.0; Win69; x69; rv:90.0) Python/20220101 Lottofox/90.0"})
    soup = BeautifulSoup(req.text.encode("utf-8"), "html.parser")

    current = soup.find("section", {"class": "top-banner-container top-banner-eurojackpot"})
    response = jsonify( 
        {   
            "betDeadline": current.find("div", {"class": "draw-date"}).find("h3").getText(),
            "week": current.find("div", {"class": "week"}).find("span").getText().strip(),
            "expectedPrice": current.find("div", {"class": "expected-price"}).find("h3").getText(),
            "grossPrice": current.find("div", {"class": "expected-price"}).find("span", {"class": "price-gross"}).getText().strip(),
            "logoImage": "https://bet.szerencsejatek.hu/assets/a5e3dce5/e99c1120/img/top-banner/eurojackpot.png"
        }
    )
    
    # https://dev.to/matheusguimaraes/fast-way-to-enable-cors-in-flask-servers-42p0
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.get("/api/v1/current/luxor/")
async def luxor():
    req = requests.get(url="https://bet.szerencsejatek.hu/jatekok/luxor", headers={"User-Agent": "Lozilla/5.0 (Doors NT 11.0; Win69; x69; rv:90.0) Python/20220101 Lottofox/90.0"})
    soup = BeautifulSoup(req.text.encode("utf-8"), "html.parser")

    current = soup.find("section", {"class": "top-banner-container top-banner-luxor"})
    response = jsonify( 
        {   
            "drawDate": current.find("div", {"class": "draw-date"}).getText().strip(),
            "week": current.find("div", {"class": "week"}).find("span").getText().strip(),
            "expectedPrice": current.find("div", {"class": "expected-price"}).find("h3").getText(),
            "logoImage": "https://bet.szerencsejatek.hu/assets/a5e3dce5/e99c1120/img/top-banner/luxor.png"
        }
    )
    
    # https://dev.to/matheusguimaraes/fast-way-to-enable-cors-in-flask-servers-42p0
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.get("/api/v1/current/joker/")
async def joker():
    req = requests.get(url="https://bet.szerencsejatek.hu/jatekok/joker", headers={"User-Agent": "Lozilla/5.0 (Doors NT 11.0; Win69; x69; rv:90.0) Python/20220101 Lottofox/90.0"})
    soup = BeautifulSoup(req.text.encode("utf-8"), "html.parser")

    current = soup.find("section", {"class": "top-banner-container top-banner-joker"})
    response = jsonify( 
        {   
            "drawDate": current.find("div", {"class": "draw-date"}).getText().strip(),
            "week": current.find("div", {"class": "week"}).find("span").getText().strip(),
            "expectedPrice": current.find("div", {"class": "expected-price"}).find("h3").getText(),
            "logoImage": "https://bet.szerencsejatek.hu/assets/a5e3dce5/e99c1120/img/top-banner/joker.png"
        }
    )
    
    # https://dev.to/matheusguimaraes/fast-way-to-enable-cors-in-flask-servers-42p0
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == "__main__":
    app.run()
