# Problem: Sort the Unsorted

## Problem Statement:

You are given an unsorted array of integers. Your task is to sort the array in non-decreasing order and print the sorted array.

## Input Format:
First line contains an integer n — the number of elements in the array.
Second line contains n space-separated integers — the elements of the array.

## Constraints:
1 ≤ n ≤ 10^5
-10^9 ≤ arr[i] ≤ 10^9

## Output Format
Print the sorted array in non-decreasing order, with each element separated by a space.

## Sample Input 
5
3 1 4 2 5

## Sample Output 
1 2 3 4 5

## Approach
1. Read the integer `n` (number of elements).
2. Check if `n` is within the given constraints.
3. Read the list of integers.
4. Ensure the number of elements matches `n` and that all integers are within the given range.
5. Use Python's built-in `sort()` method to sort the list in ascending order.
6. Print the sorted list.

## Notes
This solution passed all test cases on HackerRank.

