'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

def twoSum(nums, target):
    diff_index_dict = {}
    for i in range(len(nums)):
        if nums[i] in diff_index_dict:
            return [i, diff_index_dict[nums[i]]]
        diff = target - nums[i]
        diff_index_dict[diff] = i
        
nums = [2,7,11,15]
target = 9
# nums = [3,2,4]
# target = 6
# nums = [3,3]
# target = 6
ans = twoSum(nums, target)
print(ans)