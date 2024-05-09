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
    grade = int(input("성적을 입력하세요 : "))

    if 90 <= grade <= 100:
        pp("A")
    elif 70 <= grade < 90:
        pp("B")
