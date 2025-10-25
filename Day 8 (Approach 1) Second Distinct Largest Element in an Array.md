# Problem: Second Largest Distinct Element in an Array

# Problem Statement
You are given an array of integers (which may contain duplicate values, negative numbers, and very large or small values).
Your task is to find the second largest distinct element in the array.
If there is no second distinct largest element (i.e., all elements are the same), print "NO".
Important Notes
The "second largest" must be different from the largest element.
Duplicates do not count as distinct values.

# Input Format
The first line contains an integer n — the number of elements in the array.
The second line contains n space-separated integers.

# Constraints
2 ≤ n ≤ 10^5  
-10^9 ≤ arr[i] ≤ 10^9

# Output Format
Print the second largest distinct element.
If it does not exist, print NO.

# Sample Input 0
6
5 3 9 1 9 5

# Sample Output 0
5

# Approach
# 1. Read Input
Read an integer n — the number of elements in the array.
Read n space-separated integers into a list arr.

# 2. Validate Constraints
Ensure that:
The number of elements n satisfies 2 ≤ n ≤ 10^5.
Every element in arr lies within the range -10^9 ≤ arr[i] ≤ 10^9.
Proceed only if both conditions are true.

# 3. Remove Duplicates
Convert the list arr into a set named unique_elements to remove any duplicate values.
This ensures we only consider distinct elements for comparison.

# 4. Check Distinct Count
If there are fewer than two distinct elements (len(unique_elements) < 2),
print "NO" — because a second largest element doesn’t exist.

# 5. Sort the Unique Elements (TreeSet Concept)
Sort the set in ascending order using sorted().
This gives a sorted list sorted_elements similar to how a TreeSet maintains sorted order in other languages (like Java).

# 6. Find the Second Largest
The largest element is at index -1 (last element).
The second largest distinct element is at index -2.
Hence, return sorted_elements[-2].

# 7. Output the Result
Print the second largest distinct element if it exists.
Otherwise, print "NO".

# Note
This solution passed all test cases on HackerRank.
