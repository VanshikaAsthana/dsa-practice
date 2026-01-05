"""
Problem: Contains Duplicate

Given an integer array nums, return True if any value appears
at least twice in the array, and return False if every element is distinct.

Approach:
- Use a hash set to keep track of elements seen so far
- If an element is already in the set, a duplicate exists

Time Complexity: O(n)
Space Complexity: O(n)
"""

def containsDuplicate(nums):
   seen={}
        for i,num in enumerate(nums):
            if num in seen:
                return True
            seen[num]=i
        return False

            
