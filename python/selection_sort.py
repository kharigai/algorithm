from copy import copy
from typing import List
from random import randint

def selection_sort(numbers: List[int]) -> List[int]:
    nums = copy(numbers)
    for i in range(len(nums)):
        min = i
        for j in range(i, len(nums)):
            if nums[j] < nums[min]:
                min = j
        nums[i], nums[min] = nums[min], nums[i]
    return nums

if __name__ == '__main__':
    nums = [randint(1, 99) for _ in range(10)]
    print(nums)
    print(selection_sort(nums))
