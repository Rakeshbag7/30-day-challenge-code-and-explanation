## Problem: Rotate an Array by k Positions

## Problem Statement:
You are given an array of integers and an integer k. Rotate the array to the right by k positions.
A single rotation to the right means: the last element moves to the first position, and all other elements shift one position to the right.
If k is larger than the size of the array, rotations wrap around (i.e. perform k % n rotations).
Your task is to output the final rotated array.

## Input Format

The first line contains two integers n and k — the size of the array and the number of positions to rotate.
The second line contains n space-separated integers — the elements of the array.

## Constraints
1 ≤ n ≤ 10^5
-10^9 ≤ arr[i] ≤ 10^9
0 ≤ k ≤ 10^9

## Output Format
Print a single line with the rotated array elements separated by spaces.

## Sample Input 0

5 2
1 2 3 4 5

## Sample Output 0
4 5 1 2 3

## Approach

## Read Input:
- Read integers n (size of array) and k (number of rotations).
- Read n integers into the list arr.

## Normalize Rotation:
- Compute k = k % n so that unnecessary extra full rotations are avoided.

## Perform Rotation:
- Repeat k times:
    - Store the last element of arr in a temporary variable.
    - Shift all elements one step to the right.
    - Set the first position arr[0] to the stored last element.

## Return Result:
- After performing k right rotations, return the modified array.

## Output:
- Print the rotated array elements separated by spaces.

