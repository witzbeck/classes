"""
3 methods for displaying the Fibonacci sequence:
    two list methods & one resource-intensive recursive option
"""
from typing import Callable


def fib1(n: int, lst: list[int] = [0, 1]) -> list[int]:
    if n < 1:
        raise ValueError
    elif n == 1:
        return [0]
    elif n == 2:
        return lst
    else:
        for i in range(2, n):
            c = lst[-1] + lst[-2]
            lst.insert(-1, c)
        return lst


def fib2(n: int, lst: list[int] = [0, 1]) -> list[int]:
    if n < 1:
        raise ValueError
    elif n == 1:
        return [0]
    elif n == 2:
        return lst
    else:
        for i in range(2, n):
            lst.append(lst[-1] + lst[-2])
        return lst


def fib3(n: int, a: int = 0, b: int = 1):
    if n < 1:
        raise ValueError
    elif n == 1:
        return a
    elif n == 2:
        return b
    else:
        return fib3(n - 2) + fib3(n - 1)


def printfib(n: int, func: Callable, th: str = "th"):
    if 10 < n < 14:
        pass
    elif n % 10 == 2:
        th = "nd"
    elif n % 10 == 1:
        th = "st"
    elif n % 10 == 3:
        th = "rd"

    print(f"The {n}{th} # in the Fibonacci sequence is {func(n)}")


def testfib(niter: int) -> None:
    for i in range(1, niter + 1):
        for j, func in enumerate([fib1, fib2, fib3]):
            print(f"\nWhen n = {i}, fib{j} = {func(i)}")
