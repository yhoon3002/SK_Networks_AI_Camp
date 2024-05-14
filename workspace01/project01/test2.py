import os

import b64.encoder

if __name__ == "__main__":
    print(__file__)

    # 실제 경로
    print(os.path.realpath(__file__))

    # 절대 경로
    print(os.path.abspath(__file__))