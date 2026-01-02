"""
Problem: Two Sum
Approach:
- Use a hashmap to store seen numbers and their indices
- For each number, check if target - num already exists
Time Complexity: O(n)
Space Complexity: O(n)
"""

def twoSum(nums,target):
    seen={}
    for i, num in enumerate(nums):
        comp=target-num
        if comp in seen:
            return [seen[comp],i]
        seen[num]=i
