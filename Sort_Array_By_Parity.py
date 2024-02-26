'''
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.
'''

def sort_by_parity(nums):
    l = 0
    r = len(nums) - 1
    while l < r:
        if nums[l] % 2 != 0:
            nums.append(nums.pop(l))
            r -= 1
        else:
            l += 1
    return nums

# nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

# nums = [0]
# # Output: [0]

nums = []

ans = sort_by_parity(nums)
print(ans)
