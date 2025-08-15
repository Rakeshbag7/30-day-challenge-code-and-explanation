## Problem: GCD of Multiple Numbers in a List

## Problem Statement:

You are given a list of N positive integers. Your task is to find the Greatest Common Divisor (GCD) of all the numbers in the list.

The GCD of a list of numbers is the largest positive integer that divides each of them without leaving a remainder.

## Input Format

The first line contains a single integer N — the number of elements in the list.
The second line contains N space-separated positive integers.

## Constraints
2 ≤ N ≤ 10^5
1 ≤ Ai ≤ 10^12

## Output Format
Print a single integer — the GCD of all the numbers in the list.

## Sample Input 
3
12 18 24

## Sample Output 
6

## Explanation 
GCD(12, 18, 24) = 6.

## Approach

## Read Input:
 Read an integer n (size of the list).
 Read n integers into the list a.

## GCD function:
## Initialize GCD:
 Set gcd to the first element of the list a.
 Initialize temp as 0.

## Iterate Through the List:
 For each element a[i] from index 1 to n-1:
     Assign x = gcd and y = a[i].
      Handle zero cases:
         If both x and y are 0, skip to the next element.
         If x is 0, set gcd = y and continue.
         If y is 0, set gcd = x and continue.

## Compute GCD Using Euclidean Algorithm:
 While y is not 0:
     Store y in temp.
     Set y = x % y.
     Set x = temp.
 Update gcd = x.

## Return Result:
 Return gcd after iterating through all elements.

## Output:
 Print the returned gcd value.

## Notes
This solution passed all test cases on HackerRank.

    

