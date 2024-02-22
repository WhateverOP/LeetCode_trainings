'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
'''

# def move(nums):
#     nums_new = []
#     counter = 0
#     for i in range(0, len(nums)):
#         if nums[i] == 0:
#             counter += 1
#         else:
#             nums_new.append(nums[i])
#     zeroes_arr = [0 for i in range(counter)]
#     nums_new.extend(zeroes_arr)
#     return nums_new

def move(nums):
    i = 0
    j = len(nums) - 1
    while i <= j:
        if nums[i] == 0:
            nums.append(nums.pop(i))
            j -= 1
        else:
            i += 1
    return nums


nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# nums = [0]
# Output: [0]

# nums = [0,0,1]
# Output: [1,0,0]

ans = move(nums)
print(ans)