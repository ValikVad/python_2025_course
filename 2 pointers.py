print("Введите высоты через пробел:")
nums = list(map(int, input().split()))

left, right, max_area = 0, len(nums) - 1, 0
while left < right:
    height = min(nums[left], nums[right])
    max_area = max(max_area, height * (right - left))
    left, right = (left + 1, right) if nums[left] < nums[right] else (left, right - 1)

print("Максимальная площадь: ", max_area)