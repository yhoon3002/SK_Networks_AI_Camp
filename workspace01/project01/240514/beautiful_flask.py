from flask import Flask
from urllib import request
from bs4 import BeautifulSoup

# 웹 서버 생성
_app = Flask(__name__)


@_app.route("/")
def hello():
    # urlopen()으로 기상청의 전국 날씨를 읽는다.
    target = request.urlopen(
        "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
    )

    # BeautifulSoup를 사용해 웹 페이지를 분석한다.
    _soup = BeautifulSoup(target, "html.parser")

    # location 태그를 찾는다.
    _output = ""
    for location in _soup.select("location"):
        _output += "<h3>{}</h3>".format(location.select_one("city").string)
        _output += "날씨: {}<br/>".format(location.select_one("wf").string)
        _output += "최저/최고 기온: {} / {}".format(
            location.select_one("tmn").string, location.select_one("tmx").string
        )
        _output += "<hr/>"

    return _output
