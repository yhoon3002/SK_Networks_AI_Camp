PI = 3.141592


def number_input():
    _output = input("숫자 입력> ")
    return float(_output)


def get_circumference(radius):
    return 2 * PI * radius


def get_circle_area(radius):
    return PI * radius * radius
