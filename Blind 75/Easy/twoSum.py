#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.
#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

#brute force sol.
def _twoSum(nums, target):
  # TODO: O(n^2)
  for i in range(0, len(nums)): # n
    for j in range(i+1, len(nums)): # n
      if nums[i]+nums[j] == target: # 1
        return [i, j] # 1

def twoSum(nums, target):
  # TODO: O(n) S(n)
  complements = {}
  for i in range(len(nums)):
    diff = target - nums[i] # 2
    if diff in complements:
      return [complements[diff], i]
    else:
      complements[nums[i]] = i