from functools import lru_cache
from typing import Dict, Generator, Union, Callable
from time import time

memo: Dict[int, int] = {0: 0, 1: 1}

def fib1(n: int) -> int:
    return fib1(n - 1) + fib1(n - 2)

def fib2(n: int) -> int:
    if n < 2:
        return n
    return fib2(n - 1) + fib2(n - 2)

def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib2(n - 1) + fib2(n - 2)        
    return memo[n]

@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    if n < 2:
        return n
    return fib2(n - 1) + fib2(n - 2)

def fib5(n: int) -> int:
    if n == 0: return 0
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
    return next

def fib6(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0: yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next
        
def test_fib(label: str, function: Callable[[int], Union[int, Generator[int, None, None]]], n):
    start_time = time()
    
    result = function(n)
    
    print("Label: {}".format(label))
    print("Result: {}".format(result))
    print("Elapsed time: {:.2f}s\n".format(time() - start_time))

if __name__ == "__main__":
    N = 40
    
    test_fib("Fib2", fib2, N)
    test_fib("Fib3", fib3, N)
    test_fib("Fib4", fib4, N)
    test_fib("Fib5", fib5, N)
    test_fib("Fib6", fib6, N)
    