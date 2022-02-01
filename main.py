from bs4 import BeautifulSoup
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.get("/api/v1/current/")
async def parse_current():
    req = requests.get(url="https://bet.szerencsejatek.hu/jatekok/otoslotto", headers={"User-Agent": "Lozilla/5.0 (Doors NT 11.0; Win69; x69; rv:90.0) Python/20220101 Lottofox/90.0"})
    soup = BeautifulSoup(req.text.encode("utf-8"), "html.parser")

    current = soup.find("section", {"class": "top-banner-container top-banner-lotto5"})
    response = jsonify( 
        {   
            "drawDate": current.find("div", {"class": "draw-date"}).getText().strip(),
            "week": current.find("div", {"class": "week"}).find("span").getText().strip(),
            "expectedPrice": current.find("div", {"class": "expected-price"}).find("h3").getText()
        }
    )
    
    # https://dev.to/matheusguimaraes/fast-way-to-enable-cors-in-flask-servers-42p0
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == "__main__":
    app.run()