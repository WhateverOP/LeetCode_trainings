'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
'''

def find_single(nums):
    nums_count_dict = {}
    for i in range(0,len(nums)):
        if nums[i] not in nums_count_dict:
            nums_count_dict[nums[i]] = 0
        nums_count_dict[nums[i]] += 1
    index_1 = list(nums_count_dict.values()).index(1)
    ans = list(nums_count_dict.keys())[index_1]
    return ans

# nums = [2,2,1]
# # Output: 1
# nums = [4,1,2,1,2]
# # Output: 4
nums = [1]
# # Output: 1

ans = find_single(nums)
print(ans)