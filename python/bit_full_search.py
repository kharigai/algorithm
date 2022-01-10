from typing import List

def bit_full_search(lst: List[int], value: int) -> bool:
    n = len(lst)
    is_exist = False
    for i in range(2**n):
        total = 0
        for j in range(n):
            if (i>>j)&1 == 1:
               total += lst[j] 
        if total == value:
            is_exist = True
            break
    return is_exist

if __name__ == '__main__':
    nums = [5, 8, 10]
    print(nums)
    for v in range(30):
        is_exist = bit_full_search(nums, v)
        if is_exist:
            print(f'{v}: {is_exist}')
