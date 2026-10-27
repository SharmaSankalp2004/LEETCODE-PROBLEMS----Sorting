# LeetCode 442 – Find All Duplicates in an Array

## Problem Description
Given an integer array `nums` of length `n`, where all integers are in the range `[1, n]` and each integer appears once or twice, return an array of all integers that appear twice.

The solution uses the **Negative Marking Technique** to find duplicates efficiently.

## Approach: Negative Marking

1. Initialize an empty list `ans` to store duplicate numbers.
2. Iterate through each element in the array.
3. Take the absolute value of the current element using `abs(x)`.
4. Use `x - 1` as the index corresponding to the number `x`.
5. If `nums[x - 1]` is negative, the number has already been visited, so add it to `ans`.
6. Otherwise, mark it as visited by multiplying `nums[x - 1]` by `-1`.
7. Return the list of duplicates.



## Example

**Input:**
```python
nums = [4, 3, 2, 7, 8, 2, 3, 1]
```

**Output:**
```python
[2, 3]
```

**Explanation:** The numbers `2` and `3` appear twice in the array.

## Complexity Analysis

- **Time Complexity:** `O(n)` — The array is traversed once.
- **Auxiliary Space Complexity:** `O(1)` — No additional data structure is used apart from the output list.

## Key Learning
- Array indexing
- Absolute values and sign manipulation
- In-place array modification
- Time and space complexity optimization

**Note:** This solution modifies the input array and assumes the constraints specified in LeetCode 442.
