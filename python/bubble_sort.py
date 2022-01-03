from copy import copy
from typing import List
from random import randint

def bubble_sort(numbers: List[int]) -> List[int]:
    nums = copy(numbers)
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

if __name__ == '__main__':
    for num_len in [0, 1, 2, 10]:
        nums = [randint(1, 99) for _ in range(num_len)]
        print(nums)
        print(bubble_sort(nums))
        print()
