# NEETCODE EASY

from typing import List

# Submission 1 - Brute Force (nested loops)
def twoSumBrute(nums: List[int], target: int):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

# Submission 2 - More Optimized (DOES NOT WORK - CHECKS SAME INDICES AGAINST ITSELF)
def twoSumWrong(nums: List[int], target: int):
    for i in range(len(nums)):
        remaining = target - nums[i]
        
        if remaining in nums:
            return [i, nums.index(remaining)]

# Submission 3 - Optimal (using dictionary)
def twoSumOptimal(nums: List[int], target: int):
    seen = {} # dictionary (value/index pairs)

    for i, x in enumerate(nums): # allows you to loop while keeping track of index (i = index, x = value)
        remainder = target - x
        if remainder in seen: # checks the KEYS of the dictionary for 'remainder'
            return [seen[remainder], i] # if seen, return i (current index) and seen[remainder] (index of seen number)
        seen[x] = i # set index x to a value of i

    # NOTE
    # list: when you use 'in', it looks through the VALUES of the list (ex: nums[i] provides value of nums at index i)
    # dictionaries: when you use 'in', it looks through the KEYS of the list (ex: seen[remainder] provides the key at which value 'remainder' is found in dictionary)


print("Brute Force Outputs:")
print(twoSumBrute([3,4,5,6], 7))
print(twoSumBrute([4,5,6], 10))
print("---------------------------")
print("Optimized Outputs:")
print(twoSumOptimal([3,4,5,6], 7))
print(twoSumOptimal([4,5,6], 10))