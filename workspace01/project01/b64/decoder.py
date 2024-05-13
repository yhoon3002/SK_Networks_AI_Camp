import base64


def base64_to_str(x):
    """base64 표현을 문자열로 변환함

    b64decode()의 반환값은 bytes 타입이므로
    decode()로 문자열로 바꾼 뒤 변환함
    """
    return base64.b64decode(x).decode("utf-8")
