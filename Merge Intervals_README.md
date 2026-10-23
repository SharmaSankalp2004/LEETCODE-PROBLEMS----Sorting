Merge Intervals
📌 Problem Description

Given an array of intervals where intervals[i] = [start, end], merge all overlapping intervals and return an array of non-overlapping intervals that cover all the intervals in the input.

💡 Approach

The solution uses a Greedy Algorithm with sorting.

Sort the intervals: Sort all intervals by their starting time in ascending order.
Initialize the output: Add the first interval to the output list.
Compare intervals: Iterate through the remaining intervals and compare each interval's start with the end of the last interval in the output.
Merge or append:
If the current interval overlaps with the last interval, merge them by updating the ending time to the maximum of both ending times.
Otherwise, append the current interval to the output list.
Return the result: Return the merged intervals.

🧪 Example

Input:

intervals = [[1,3],[2,6],[8,10],[15,18]]


Output:

[[1,6],[8,10],[15,18]]


Explanation:

[1,3] and [2,6] overlap, so they merge into [1,6].
[8,10] does not overlap with [1,6], so it remains separate.
[15,18] does not overlap with [8,10], so it remains separate.

The final result contains only non-overlapping intervals.

⏱️ Complexity Analysis
Time Complexity: O(n log n) — Sorting takes O(n log n) time, and traversing the intervals takes O(n) time.
Space Complexity: O(n) — The output list can store up to n intervals. Sorting space depends on the implementation.
🛠️ Technologies Used
Python 3
Sorting
Greedy Algorithm
Arrays and Lists
🎯 Key Takeaway

Sorting intervals by their starting times makes it easy to identify overlapping intervals and merge them efficiently in a single traversal.

👨‍💻 Author

Created as a Python solution to the Merge Intervals coding problem.

⭐ If you find this solution helpful, consider giving the repository a star!
