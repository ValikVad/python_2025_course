import requests
import time

def main() -> None:
    start_time: time.time = time.time()
    requests_cnt: int = 100
    ok_count: int = 0

    for _ in range(0, requests_cnt):
        response = requests.get("https://www.ya.ru")
        if response.ok:
            ok_count += 1

    print(f"Count of requests: {requests_cnt}, OK of all: {ok_count}")
    print(f"Current time: {time.time() - start_time}")


if __name__ == "__main__":
    main()