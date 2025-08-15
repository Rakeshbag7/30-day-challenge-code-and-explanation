## Problem:Case-Insensitive Character Frequency with Sorting

## Problem Statement:
You are given a non-empty string S which may contain letters (uppercase and lowercase), digits, spaces, and special characters .

Your task is to :

Ignore all spaces in the string.
Convert all letters to lowercase.
Count the frequency of each character (letters and digits only; exclude special characters like @, #, !, etc.).
Print the characters and their frequencies sorted by character in increasing order (lexicographically).

## Input Format
A single line containing the string S.

## Constraints
1 ≤ |S| ≤ 10^5
S can contain letters (a–z, A–Z), digits (0–9), spaces, and special characters.

## Output Format

## Output - c : f

c is the character (a lowercase letter or digit)
f is its frequency count in the cleaned string
✅ The output must be sorted by character in increasing order (i.e. digits 0–9 first, then letters a–z).

## Sample Input 
Hello World! 123

## Sample Output 

1 : 1
2 : 1
3 : 1
d : 1
e : 1
h : 1
l : 3
o : 2
r : 1
w : 1

## Approach

## Read Input:
- Read the input string s.

## Count Cleaned function:

## Clean and Convert:
- Initialize an empty list cleaned.
- Iterate over each character in s:
    - If the character is alphanumeric, convert it to lowercase and append it to cleaned.

### Sort Characters:
- Sort the cleaned list so that identical characters are adjacent.

## Count Frequencies:
- Initialize an empty list count.
- Use a while loop to traverse cleaned:
    - Store the current character in current and set its frequency to 1.
    - Increment the frequency while the next characters are the same.
    - Append [current, frequency] to count.

## Output Result:
- For each element in count, print the character and its frequency in the format:
  character : frequency

## Notes
This solution passed all test cases on HackerRank.
