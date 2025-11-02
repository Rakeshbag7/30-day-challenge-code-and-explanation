## Matrix Multiplication

## Problem Statement
You are given two matrices A and B. Your task is to compute and output their matrix product C = A × B.
Matrix multiplication is defined as:
If A is of dimension p × q and B is of dimension q × r, then their product C = A × B is a p × r matrix where:

## Input Format
First line: three integers p q r — dimensions of matrices (A is p×q, B is q×r).
Next p lines: each line contains q space-separated integers — rows of matrix A.
Next q lines: each line contains r space-separated integers — rows of matrix B.

## Constraints
1 ≤ p, q, r ≤ 200
-10^4 ≤ A[i][j], B[i][j] ≤ 10^4

## Output Format
Print p lines. Each line contains r space-separated integers representing a row of matrix C.

## Sample Input 0
2 3 2
1 2 3
4 5 6
7 8
9 10
11 12

## Sample Output 0
58 64
139 154

## Approach

## Read Input:
- Read three integers p, q, r which represent dimensions of matrices.
- Read matrix A of size p x q.
- Read matrix B of size q x r.

## Validate Elements:
- Check every element of matrix A to ensure it lies within the allowed range.
- Check every element of matrix B to ensure it lies within the allowed range.

## Initialize Result Matrix:
- Create an empty result matrix C of size p x r.
- Fill all positions with 0 initially.

## Matrix Multiplication:
- For each cell C[i][j]:
    - Compute the sum of A[i][k] * B[k][j] for all k from 0 to q-1.
- Store this computed value in C[i][j].

## Output:
- Print all rows of the resulting matrix C.
