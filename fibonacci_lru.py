from functools import lru_cache

@lru_cache
def fibo(n):
    if n <= 2:
        return 1
    return fibo(n-1) + fibo(n-2)
