from helpers.debug import *

if __name__ == "__main__":
    a = "Hello"  # 문자열
    b = '"Hello, I am "'
    c = 123  # 정수
    d = 3.141592  # 실수
    e = True  # 불리언

    f = r"\n"  # 로우로 처리
    g = "\\n"  # 더블로 처리

    file_path = "/Users/lim_younghoon/Desktop/workspace01/project01/main.py"

    long_line = """
    abc
    def
    ghijk
    lm
    opqr
    stuvw
    xyz
    """

    indexing = "안녕하세요 홍길동님"

    pi = None
    getType(pi)

    # getType(a)
    # getType(b)
    # getType(c)
    # getType(d)
    # getType(e)

    # pp(f)
    # pp(g)

    # getType(file_path)

    # pp(long_line)

    # pp(indexing[3] + indexing[3] + indexing[3])  # 세세세
    # pp(indexing[6:9])  # 홍길동
    # pp(indexing[-1])  # 님
    # pp(indexing[-4:-1])  # 홍길동
    # pp(indexing[6:-1])  # 홍길동
    # pp(indexing[6:])  # 홍길동님

    # pp(len(indexing))

    # pp(dir(indexing))
    # pp(dir(1))
