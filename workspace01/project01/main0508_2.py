from helpers.debug import *


###############
## 입출력시스템 ##
###############
def input_output():
    _name = input("Input your name ! \n")
    _age = input("Input your age ! \n")

    getType(_name)
    print(f"Your name is {_name}")

    _temp_age = int(_age)
    getType(_age)
    getType(_temp_age)
    print(f"Your age is {_age}")


#############
## 타입 변환 ##
#############
def transform_type():
    a = 3.14
    b = 3

    pp(int(a))  # 3
    pp(float(b))  # 3.0
    getType(str(1))  # str

    ppt(a + b)
    ppt(3.0 + 3.14)
    ppt(int(a + b))
    ppt(int(3.0 + 3.14))

    inch_cm = inch_to_cm(13.3)
    cm_inch = cm_to_inch(10)

    pp(inch_cm)
    pp(cm_inch)

    cal_circle()

    list = [12, 13, 14]

    print("{}ab{}cd{}".format(*list))

    print("ABCD".lower())

    index = "무궁화 꽃꽃이 피었습니다".rfind("꽃")
    pp(index)

    file_path = "/Users/lim_younghoon/Desktop/workspace01/project01/main.py"
    print(file_path.split("/")[4])


# cal_sphere()
# cal_sphere2()
# pythagoras()
# pythagoras2()
