'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
'''

def search(nums, target):
    l = 0
    r = len(nums) - 1
    ans = -1
    while l < r:
        m = (l + r) // 2
        if nums[m] >= target:
            r = m
        else:
            l = m + 1
    if nums[l] == target:
        ans = l
    return ans

nums = [-1,0,3,5,9,12]
target = 9
ans = search(nums, target)
print(ans)