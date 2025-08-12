## Problem: Find the Target (Binary Search)

## Problem Statement:

You are given a sorted array of integers in non-decreasing order and a target value. Your task is to determine the index of the target in the array using binary search.

If the target exists in the array, print its 0-based index.
If the target does not exist in the array, print -1.

## Input Format:

First line contains an integer n — the size of the array.
Second line contains n space-separated integers — the elements of the array (sorted in non-decreasing order).
Third line contains an integer target — the value to search for.

## Constraints:

1 ≤ n ≤ 10^5
-10^9 ≤ arr[i], target ≤ 10^9
The array is sorted in non-decreasing order.

## Output Format:

Print a single integer — the index of target in the array, or -1 if not found.

## Sample Input 
8
-5 -2 0 3 3 3 7 9
3

## Sample Output 
3

## Explanation 

3 is at index 3 (any valid index with value 3 is acceptable if multiple occurrences are present).

## Approach:

## Read Input:

Take the size of the list n.

Read n sorted integers into the list arr.

Read the integer target to search for.

## Initialize Pointers:

lower points to the start of the list (0 index).

upper points to the end of the list (n-1 index).

## Search Process:

While lower <= upper:

Calculate mid = (lower + upper) // 2 (middle index).

If arr[mid] == target: return mid (index of target).

If arr[mid] < target: move search to the right half (lower = mid + 1).

Else: move search to the left half (upper = mid - 1).

## Not Found Case:

If loop ends without finding the target, return -1.

## Notes
This solution passed all test cases on HackerRank.
