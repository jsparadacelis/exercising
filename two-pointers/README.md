# Two pointers

## Some notes

## Exercise description
- Valid Palindrome: https://leetcode.com/problems/valid-palindrome/description/
- Two Sum II - Input Array Is Sorted: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
- Container with most water: https://leetcode.com/problems/container-with-most-water/description/
## Workarounds
- Valid palindrome: two pointers within a while. If the pointers are not in a valid alphanum char, iterate over the string until the pointer is in an alphanum value.
- Two Sum II - Input Array Is Sorted: two pointers then sum up left and right. If target is achieved return the pointers, if not compare target vs left and right. Based on which is closer, increase the pointer.
- Container with most water: two pointers. calculate the area of each iteration. If left pointer is less than right pointer, increase left, otherwise reduce right.
