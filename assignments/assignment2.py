# Three - Sum Brute Force Algorithm Performance Analysis
import time
import random
from typing import List, Tuple
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Given an array of n distinct integers and a target sum value, 
# determine if there exist three elements a, b, c in the array
# such that a + b + c equals the target sum.


# ThreeSum Problem Signature Input: Array A of n integers, 
# target integer t Output: true if ∃ i,j,k such that A[i] + A[j] + A[k] = t 
# false otherwise // Note: i, j, k should be distinct indices
def brute_troissum(arr, t):
    n = len(arr)
    counter = 0
    found = False
    # check there are atleast 3 in array
    if len(arr) >= 3:
        # first pointer, second, and third pointers
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    # check if we have our desired sum
                    counter += 1
                    # check sum
                    if arr[i] + arr[j] + arr[k] == t:
                        found = True
                        # exit if found
                        return found, counter
        return found, counter
    else:
        return found, counter # Not enough in array

def generate_list(sz): # test sizes = 50, 100, 200, 400, 800
    return np.random.randint(low=1, high=sz, size=sz).tolist()


def make_table(sz, tm, ops):
    # Create Graph with Averages
    data = {
        "Array Size": sz,
        "Mean Runtime (s)": tm,
        "Mean Operations Count": ops
    }
    df = pd.DataFrame(data)
    print(df)


def runtime_tbl(sizes, avg_times):
    # Used averages for this
    slowdown = []
    labels = []

    for i in range(1, len(sizes)):
        labels.append(f"{sizes[i-1]} → {sizes[i]}")
        slowdown.append(avg_times[i] / avg_times[i-1])

    data = {
        "Size Growth": labels,
        "Expected Slowdown": "8x slower (2³)",
        "Measured Slowdown": slowdown
    }
    df = pd.DataFrame(data)
    print("\nRuntime Slowdown Factors:")
    print(df.to_string(index=False))

def visualize(sizes, times, ops): # Create a graph plotting array size vs. runtime

    # Plot Average Runtime
    plt.figure(figsize=(10, 5))
    plt.plot(sizes, times, marker='o', color='royalblue', linewidth=2)
    plt.xlabel("Array Size (n)")
    plt.ylabel("Average Runtime (seconds)")
    plt.title("Three-Sum Brute Force: Array size vs Runtime")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()


    # Plot sizes v operation average
    plt.figure(figsize=(10, 5))
    plt.plot(sizes, ops, marker='o', color='royalblue', linewidth=2)
    # Get reference for O(n^3)
    plt.plot(sizes, [n**3 for n in sizes], linestyle='--', color='gray', label='O(n³) Reference')
    plt.xlabel("Array Size (n)")
    plt.ylabel("Operations")
    # use log to see slope
    plt.yscale("log")
    plt.legend()
    plt.title("Three-Sum Brute Force: Array size vs Operations")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()


def main():
    sizes = [50, 100, 200, 400, 800]
    trials = 10

    # report averages
    avg_times = []
    avg_ops = []

    for sz in sizes:
        # t = random.randint(1, sz)
        # t = sz
        # unatainable target to show O(n^3)
        t = 9999
        times = []
        ops = []
                

        for _ in range(trials):
            rand_arr = generate_list(sz)
            start = time.perf_counter()
            result, counter = brute_troissum(rand_arr, t)
            end = time.perf_counter()

            times.append(end - start)
            ops.append(counter)

        # record medians
        avg_times.append(np.mean(times, dtype=float))
        avg_ops.append(np.mean(ops, dtype=float))
    # normalize so can plot
    make_table(sizes, avg_times, avg_ops)
    # Create a graph plotting array size vs. runtime

    visualize(sizes, avg_times, avg_ops)
    # Calculate the growth rate between consecutive array sizes
    runtime_tbl(sizes, times)




if __name__ == '__main__':
    main()
    