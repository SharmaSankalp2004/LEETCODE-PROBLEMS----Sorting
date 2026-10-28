Wiggle Sort
Problem Description

Given an integer array nums, reorder it in-place so that it follows the wiggle pattern:

nums[0] <= nums[1] >= nums[2] <= nums[3] >= nums[4] ...

The goal is to arrange the elements so that consecutive elements alternate between smaller and larger values.

Approach: Sorting and Reversing

The solution uses sorting and array slicing to construct the wiggle pattern efficiently.

Algorithm
Sort the array in ascending order.
Calculate the middle index using (n - 1) // 2.
Reverse the first half, including the middle element, and assign it to the even indices.
Reverse the second half and assign it to the odd indices.
Modify the original array in-place.

Reversing both halves helps maintain the wiggle pattern, including when duplicate values are present.


Example

Input:

text
nums = [1, 5, 1, 1, 6, 4]


Output:

text
[1, 6, 1, 5, 1, 4]


Explanation:

The resulting array satisfies the wiggle pattern:

1 <= 6
6 >= 1
1 <= 5
5 >= 1
1 <= 4
Complexity Analysis
Time Complexity: O(n log n) — sorting the array dominates the running time.
Space Complexity: O(n) — sorting and slice-based assignments may require additional memory.
Key Concepts
Array manipulation
Sorting
Python slicing
In-place modification
Time and space complexity
Language

Python 3
