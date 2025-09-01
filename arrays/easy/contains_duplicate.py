from typing import List

def hasDuplicateBruteForce(nums: List[int]):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

def hasDuplicateHash():
    def hasDuplicate(nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
test1 = [1,2,3,1]
test2 = [1,2,3,4]
test3 = [1,1,1,3,3,4,3,2,4,2]

print("Brute Force Outputs:")
print(hasDuplicateBruteForce(test1))
print(hasDuplicateBruteForce(test2))
print(hasDuplicateBruteForce(test3))
print("---------------------------")
print("Optimized Outputs:")
print(hasDuplicateBruteForce(test1))
print(hasDuplicateBruteForce(test2))
print(hasDuplicateBruteForce(test3))