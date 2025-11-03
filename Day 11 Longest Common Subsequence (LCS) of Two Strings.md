## Problem:Longest Common Subsequence (LCS) of Two Strings

## Problem Statement:
Given two strings A and B, find the length of their Longest Common Subsequence (LCS).
A subsequence of a string is obtained by deleting zero or more characters without changing the relative order of the remaining characters.
The Longest Common Subsequence is the longest sequence that is a subsequence of both strings.

## Input Format
The first line contains the string A.
The second line contains the string B.

## Constraints
1 ≤ |A|, |B| ≤ 1000
Strings consist of lowercase English letters only.

## Output Format
Print a single integer — the length of the longest common subsequence.

## Sample Input 0
abcde
ace

## Sample Output 0
3

Approach

Read Input:
- Read string A.
- Read string B.

Initialize DP Table:
- Create a 2D matrix of size (n+1) x (m+1) where n = len(A) and m = len(B).
- Initialize all values in this matrix to 0.
- This table will store the lengths of LCS for different prefixes of A and B.

Fill DP Table (Bottom-Up):
- Iterate i from 1 to n:
    - Iterate j from 1 to m:
        - If A[i-1] == B[j-1]:
            - Characters match → LCS grows by 1.
            - matrix[i][j] = matrix[i-1][j-1] + 1
        - Else:
            - Characters do not match → choose maximum from top or left cell.
            - matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

Final Result:
- The bottom-right value matrix[n][m] contains the length of the longest common subsequence.

Output:
- Print matrix[n][m]
