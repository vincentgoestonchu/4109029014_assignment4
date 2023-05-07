import time
import matplotlib.pyplot as plt


def F_recursive(n):
    if n <= 1:
        return 1
    else:
        return F_recursive(n-1) + F_recursive(n-2)


def F_dynamic(n):
    dp = [0] * (n+1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


def measure_execution_time(func, n_values, threshold=None):
    times = []
    for n in n_values:
        if threshold and n >= threshold:
            times.append(1000)  # Mark as a large value
        else:
            start_time = time.time()
            func(n)
            times.append(time.time() - start_time)
    return times


def plot_results(n_values, recursive_times, dynamic_times):
    plt.plot(n_values, recursive_times, label='Recursive')
    plt.plot(n_values, dynamic_times, label='Dynamic Programming')
    plt.xlabel('n')
    plt.ylabel('Execution Time (s)')
    plt.legend()
    plt.show()


def main():
    n_values = list(range(10, 101, 10))
    threshold = 50

    recursive_times = measure_execution_time(F_recursive, n_values, threshold)
    dynamic_times = measure_execution_time(F_dynamic, n_values)

    plot_results(n_values, recursive_times, dynamic_times)


if __name__ == "__main__":
    main()