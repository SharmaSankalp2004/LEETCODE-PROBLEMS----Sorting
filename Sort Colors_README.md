Sort Colors — LeetCode Solution
Problem Description

Given an integer array nums containing 0, 1, and 2, sort the array in-place so that all elements of the same color are adjacent, in the order:

0 → Red
1 → White
2 → Blue

You must solve the problem without using the library's built-in sorting function.

Approach: Dutch National Flag Algorithm

This solution uses three pointers to sort the array in a single pass without using extra space for another array.

Algorithm
Initialize three pointers:
l = 0: the next position for a 0.
r = len(nums) - 1: the next position for a 2.
i = 0: the current element being examined.
Iterate while i <= r:
If nums[i] == 0:
Swap nums[i] with nums[l].
Increment both l and i.
If nums[i] == 2:
Swap nums[i] with nums[r].
Decrement r.
Do not increment i, because the swapped-in element has not been examined yet.
If nums[i] == 1:
Increment i, because 1 is already in the correct middle region.
Finish: When i > r, all elements are sorted in-place.

Example

Input:

nums = [2, 0, 2, 1, 1, 0]


Output:

[0, 0, 1, 1, 2, 2]


Explanation:

The algorithm moves all 0s to the left, keeps 1s in the middle, and moves all 2s to the right.

The original array is modified directly, so the function does not need to return a new array.

Complexity Analysis
Time Complexity: O(n) — Each element is examined at most a constant number of times.
Space Complexity: O(1) — Sorting is performed in-place using only three pointers.
Key Concepts
Dutch National Flag Algorithm
Three-Pointer Technique
In-Place Sorting
Array Manipulation
Single-Pass Algorithms
Time and Space Complexity Analysis
LeetCode

Problem: 75. Sort Colors
