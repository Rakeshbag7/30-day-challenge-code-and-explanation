# Problem: Sort the Unsorted

## Problem Statement:

You are given an unsorted array of integers. Your task is to sort the array in non-decreasing order and print the sorted array.

## Input Format:
First line contains an integer n — the number of elements in the array.
Second line contains n space-separated integers — the elements of the array.

## Constraints:
1 ≤ n ≤ 10^5, 
-10^9 ≤ arr[i] ≤ 10^9

## Output Format
Print the sorted array in non-decreasing order, with each element separated by a space.

## Sample Input 
5
3 1 4 2 5

## Sample Output 
1 2 3 4 5

## Approach

## Read Input:

Take the integer n (size of the list).

Check if n satisfies 1 ≤ n ≤ 10^5.

Read n integers into the list arr.

## Validate Input:

Ensure that the number of elements entered matches n.

For each element in arr, check that it satisfies -10^9 ≤ a_i ≤ 10^9.

If any element is outside the allowed range, exit the program.

## Sorting:

Use Python’s built-in sort() method to arrange the list in ascending order.

## Output:

Print the sorted list elements in a single line separated by spaces.




## Notes
This solution passed all test cases on HackerRank.

