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
    for num_len in [0, 1, 2, 10]:
        nums = [randint(1, 99) for _ in range(num_len)]
        print(nums)
        print(insertion_sort(nums))
