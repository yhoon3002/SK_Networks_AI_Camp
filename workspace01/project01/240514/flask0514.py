from flask import Flask

_app = Flask(__name__)


## Java - @어노테이션
# 생략도 가능, 컴파일러(명시적) 알려줘
## Python - @데코레이터
# 미리 만들어둔 데코레이터 / 내가 만들어쓰는 데코레이터 / 함수를 감싸줘서 기능을 추가해준다 / 함수를 변경하는 거


# 공유기 라우터 경로처리
@_app.route("/")  # 루트경로
def hello():
    return """
    <p style="margin-top: 20px;">
        <h1 style="width: 100%; text-align: center; border-bottom: 3px solid #000;">Flask</h1>
        <h3 style="font-weight: bold; color: blue">My Flask</h3>
    </p>
    """
