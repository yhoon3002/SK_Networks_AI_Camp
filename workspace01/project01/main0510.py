from helpers.debug import *
from helpers.mathf import *

if __name__ == "__main__":
    ############################
    ## 반복문으로 피라미드 만들기(1) ##
    ############################
    def pyramid_1():
        _pyramid = ""

        for i in range(1, 10):
            for j in range(0, i):
                _pyramid += "*"
            if i != 9:
                _pyramid += "\n"

        print(_pyramid)

    #############################
    ## 반복문으로 피라미드 만들기(2) ##
    #############################
    def pyramid_2():
        _pyramid = ""

        for i in range(1, 15):
            for j in range(14, i, -1):
                _pyramid += " "
            for k in range(0, 2 * i - 1):
                _pyramid += "*"
            _pyramid += "\n"

        print(_pyramid)

    #######################
    ## while로 누적합 구하기 ##
    #######################
    def cumulative_sum():
        _sum = 0
        while True:
            _sum += 1
            if _sum == 15:
                break

        print(_sum)

    #########################
    ## 해당하는 값 모두 제거하기 ##
    #########################
    def remove_value():
        _list_test = [1, 2, 1, 2]
        _value = 2

        while _value in _list_test:
            _list_test.remove(_value)

        print(_list_test)

    #########################
    ## 시간을 기반으로 반복하기 ##
    #########################
    def while_with_time():
        import time

        _number = 0

        _targetTick = time.time() + 5
        while time.time() < _targetTick:
            _number += 1

        print(_number)

    #################################
    ## while문으로 1부터 100까지 더하기 ##
    #################################
    def sum_1_to_100():
        _sequence = list(range(1, 101))
        _sum = 0
        _temp = 0

        while True:
            _temp += 1
            _sum += _sequence[_temp]

            if _temp == 100:
                break

        print(_sum)

    #########################################
    ## continue문으로 수열 값중에 홀수만 다 더하기 ##
    #########################################
    def sum_odd():
        _sequence = list(range(1, 101))
        _sum = 0
        _temp = 0

        while True:
            _temp += 1
            if _sequence[_temp - 1] % 2 == 0:
                continue

            _sum += _sequence[_temp - 1]

            if _temp == 99:
                break

        print(_sum)

    #######################################
    ## 각 리스트를 조합해 하나의 딕셔너리를 만들기 ##
    #######################################
    def make_dictionary():
        _keyList = ["name", "hp", "mp", "level"]
        _valueList = ["기사", 200, 30, 5]
        _character = {}

        for i in range(len(_keyList)):
            _character[_keyList[i]] = _valueList[i]

        print(_character)

    ##########################################################
    ## 1부터 100까지의 숫자 중 어떤 숫자를 곱했을 때 최대가 되는지 찾기1 ##
    ##########################################################
    def find_max_1():
        _maxValue = 0
        _a = 0
        _b = 0

        for i in range(1, 101):
            j = 100 - i

            if _maxValue < i * j:
                _maxValue = i * j
                _a = i
                _b = j

        print("최대가 되는경우: {} * {} = {}".format(_a, _b, _maxValue))

    ##############################
    ## enumberate() 함수와 리스트 ##
    ##############################
    def enumerate_function_and_list():
        _list = ["Element A", "Element B", "Element C"]

        print(list(enumerate(_list)))

        for i, val in enumerate(_list):
            print("{}번째 Element는 {}입니다".format(i, val))

    ###########################
    ## 리스트 안에 for문 사용하기 ##
    ###########################
    def for_in_list():
        _array = [i * i for i in range(0, 20, 2)]

        print(_array)

    #############################
    ## reversed()함수와 이터레이터 ##
    #############################
    def reversed_and_iterator():
        _numbers = [1, 2, 3, 4, 5, 6]
        _rNum = reversed(_numbers)

        print(_rNum)
        print(next(_rNum))
        print(next(_rNum))
        print(next(_rNum))
        print(next(_rNum))
        print(next(_rNum))
        print(next(_rNum))

    ##################
    ## 매개변수의 기본 ##
    ##################
    def print_n_times(val, n):
        for i in range(n):
            print(val)

    ####################
    ## 가변 매개변수 함수 ##
    ####################
    def print_n_times2(n, *val):
        for i in range(n):
            for v in val:
                print(v)

    ########################################################
    ## 기본 매개변수와 키워드 매개변수를 활용해 범위의 정수를 더하는 함수 ##
    ########################################################
    def sum_all(start=0, end=100, step=1) -> int:
        _output = 0

        for i in range(start, end + 1, step):
            _output += i

        return _output

    ###################
    ## 리스트 평탄화하기 ##
    ###################
    _example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]

    def flatten(data):
        _output = []
        for item in data:
            if type(item) == list:
                _output += item
            else:
                _output.append(item)
        return _output

    ################################
    ## lambda와 filter 같이 사용하기 ##
    ################################
    def lambda_with_filter():
        _list = 1, 2, 3, 4, 5
        print(list(filter(lambda x: x > 2, _list)))

    ##############
    ## 파일 열기1 ##
    ##############
    def file_io():
        _filePath = "/Users/lim_younghoon/Desktop/SK_Networks_AI/workspace01/project01/2024-05-08.txt"

        _openedFile = open(_filePath, encoding="utf-8")
        _contents = _openedFile.read()
        _contents2 = _openedFile.readline()

        print(_contents)

    ##############
    ## 파일 열기2 ##
    ##############
    def file_io2():
        _filePath = "/Users/lim_younghoon/Desktop/SK_Networks_AI/workspace01/project01/2024-05-08.txt"

        with open(_filePath, encoding="utf-8", mode="a") as file:
            file.write("추가됨추가됨추가됨추가됨추가됨추가됨추가됨추가됨")

    ###################################
    ## 랜덤하게 1000명의 키와 몸무게 만들기 ##
    ###################################
    def make_random_height_weight():
        import random as rd

        _korean = list("가나다라마바사아자차카타파하")

        with open("info.txt", "w") as file:
            for i in range(5):
                _name = rd.choice(_korean) + rd.choice(_korean)
                _weight = rd.randrange(40, 100)
                _height = rd.randrange(140, 200)

                file.write("{}, {}, {}\n".format(_name, _height, _weight))

    ############################
    ## 반복문으로 파일 한 줄씩 읽기 ##
    ############################
    def make_random_bmi():
        with open("info.txt", "r") as file:
            for line in file:
                (_name, _weight, _height) = line.strip().split(", ")

                if (not _name) or (not _weight) or (not _height):
                    continue

                _bmi = int(_weight) / ((int(_height) / 100) ** 2)
                _result = ""
                if 25 <= _bmi:
                    _result = "과체중"
                elif 18.5 <= _bmi:
                    _result = "정상 체중"
                else:
                    _result = "저체중"

                print(
                    "\n".join(
                        [
                            "이름: {}",
                            "몸무게: {}",
                            "키: {}",
                            "bmi: {}",
                            "결과: {}",
                        ]
                    ).format(_name, _weight, _height, _bmi, _result)
                )
                print()

    ##################
    ## 제너레이터 함수 ##
    ##################
    def test():
        print("호출되었습니다.")
        yield "test"

    ##########################
    ## 딕셔너리 오름차순 정렬하기 ##
    ##########################
    def sort_dictionary():
        _dictionaryInList = [
            {"price": 1000},
            {"price": 5000},
            {"price": 3000},
        ]

        _dictionaryInList.sort(
            key=lambda _dictionaryInList: _dictionaryInList["price"], reverse=False
        )

        for list in _dictionaryInList:
            print(list)
