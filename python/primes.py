from math import sqrt
from typing import List

def primes(num: int) -> List[int]:
    is_primes = [True] * (num + 1)
    is_primes[0] = is_primes[1] = False

    # k が素数かどうかは sqrt(k) より小さい素数で割り算すれば良い
    # それらの素数で割れなければ素数
    # ref: https://manabitimes.jp/math/992
    for i in range(2, int(sqrt(num))):
        if not is_primes[i]:
            continue
        for j in range(i * 2, num + 1, i):
            is_primes[j] = False
    return [i for i in range(num + 1) if is_primes[i]] 

if __name__ == '__main__':
    num = 101
    print(num)
    print(primes(num))  
