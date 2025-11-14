import threading
import time

import requests


def foo_compute(n: int = 1000, i_: int = 0):
    # print("compute start")
    for i in range(n):
        print(i_)
        abs((i**10) / (-5))
    # print("compute done")


def foo_req(url: str = "https://www.google.com"):
    # print("req start")
    for i in range(1):
        resp = requests.get(url)
    # print("req done")


a = 0


def data_increase(add: int = 1):

    for i in range(2000000):
        global a
        a += add


def run(tread_flag: bool = False):

    start_time = time.time()

    if tread_flag:
        threads = []
        for i in range(2):
            thread = threading.Thread(target=data_increase)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
    else:
        for i in range(2):
            foo_req()
    print(f"Total time taken for compute: {time.time() - start_time}")


if __name__ == "__main__":
    run(True)

    print(a)
