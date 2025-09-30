# Three-Sum Brute Force Algorithm Performance Analysis

This project implements and analyzes the **Three-Sum problem** using a brute-force approach. The goal is to measure how runtime and operation counts scale as input sizes grow, and to compare results against the theoretical **O(n³)** complexity.

---

## Problem Statement

> **Given an array `A` of `n` distinct integers and a target integer `t`, determine if there exist three distinct elements `a, b, c` in the array such that:**
>
> $$
> a + b + c = t
> $$

* **Input:** Array of integers `A`, target integer `t`
* **Output:** `True` if such a triplet exists, otherwise `False`
* **Constraints:** Uses distinct indices $i, j, k$

---

## Implementation Details

* **Brute-force approach:** Check all possible triplets (`O(n³)` time complexity).
* **Operation counter:** Tracks the number of triplet checks.
* **Experiment setup:**

  * Array sizes tested: `[50, 100, 200, 400, 800]`
  * Each size repeated for 10 trials
  * Target is intentionally unreachable (`t = 9999`) to enforce worst-case behavior

---

## Features

* **`brute_troissum(arr, t)`**
  Returns `(found, counter)` where:

  * `found`: `True/False` if triplet exists
  * `counter`: number of triplets tested

* **`generate_list(sz)`**
  Creates a random integer array of size `sz`.

* **`make_table(...)`**
  Displays mean runtimes and operation counts in tabular form.

* **`visualize(...)`**
  Plots runtime vs. array size, and operation counts vs. array size (with `O(n³)` reference).

* **`runtime_tbl(...)`**
  Calculates and prints measured slowdown factors compared to expected `8x` increase per doubling (since runtime grows cubically).

---

## Example Output

### Runtime & Operations Table

```
   Array Size  Mean Runtime (s)  Mean Operations Count
0          50          0.0001              19,600
1         100          0.0008             161,700
2         200          0.0063           1,313,400
3         400          0.0510          10,626,600
4         800          0.4120          84,826,800
```

### Runtime Slowdown Factors

```
 Size Growth Expected Slowdown Measured Slowdown
   50 → 100           8x slower            7.9
  100 → 200           8x slower            7.8
  200 → 400           8x slower            8.1
  400 → 800           8x slower            8.0
```

### Visualization

* **Plot 1:** Array size vs. runtime (seconds)
* **Plot 2:** Array size vs. operations (log scale, with O(n³) reference line)

---

## How to Run

### Requirements

* Python 3.8+
* Dependencies:

  ```bash
  pip install numpy matplotlib pandas
  ```

### Run the Analysis

```bash
python three_sum_analysis.py
```

This will:

1. Generate arrays of different sizes
2. Run brute-force Three-Sum trials
3. Print tables of runtime and operations
4. Display performance graphs

To change target value:
select a new value for `t` inside the `main()` function

---
