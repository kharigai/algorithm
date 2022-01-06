from typing import List, NewType

IndexNumber = NewType('IndexNumber', int)

def binary_search(numbers: List[int], value: int) -> IndexNumber:
    def _binary_search(left: IndexNumber, right: IndexNumber) -> IndexNumber:
        if left > right:
            return -1

        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            return _binary_search(mid+1, right)
        else:
            return _binary_search(left, mid-1)

    return _binary_search(0, len(numbers) - 1)

if __name__ == '__main__':
    nums = [i for i in range(10) if i % 2]
    print(f'search list: {nums}')
    for i in range(10):
        print('search number: {}, get index: {}'.format(i, binary_search(nums, i)))
