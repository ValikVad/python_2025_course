from collections import deque
from typing import List

# result [0, 1, 2, 3, 3, 5]

# naive solution - O(nlogn)
def solution1(array: List[int]) -> List[int]:
    b = [abs(x) for x in array]
    return sorted(b);

# 2 pointers solution - O(n)
def solution2(array: List[int]) -> List[int]:
    left: int = 0
    right: int = len(array) - 1
    answer: List[int] = []

    while left <= right:
        if (abs(array[left]) >= abs(array[right])):
            answer.append(abs(array[left]))
            left += 1
        else:
            answer.append(abs(array[right]))
            right -= 1

    return answer[::-1]

# very smart solution - O(n)
def solution3(array: List[int]) -> List[int]:
    left: int = 0
    right: int = len(array) - 1
    answer: deque[int] = deque()

    while left <= right:
        if (abs(array[left]) >= abs(array[right])):
            answer.appendleft(abs(array[left]))
            left += 1
        else:
            answer.appendleft(abs(array[right]))
            right -= 1
        
    return answer;

def main() -> None:
    array = [-3, -2, 0, 1, 3, 5]
    print("Input:", *array);
    
    print("Output_1:", *solution1(array))
    print("Output_2:", *solution2(array))
    print("Output_3:", *solution3(array))

if __name__ == "__main__":
    main()