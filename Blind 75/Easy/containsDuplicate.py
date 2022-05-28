# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Input: nums = [1,2,3,1]
# Output: true

# brute force sol O(n^2)
def _containsDuplicate(nums):
  for i in range(0, len(nums)): #n
    for j in range(i+1, len(nums)): #n
      if nums[i] == nums[j]: #1
        return True #1
  return False #1

def containsDuplicate(nums):
  # TODO: O(n) S(n)
  hash = {}
  for i in range(len(nums)): # n
    if nums[i] in hash: # 1
      return True # 1
    else: # 1
      hash[nums[i]] = True # 1
  return False # 1