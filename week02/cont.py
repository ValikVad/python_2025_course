from typing import List

nums: List[int] = [1, 8, 6, 2, 5, 4, 8, 3, 7]
#                  |                        |
# result = 49


def area(h1: int, h2: int, p1: int, p2: int) -> int:
    return min(h1, h2) * (p2 - p1)


def max_area(h: List[int]) -> int:
    p1, p2 = 0, len(h) - 1
    max_area = area(h[p1], h[p2], p1, p2)

    while abs(p1 - p2) >= 1:
        if h[p1] > h[p2]:
            p2 -= 1
        else:
            p1 += 1

        cur_area = area(h[p1], h[p2], p1, p2)
        if max_area < cur_area:
            max_area = cur_area
    return max_area


print(max_area(nums))
