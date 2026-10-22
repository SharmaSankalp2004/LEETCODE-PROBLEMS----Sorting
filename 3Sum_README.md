3Sum — LeetCode Solution
Problem Description


Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]] such that:

i, j, and k are distinct indices.
nums[i] + nums[j] + nums[k] == 0.
The solution must not contain duplicate triplets.
Approach: Sorting + Two Pointers

This solution uses sorting and the two-pointer technique to efficiently find triplets whose sum equals zero.

Algorithm
Sort the array in ascending order to make it easier to compare sums and move pointers.
Iterate through the array using index i to select the first element of each triplet.
Skip duplicate elements: If the current element is the same as the previous element, skip it to avoid duplicate triplets.
Initialize two pointers:
j = i + 1: starts immediately after the current element.
k = len(nums) - 1: starts at the end of the array.
Calculate the sum of the three selected elements:
If the sum is greater than zero, decrement k to reduce the sum.
If the sum is less than zero, increment j to increase the sum.
If the sum equals zero, add the triplet to the result and move j forward.
Skip duplicate values after finding a valid triplet to ensure uniqueness.
Return the result containing all unique triplets.

Example

Input:

nums = [-1, 0, 1, 2, -1, -4]


Output:

[[-1, -1, 2], [-1, 0, 1]]


Explanation:

The unique triplets whose sum equals zero are:

[-1, -1, 2] → -1 + (-1) + 2 = 0
[-1, 0, 1] → -1 + 0 + 1 = 0

Duplicate triplets are avoided by skipping repeated values.

Complexity Analysis
Time Complexity: O(n²)
Sorting takes O(n log n).
The outer loop runs O(n) times, and the two-pointer traversal takes O(n) per iteration.
Space Complexity: O(1) auxiliary space, excluding the output and the space used internally by the sorting implementation.
Key Concepts
Array Sorting
Two-Pointer Technique
Duplicate Handling
Array Traversal
Time and Space Complexity Analysis
LeetCode

Problem: 15. 3Sum

Note: This solution modifies the input array by sorting it in place.
