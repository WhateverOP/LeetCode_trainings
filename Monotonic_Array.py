'''
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.
'''

def is_monotonic(nums):
    zero_counter = 0
    counter = 0
    for i in range(0, len(nums) - 1):
        if nums[i + 1] - nums[i] < 0:
            counter -= 1
        elif nums[i + 1] - nums[i] > 0:
            counter += 1
        else:
            zero_counter += 1
    if zero_counter == len(nums) - 1:
        return True
    elif len(nums) - 1 - zero_counter == abs(counter):
        return True
    return False

# nums = [1,2,2,3]
# Output: true


# nums = [6,5,4,4]
# # Output: true

nums = [1,3,2]
# # Output: false

ans = is_monotonic(nums)
print(ans)
