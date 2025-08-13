## Problem: Palindrome After Cleanup

## Problem Statement:
You are given a string s, which may contain letters (uppercase or lowercase), digits, spaces, and special characters.

Your task is to:
Remove all characters except alphabets and digits.
Convert all uppercase letters to lowercase.
Check if the cleaned-up string is a palindrome.
A palindrome is a string that reads the same backward as forward.

## Input Format
A single line containing the string s.

## Constraints:
1 ≤ |s| ≤ 10^5
The string may contain letters, digits, spaces, and special characters like @, #, ., etc.

## Output Format
Print "YES" if the cleaned string is a palindrome.
Print "NO" otherwise.

## Sample Input
A man, a plan, a canal: Panama

## Sample Output 
YES

## Approach

## Read Input:

Read the input string s.
## Palindrome function:
Cleanup the String:

Initialize an empty list cleaned. (This is the different from the previous approach-1)

Iterate through each character of s:
- If the character is alphanumeric, convert it to lowercase and append it to the cleaned list.

## Check Palindrome:
Join the cleaned list into a string.
Reverse the cleaned list and join it into another string.

## Compare the two strings:
- If they are the same, return "YES".
- Otherwise, return "NO".

## Output:
Print the result from the palindrome check function.

## Notes
This solution passed all test cases on HackerRank.
