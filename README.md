Sort List
📌 Problem Description

Given the head of a singly linked list, sort the list in ascending order and return its sorted head.

The solution uses the Merge Sort algorithm to efficiently sort the linked list without converting it into an array.

💡 Approach

This solution uses Divide and Conquer with three helper operations.

Base Case: If the linked list is empty or contains only one node, return it because it is already sorted.
Find the Middle: Use the slow and fast pointer technique to find the middle node of the linked list.
Split the List: Separate the linked list into two halves by setting mid.next = None.
Recursive Sorting: Recursively sort both halves using sortList().
Merge Sorted Lists: Merge the two sorted halves using the merge() function.
Return the Result: Return the head of the merged, sorted linked list.

🧪 Example

Input:

head = [4,2,1,3]


Output:

[1,2,3,4]


Explanation:

The linked list is divided into smaller sublists, each sublist is sorted recursively, and the sorted sublists are merged together.

For example:

[4, 2, 1, 3]
       ↓
[4, 2]  [1, 3]
   ↓       ↓
[2, 4]  [1, 3]
       ↓
[1, 2, 3, 4]

⏱️ Complexity Analysis
Time Complexity: O(n log n) — The list is divided into halves recursively, and merging at each level takes linear time.
Auxiliary Space Complexity: O(log n) — The recursive call stack requires logarithmic space. The merge operation reuses existing nodes rather than creating new nodes for the sorted output.
🛠️ Concepts Used
Merge Sort
Divide and Conquer
Recursion
Fast and Slow Pointers
Singly Linked Lists
🎯 Key Takeaway

Merge Sort is an efficient algorithm for sorting linked lists because it achieves O(n log n) time complexity and merges nodes without requiring an additional array.

👨‍💻 Author

Python implementation of the Sort List problem using Merge Sort.

⭐ If you find this solution helpful, consider giving the repository a star!
