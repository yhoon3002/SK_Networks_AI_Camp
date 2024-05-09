from helpers.debug import *

if __name__ == "__main__":
    ##
    ## 조건문 기본 사용
    # number = input("정수 입력: ")
    # number = int(number)

    # if number > 0:
    #     pp("양수입니다")

    # if number < 0:
    #     pp("음수입니다")

    # if number == 0:
    #     pp("0입니다.")

    ##
    ## 위 조건문 기본사용 리팩토링
    # number = input("정수 입력: ")
    # number = int(number)

    # if number > 0:
    #     pp("양수입니다")
    # elif number < 0:
    #     pp("음수입니다")
    # elif number == 0:
    #     pp("0입니다.")

    ##
    ## 날짜 출력하기
    # import datetime as dt

    # now = dt.datetime.now()

    # print(
    #     f"지금은 {now.year}년 {now.month}월 {now.day}일 {now.hour}시 {now.minute}분 {now.second}초 입니다."
    # )

    ##
    ## 날짜 변형해서 출력하기
    # import datetime as dt

    # now = dt.datetime.now()

    # modified = now.strftime("%y-%m-%d %A %H:%M:%S")

    # translated = modified.replace("AM", "오전")

    # print(modified)

    ##
    ## 성적 출력하기
    # grade = int(input("성적을 입력하세요 : "))

    # if 90 <= grade <= 100:
    #     pp("A")
    # elif 70 <= grade < 90:
    #     pp("B")

    ##
    ## 리스트
    # fruits = ["apple", "pear", "banana", "melon", "peach"]
    # fruits[0] = "grape"
    # emoji = ["😄", "😀", "😅", "🥲", "😬"]

    # print(fruits)

    ##
    ## 다중포문
    # list = [
    #     ["Hong", 20, "Student"],
    #     ["Lee", 32, "Professor"],
    #     ["Kim", 32, "Unemployed"],
    #     ["Lim", 32, "Student"],
    #     ["Park", 32, "Professor"],
    # ]
    # list[1][2] = "UnEmployed"
    # print(list[1][2])

    # list = ["a", "b", "c"]
    # list.append("d")
    # list.insert(0, "e")
    # list.extend(["f", "g"])
    # list.pop()
    # del list[0]

    # print(list)

    ##
    ## for문(1)
    # list = ["a", "b", "c", "d", "e"]
    # for i in range(0, len(list), 1):
    #     print(list[i])

    # for i in range(0, 10):
    #     print(f"{i}번째")

    # for i in list:
    #     print(i)

    ##
    ## for문(2)
    # list = ["a", "b", "c", "d", "e"]

    # for i, j in enumerate(list):
    #     # print(i)
    #     print(j)

    ##
    ## for문(3)
    # empty_list = []

    # for i in range(1, 1001):
    #     empty_list.append(i)

    # print(empty_list)

    ##
    ## for문(4)
    # for character in "안녕하세요":
    #     print("-", character)

    ##
    ## 이중 for문(1)
    # lol = [[1, 2, 3], [4, 5, 6, 7], [8, 9]]

    # for i in lol:
    #     for j in i:
    #         print(j)

    ##
    ## 이중 for문(2)
    for i in range(1, 10):
        print(f"{i}단")
        for j in range(1, 10):
            print(f"{i} * {j} = {i * j}".center(20))
