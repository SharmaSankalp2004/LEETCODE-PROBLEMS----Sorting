Number of Friend Requests
Problem Description

Given an integer array ages, where ages[i] represents the age of the 
𝑖
-th person, determine the total number of friend requests sent under the following rules.

A person of age x will not send a friend request to a person of age y if any of these conditions hold:

y <= 0.5 * x + 7
y > x
y > 100 and x < 100

Otherwise, the friend request is allowed. A person cannot send a friend request to themselves, but multiple people of the same age can send requests to each other.

Return the total number of valid friend requests.

Approach: Sorting and Two Pointers

The solution combines sorting, a frequency map, and two pointers to count valid friend requests efficiently.

Algorithm
Count frequencies: Use Counter to store the number of people of each age.
Sort the ages: Sorting allows valid age ranges to be processed in order.
Skip younger people: People younger than 15 cannot send valid requests under the given rules.
Find the valid lower bound: Calculate min_age = age * 0.5 + 7 and advance pointer j past ages that do not satisfy the lower-age constraint.
Count requests between equal ages: Add counts[age] - 1 to account for requests between people of the same age, excluding the sender.
Count requests to other valid ages: Use pointer k to track the beginning of the current age group and add k - j to count eligible people in the valid age range.
Return the accumulated result.
Example

Input:

text
ages = [16, 16, 17, 18]


Output:

text
4


Explanation:

Each person aged 16 can send a request to the other person aged 16: 2 requests.
Each person aged 16 can send a request to the person aged 17: 2 requests.
The person aged 18 can send requests to the two people aged 16 and the person aged 17, but the total depends on the age restrictions; in this example, the valid requests are counted by the algorithm.
Complexity Analysis
Time Complexity: O(n log n) — sorting takes O(n log n), while the pointer-based traversal is linear.
Space Complexity: O(n) — the frequency map can store up to n distinct ages.
Key Concepts
Sorting
Two pointers
Hash maps and frequency counting
Array traversal
Counting valid pairs
Language

Python 3
