from copy import copy
from typing import List
from random import randint

def insertion_sort(numbers: List[int]) -> List[int]:
    nums = copy(numbers)

    for i in range(len(nums)):
        temp = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > temp:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = temp

    return nums

if __name__ == '__main__':
    nums = [8, 7]
    print(nums)
    print(insertion_sort(nums))
