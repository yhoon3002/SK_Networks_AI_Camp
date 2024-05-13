if __name__ == "__main__":

    def except01():
        try:
            _numberInputA = int(input("정수 입력> "))

            print("원의 반지름:", _numberInputA)
            print("원의 둘레:", 2 * 3.14 * _numberInputA)
            print("원의 넓이:", 3.14 * _numberInputA * _numberInputA)

        except Exception as exception:
            print("type(exception):", type(exception))
            print("exception:", exception)

    def except02():
        _listNumber = [52, 273, 32, 72, 100]

        try:
            _numberInput = int(input("정수 입력> "))

            print("{}번째 요소: {}".format(_numberInput, _listNumber[_numberInput]))

        except ValueError:
            print("정수를 입력해주세요")

        except IndexError:
            print("리스트의 인덱스를 벗어났습니다")

    def raise_exception():
        _number = input("정수 입력> ")
        _number = int(_number)

        if _number > 0:
            raise NotImplementedError
        else:
            ...

    def math_module():
        import math

        print(math.sin(1))
        print(math.cos(1))
        print(math.tan(1))

    def random_module():
        import random

        print(random.random())
        print(random.uniform(10, 20))
        print(random.randrange(10))
        print(random.choice([1, 2, 3, 4, 5]))
        print(random.shuffle([1, 2, 3, 4, 5]))
        print(random.sample([1, 2, 3, 4, 5], k=2))

    def sys_module():
        import sys

        print(sys.argv)
        print(sys.copyright)
        print(sys.version_info)
        print(sys.version)

        sys.exit()

    def os_module():
        import os

        print(os.name)
        print(os.getcwd())
        print(os.listdir())

    def time_module():
        import time

        time.sleep(5)
        print("==============")

    def urllib_module():
        from urllib import request

        target = request.urlopen("https://google.com")
        output = target.read()

        print(output)

    urllib_module()
