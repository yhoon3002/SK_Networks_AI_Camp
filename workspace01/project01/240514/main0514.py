if __name__ == "__main__":

    def beautiful_weather():
        from urllib import request
        from bs4 import BeautifulSoup

        # urlopen() 함수로 기상청의 전국 날씨를 읽는다.
        _target = request.urlopen(
            "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
        )

        # BeautifulSoup를 사용해 웹 페이지를 분석한다.
        _soup = BeautifulSoup(_target, "html.parser")

        # print(type(_soup))
        # print(dir(_soup))

        # location 태그를 찾는다.
        for location in _soup.select("location"):
            # 내부의 city, wf, tmn, tmx 태그를 찾아 출력한다.
            print("도시:", location.select_one("city").string)
            print("날씨:", location.select_one("wf").string)
            print("최저기온:", location.select_one("tmn").string)
            print("최고기온:", location.select_one("tmx").string)
            print()

    beautiful_weather()
