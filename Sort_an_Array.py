'''
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
'''

def quickSort(nums):
    if len(nums) < 2:
        return nums
    else:
        pivot = nums[0]
        less = [i for i in nums[1:] if i <= pivot]
        greater = [i for i in nums[1:] if i > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)

def sortArray(nums):
    return quickSort(nums)
    
nums = [5,2,3,1]
nums = [5,1,1,2,0,0]
ans = sortArray(nums)
print(ans)