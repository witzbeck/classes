from random import randint

rmin, rmax, ntests = 500, 5_000, 1_000

half = lambda x: x // 2
trip1 = lambda x: (3 * x) + 1
testint = lambda: randint(rmin, rmax)


def collatz(start_int: int, i: int = 0):
    """conjecture
        a sequence of positive integers will reach one when:
        x_{n} = 3x+1 when x_{n-1} is odd
        x_{n} = x//2 when x_{n-1} is even

    """
    if not isinstance(start_int, int):
        raise TypeError("input must be integer")
    elif start_int < 2:
        raise ValueError("input must be at least 2")
    x = start_int
    
    while x != 1:
        i += 1
        if x % 2 == 0:
            x = half(x)
        else:
            x = trip1(x)
    return i


def test(ntests: int):
    return [collatz(testint()) for _ in range(ntests)]


if __name__ == "__main__":
    print(test(ntests))