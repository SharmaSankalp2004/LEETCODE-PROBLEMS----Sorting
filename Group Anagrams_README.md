Group Anagrams — LeetCode Solution
Problem Description

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Two strings are anagrams if they contain the same characters with the same frequencies, but the characters may appear in a different order.

Approach: Sorting + Hash Map

This solution uses a hash map (defaultdict) to group strings that have the same sorted characters.

Algorithm
Initialize a hash map: Create ans using defaultdict(list) to store groups of anagrams.
Iterate through each string: For every string s in strs:
Sort its characters using sorted(s).
Join the sorted characters into a string to create a unique key for its anagram group.
Append the original string to ans[key].
Return the groups: Convert the hash map's values into a list of lists.
Why does sorting work?

Anagrams contain exactly the same characters, so sorting their characters produces the same key.

For example:

"eat" → "aet"
"tea" → "aet"
"ate" → "aet"

All three strings share the same key and are placed in the same group.

Example

Input:

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


Output:

[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]


Explanation:

"eat", "tea", and "ate" share the sorted key "aet".
"tan" and "nat" share the sorted key "ant".
"bat" has the sorted key "abt" and forms its own group.
Complexity Analysis

Let:

n be the number of strings.
k be the maximum length of a string.

Time Complexity: O(n × k log k)

Sorting each string takes up to O(k log k).
Processing all n strings gives O(n × k log k) overall.

Space Complexity: O(n × k)

The hash map stores the strings and their grouping keys.
The output contains all input strings, requiring space proportional to their total length.
Key Concepts
Hash Maps
defaultdict
String Sorting
Anagrams
Grouping and Frequency Patterns
Time and Space Complexity Analysis
LeetCode

Problem: 49. Group Anagrams
