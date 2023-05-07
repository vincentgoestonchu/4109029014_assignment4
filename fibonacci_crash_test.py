import time


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


def find_max_n_for_crash():
    n = 0
    while True:
        start_time = time.time()
        fib(n+1)
        end_time = time.time()
        if end_time - start_time > 1:  # Execution time is too long
            return n-1
        n += 1


def fib_dp(n):
    if n <= 1:
        return n
    else:
        memo = [0] * (n+1)
        memo[0], memo[1] = 0, 1
        for i in range(2, n+1):
            memo[i] = memo[i-1] + memo[i-2]
        return memo[n]


def test_dp_crash(n):
    result = fib_dp(n+1)
    if result == float('inf'):
        return True
    else:
        return False


if __name__ == "__main__":
    max_n = find_max_n_for_crash()
    print("Maximum value of n such that computing F(n+1) recursively causes your computer to crash:", max_n)

    n = 10000  # Set a large value of n to test
    if test_dp_crash(n):
        print("The computer crashed while using dynamic programming to compute F_dp(n+1).")
    else:
        print("The computer did not crash while using dynamic programming to compute F_dp(n+1)!")