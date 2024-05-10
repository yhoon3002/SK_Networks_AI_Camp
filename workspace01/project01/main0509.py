from helpers.debug import *

if __name__ == "__main__":
    ###################
    ## 조건문 기본 사용 ##
    ###################
    def basic_conditional_state_1():
        _number = input("정수 입력: ")
        _number = int(_number)

        if _number > 0:
            pp("양수입니다")

        if _number < 0:
            pp("음수입니다")

        if _number == 0:
            pp("0입니다.")

    ###########################
    ## 위 조건문 기본사용 리팩토링 ##
    ###########################
    def basic_conditional_state_2():
        _number = input("정수 입력: ")
        _number = int(_number)

        if _number > 0:
            pp("양수입니다")
        elif _number < 0:
            pp("음수입니다")
        elif _number == 0:
            pp("0입니다.")

    ################
    ## 날짜 출력하기 ##
    ################
    def print_date():
        import datetime as dt

        _now = dt.datetime.now()

        print(
            f"지금은 {_now.year}년 {_now.month}월 {_now.day}일 {_now.hour}시 {_now.minute}분 {_now.second}초 입니다."
        )

    #######################
    ## 날짜 변형해서 출력하기 ##
    #######################
    def print_transformed_date():
        import datetime as dt

        _now = dt.datetime.now()

        _modified = _now.strftime("%y-%m-%d %A %H:%M:%S")

        _translated = _modified.replace("AM", "오전")

        print(_modified)

    ################
    ## 성적 출력하기 ##
    ################
    def print_grade():
        _grade = int(input("성적을 입력하세요 : "))

        if 90 <= _grade <= 100:
            pp("A")
        elif 70 <= _grade < 90:
            pp("B")

    ###########
    ## 리스트 ##
    ###########
    def list():
        _fruits = ["apple", "pear", "banana", "melon", "peach"]
        _fruits[0] = "grape"
        _emoji = ["😄", "😀", "😅", "🥲", "😬"]

        print(_fruits)

    ############
    ## 다중포문 ##
    ############
    def multiple_for():
        _list = [
            ["Hong", 20, "Student"],
            ["Lee", 32, "Professor"],
            ["Kim", 32, "Unemployed"],
            ["Lim", 32, "Student"],
            ["Park", 32, "Professor"],
        ]
        _list[1][2] = "UnEmployed"
        print(_list[1][2])

        _list = ["a", "b", "c"]
        _list.append("d")
        _list.insert(0, "e")
        _list.extend(["f", "g"])
        _list.pop()
        del _list[0]

        print(_list)

    ##############
    ## for문(1) ##
    ##############
    def for_1():
        _list = ["a", "b", "c", "d", "e"]
        for i in range(0, len(_list), 1):
            print(_list[i])

        for i in range(0, 10):
            print(f"{i}번째")

        for i in _list:
            print(i)

    ##############
    ## for문(2) ##
    ##############
    def for_2():
        _list = ["a", "b", "c", "d", "e"]

        for i, j in enumerate(_list):
            print(i)
            print(j)

    ##############
    ## for문(3) ##
    ##############
    def for_3():
        _empty_list = []

        for i in range(1, 1001):
            _empty_list.append(i)

        print(_empty_list)

    ##############
    ## for문(4) ##
    ##############
    def for_4():
        for character in "안녕하세요":
            print("-", character)

    ##################
    ## 이중 for문(1) ##
    ##################
    def double_for_1():
        _lol = [[1, 2, 3], [4, 5, 6, 7], [8, 9]]

        for i in _lol:
            for j in i:
                print(j)

    ##################
    ## 이중 for문(2) ##
    ##################
    def double_for_2():
        for i in range(1, 10):
            print(f"{i}단")
            for j in range(1, 10):
                print(f"{i} * {j} = {i * j}".center(20))

    ########################
    ## List Comprehension ##
    ########################
    def list_comprehension():
        _emptyList = [i for i in range(0, 10) if i >= 5]
        print(_emptyList)

    ####################
    ## Dictionary(1) ##
    ####################
    def dictionary_1():
        _dictionary = {"name": "Hong", "age": 23}
        _age = _dictionary["age"]

        print(_age)

    ####################
    ## Dictionary(2) ##
    ####################
    def dictionary_2():
        _dictionaryInList = [
            {
                "postId": 1,
                "id": 1,
                "name": "id labore ex et quam laborum",
                "email": "Eliseo@gardner.biz",
                "body": "laudantium enim quasi est quidem magnam voluptate ipsam eostempora quo necessitatibusdolor quam autem quasireiciendis et nam sapiente accusantium",
            },
            {
                "postId": 1,
                "id": 2,
                "name": "quo vero reiciendis velit similique earum",
                "email": "Jayne_Kuhic@sydney.com",
                "body": "est natus enim nihil est dolore omnis voluptatem numquamet omnis occaecati quod ullam atvoluptatem error expedita pariaturnihil sint nostrum voluptatem reiciendis et",
            },
        ]

        # 두 번째 사람 이메일 주소 출력
        print(_dictionaryInList[1]["email"])

        # 첫 번째 사람 id를 30으로 변경
        _dictionaryInList[0]["id"] = 30
        print(_dictionaryInList[0]["id"])

        # 변경된 _dictionaryInList 출력
        print(_dictionaryInList)

    ##############################
    ## for문과 딕셔너리 같이 사용하기 ##
    ##############################
    def for_with_dictionary():
        _dictionary = {"name": "Hong", "age": 21}

        for key in _dictionary:
            print(key, _dictionary[key])
            print(_dictionary.get(key))

        for key, value in _dictionary.items():
            print(f"key is {key}, value is {value}")

    ####################################################
    ## numbers 내부에 들어 있는 숫자가 몇 번 등장하는지 출력하기 ##
    ####################################################
    def print_how_many_numbers():
        _numbers = [1, 2, 6, 8, 4, 3, 2, 1, 9, 5, 4, 9, 7, 2, 1, 3, 5, 4, 8, 9, 7, 2, 3]
        _counter = {}

        for number in _numbers:
            _counter[number] = _numbers.count(number)

        print(_counter)

    #####################
    ## 반대로 반복하기(1) ##
    #####################
    def reverse_for():
        for i in range(4, -1, -1):
            print(format(i))
