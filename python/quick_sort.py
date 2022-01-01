from copy import copy
from random import randint
from typing import List

def quick_sort(numbers: List[int]) -> List[int]:
    nums = copy(numbers)
    
    def _partition(low, high) -> int:
        pivot = nums[high]
        i = low - 1
        for j in range(low, high):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        index = i + 1
        nums[index], nums[high] = nums[high], nums[index]
        return index

    def _quick_sort(low, high) -> None:
        if low > high:
            return
        index = _partition(low, high) 
        _quick_sort(low, index - 1)
        _quick_sort(index + 1, high)
    
    _quick_sort(0, len(nums) - 1)
    return nums

if __name__ == '__main__':
    nums = [randint(1, 99) for _ in range(10)]
    print(nums)
    print(quick_sort(nums)) 
