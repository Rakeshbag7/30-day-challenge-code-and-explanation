# Problem: Remove Duplicates from an Array

# Problem Statement:

You are given an array of integers. Your task is to remove all duplicate elements while preserving the order of their first occurrence.

Print the resulting array of unique elements in the order they first appeared in the input.

# Input Format

The first line contains an integer n — the number of elements in the array.
The second line contains n space-separated integers.

# Constraints
1 ≤ n ≤ 10^5  
-10^9 ≤ arr[i] ≤ 10^9

# Output Format
Print a single line with the unique elements separated by spaces, in their original order of first appearance.

# Sample Input 0
8
1 2 3 2 1 4 5 3

# Sample Output 0
1 2 3 4 5

# Sample Input 1
5
10 20 30 40 50

# Sample Output 1
10 20 30 40 50

# Approach
# 1. Read Input
Read an integer n — the number of elements in the array.
Read n integers and store them in a list arr.

# 2. Initialize Data Structures
Create an empty set seen to keep track of elements that have already appeared.
Create an empty list unique_elements to store unique numbers in the order they first appear.

# 3. Iterate Through the Array
For each element num in arr:
Check if num is not in seen.
If it’s not in seen:
Add it to seen (to mark it as encountered).
Append it to unique_elements (to preserve order).
If it’s already in seen, skip it (to remove duplicates).

# 4. Output the Result
After iterating through all elements, print the unique_elements list as a space-separated string.

# Notes
This solution passed all test cases on HackerRank.


In the second example:
All elements are already unique, so the output remains the same.
