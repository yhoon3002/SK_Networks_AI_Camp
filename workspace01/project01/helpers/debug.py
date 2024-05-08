# 사용자 함수
import math as Math


def pp(a):
    print(a)


def ppt(a):
    print("타입은 ", type(a))
    print("값은", a)


def getType(a):
    print("==>", type(a))


def getLen(a):
    print("==>", len(a))


def inch_to_cm(raw_data):
    inch = float(raw_data)
    cm = inch * 2.54

    return cm


def cm_to_inch(raw_data):
    inch = float(raw_data) / 2.54
    return inch


def cal_circle():
    str_input = input("원의 반지름을 입력하세요: ")
    num_input = float(str_input)
    print(f"반지름: {num_input}")
    print(f"둘레: {2 * 3.14 * num_input}")
    print(f"넓이: {3.14 * (num_input ** 2)}")


pi = 3.141592


def cal_sphere():
    a = float(input("구의 반지름을 입력해주세요: "))
    print(f"구의 부피는 { 4 / 3 * pi * a ** 3}")
    print(f"구의 겉넓이는 {a ** 2 * 4 * pi}")


def cal_sphere2():
    a = float(input("구의 반지름을 입력해주세요: "))
    print(f"구의 부피는 { 4 / 3 * pi * Math.pow(a, 3)}")
    print(f"구의 겉넓이는 {Math.pow(a, 2) * 4 * pi}")


def pythagoras():
    a = float(input("밑변의 길이를 입력해주세요: "))
    b = float(input("높이의 길이를 입력해주세요: "))

    print(f"빗변의 길이는 {(a ** 2  + b ** 2)**(1/2)}")


def pythagoras2():
    a = float(input("밑변의 길이를 입력해주세요: "))
    b = float(input("높이의 길이를 입력해주세요: "))

    print(f"빗변의 길이는 {Math.sqrt(a ** 2  + b ** 2)}")
