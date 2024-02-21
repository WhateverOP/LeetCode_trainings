'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
'''

def get_squares_array(nums):
    l = 0
    r = len(nums) - 1
    nums_2 = [i**2 for i in nums]
    nums_2_sorted = []
    while l <= r:
        if nums_2[l] >= nums_2[r]:
            nums_2_sorted.append(nums_2[l])
            l += 1
        else:
            nums_2_sorted.append(nums_2[r])
            r -= 1
    return nums_2_sorted[::-1]

nums = [-7,-3,2,3,11]
ans = get_squares_array(nums)
print(ans)
# [4,9,9,49,121]