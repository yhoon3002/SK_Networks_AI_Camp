#############
## 팩토리얼1 ##
#############
def make_factorial_1(num):
    _result = 1

    for i in range(1, num + 1):
        _result *= i

    return _result


#############
## 팩토리얼2 ##
#############
def make_factorial_2(num):
    if num == 0:
        return 1
    else:
        return num * make_factorial_2(num - 1)


#################
## 피보나치 수열1 ##
#################
def make_fibonacci_1(num):
    if num == 1:
        return 1
    if num == 2:
        return 1
    else:
        return make_fibonacci_1(num - 1) + make_fibonacci_1(num - 2)


#################
## 피보나치 수열2 ##
#################
_count = 0


def make_fibonacci_2(num):
    print("fibonacci({})를 구합니다.".format(num))
    global _count
    _count += 1

    if num == 1:
        return 1
    if num == 2:
        return 1
    else:
        return make_fibonacci_2(num - 1) + make_fibonacci_2(num - 2)


def make_fibonacci_memo(num):
    _dictionary = {1: 1, 2: 1}

    if num in _dictionary:
        return _dictionary[num]
    else:
        _result = make_fibonacci_memo(num - 1) + make_fibonacci_memo(num - 2)
        _dictionary[num] = _result
        return _result
