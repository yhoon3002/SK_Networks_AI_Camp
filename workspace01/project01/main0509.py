from helpers.debug import *

if __name__ == "__main__":
    ####################
    ## 조건문 기본 사용
    # number = input("정수 입력: ")
    # number = int(number)

    # if number > 0:
    #     pp("양수입니다")

    # if number < 0:
    #     pp("음수입니다")

    # if number == 0:
    #     pp("0입니다.")

    ####################
    ## 위 조건문 기본사용 리팩토링
    # number = input("정수 입력: ")
    # number = int(number)

    # if number > 0:
    #     pp("양수입니다")
    # elif number < 0:
    #     pp("음수입니다")
    # elif number == 0:
    #     pp("0입니다.")

    ####################
    ## 날짜 출력하기
    # import datetime as dt

    # now = dt.datetime.now()

    # print(
    #     f"지금은 {now.year}년 {now.month}월 {now.day}일 {now.hour}시 {now.minute}분 {now.second}초 입니다."
    # )

    ####################
    ## 날짜 변형해서 출력하기
    # import datetime as dt

    # now = dt.datetime.now()

    # modified = now.strftime("%y-%m-%d %A %H:%M:%S")

    # translated = modified.replace("AM", "오전")

    # print(modified)

    ####################
    ## 성적 출력하기
    # grade = int(input("성적을 입력하세요 : "))

    # if 90 <= grade <= 100:
    #     pp("A")
    # elif 70 <= grade < 90:
    #     pp("B")

    ####################
    ## 리스트
    # fruits = ["apple", "pear", "banana", "melon", "peach"]
    # fruits[0] = "grape"
    # emoji = ["😄", "😀", "😅", "🥲", "😬"]

    # print(fruits)

    ####################
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

    ####################
    ## for문(1)
    # list = ["a", "b", "c", "d", "e"]
    # for i in range(0, len(list), 1):
    #     print(list[i])

    # for i in range(0, 10):
    #     print(f"{i}번째")

    # for i in list:
    #     print(i)

    ####################
    ## for문(2)
    # list = ["a", "b", "c", "d", "e"]

    # for i, j in enumerate(list):
    #     # print(i)
    #     print(j)

    ####################
    ## for문(3)
    # empty_list = []

    # for i in range(1, 1001):
    #     empty_list.append(i)

    # print(empty_list)

    ####################
    ## for문(4)
    # for character in "안녕하세요":
    #     print("-", character)

    ####################
    ## 이중 for문(1)
    # lol = [[1, 2, 3], [4, 5, 6, 7], [8, 9]]

    # for i in lol:
    #     for j in i:
    #         print(j)

    ####################
    ## 이중 for문(2)
    # for i in range(1, 10):
    #     print(f"{i}단")
    #     for j in range(1, 10):
    #         print(f"{i} * {j} = {i * j}".center(20))

    ####################
    ## List Comprehension
    # empty_list = [i for i in range(0, 10) if i >= 5]
    # print(empty_list)

    ####################
    ## Dictionary(1)
    # dictionary = {"name": "Hong", "age": 23}
    # age = dictionary["age"]

    # print(age)

    ####################
    ## Dictionary(2)
    # dictionary_in_list = [
    #     {
    #         "postId": 1,
    #         "id": 1,
    #         "name": "id labore ex et quam laborum",
    #         "email": "Eliseo@gardner.biz",
    #         "body": "laudantium enim quasi est quidem magnam voluptate ipsam eostempora quo necessitatibusdolor quam autem quasireiciendis et nam sapiente accusantium",
    #     },
    #     {
    #         "postId": 1,
    #         "id": 2,
    #         "name": "quo vero reiciendis velit similique earum",
    #         "email": "Jayne_Kuhic@sydney.com",
    #         "body": "est natus enim nihil est dolore omnis voluptatem numquamet omnis occaecati quod ullam atvoluptatem error expedita pariaturnihil sint nostrum voluptatem reiciendis et",
    #     },
    # ]

    # # 두 번째 사람 이메일 주소 출력
    # print(dictionary_in_list[1]["email"])

    # # 첫 번째 사람 id를 30으로 변경
    # dictionary_in_list[0]["id"] = 30
    # print(dictionary_in_list[0]["id"])

    # # 변경된 dictionary_in_list 출력
    # print(dictionary_in_list)

    ####################
    ## for문과 딕셔너리 같이 사용하기
    # dictionary = {"name": "Hong", "age": 21}

    # for key in dictionary:
    #     print(key, dictionary[key])
    #     print(dictionary.get(key))

    # for key, value in dictionary.items():
    #     print(f"key is {key}, value is {value}")

    ####################
    ## numbers 내부에 들어 있는 숫자가 몇 번 등장하는지 출력하기
    # numbers = [1, 2, 6, 8, 4, 3, 2, 1, 9, 5, 4, 9, 7, 2, 1, 3, 5, 4, 8, 9, 7, 2, 3]
    # counter = {}

    # for number in numbers:
    #     counter[number] = numbers.count(number)

    # print(counter)

    ####################
    ## 반대로 반복하기(1)
    # for i in range(4, -1, -1):
    #     print(format(i))

    ####################
    ## 중첩 반복문으로 피라미드 만들기
    # star = ""

    # for i in range(1, 10):
    #     for j in range(0, i):
    #         star += "*"
    #     star += "\n"

    # print(star)