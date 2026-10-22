3Sum Closest — LeetCode Solution
Problem Description


Given an integer array nums and an integer target, find three integers in nums whose sum is closest to target.

Return the sum of the three integers.

You may assume that each input has exactly one solution.

Approach: Sorting + Two Pointers

This solution uses sorting and the two-pointer technique to efficiently find the triplet sum closest to the target.

Algorithm
Sort the array in ascending order to make pointer movement predictable.
Initialize variables:
n: stores the length of the array.
closest_sum: stores the current closest sum, initially set to infinity.
Iterate through the array using index i as the first element of the triplet.
Skip duplicate elements to avoid processing the same first element repeatedly.
Initialize two pointers:
lo = i + 1: points to the next element.
hi = n - 1: points to the last element.
Calculate the current sum of the three selected elements.
Update the closest sum if the current sum is closer to the target than the previous best sum.
Move the pointers:
If cur_sum == target, return immediately because the exact target has been found.
If cur_sum < target, increment lo to increase the sum.
If cur_sum > target, decrement hi to decrease the sum.
Return closest_sum after all possible pointer combinations have been explored.
Example

Input:

nums = [-1, 2, 1, -4]
target = 1


Output:

2


Explanation:

After sorting, the array becomes:

[-4, -1, 1, 2]


The triplet [-1, 1, 2] has a sum of 2.

Its difference from the target is:

|2 - 1| = 1

This is the closest possible sum, so the answer is 2.

Complexity Analysis
Time Complexity: O(n²)
Sorting takes O(n log n).
The outer loop takes O(n) iterations.
The two-pointer traversal takes O(n) per iteration.
Space Complexity: O(1) auxiliary space, excluding implementation-dependent sorting space.
Key Concepts
Array Sorting
Two-Pointer Technique
Absolute Difference
Greedy Search
Optimization
Time and Space Complexity Analysis
LeetCode

Problem: 16. 3Sum Closest

Note: The solution sorts nums in place, modifying the original array.
