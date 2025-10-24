# Problem: Merge Two Sorted Arrays

# Problem Statement:
You are given two sorted arrays in non-decreasing order.
Your task is to merge them into a single sorted array in non-decreasing order without using any built-in sort function.
You must maintain the order of elements and efficiently combine both arrays.

# Input Format
The first line contains an integer n — the size of the first array.
The second line contains n space-separated integers — elements of the first array (sorted).
The third line contains an integer m — the size of the second array.
The fourth line contains m space-separated integers — elements of the second array (sorted).

# Constraints
1 ≤ n, m ≤ 10^5  
-10^9 ≤ arr[i] ≤ 10^9  
Both arrays are already sorted in non-decreasing order.

# Output Format
Print a single line containing the merged sorted array with all elements separated by spaces.

# Sample Input
5
1 3 5 7 9
4
2 4 6 8

# Sample Output
1 2 3 4 5 6 7 8 9

# Approach
# 1. Read Input
Read an integer n — the size of the first sorted array.
Read n integers into a list r.
Read an integer m — the size of the second sorted array.
Read m integers into a list s.

# 2. Validate Constraints (Using If-Ladder)
Ensure that both n and m lie within the given range:
1 ≤ n, m ≤ 10^5
Check that the number of elements in each list matches the sizes given (len(r) == n and len(s) == m).
Confirm that every element in both arrays lies within the valid range:
-10^9 ≤ element ≤ 10^9.
Only if all these conditions are satisfied, proceed to merge the arrays.

# 3. Initialize Pointers and Merged List
Create two pointers, i and j, initially set to 0.
Create an empty list merged to store the merged result.
The pointers will track the current position in each array.

# 4. Merge the Two Sorted Arrays (Two-Pointer Technique)
While both arrays still have elements to compare (i < n and j < m):
If r[i] <= s[j], append r[i] to merged and increment i.
Otherwise, append s[j] to merged and increment j.
This ensures that the merged array remains sorted without using any built-in sorting function.

# 5. Append Remaining Elements
If elements remain in either r or s after one array is exhausted:
Append the remaining elements of r to merged if any.
Append the remaining elements of s to merged if any.

# 6. Output the Result
Convert the list merged into a space-separated string and print it.

# Notes
This solution passed all test cases on HackerRank.
