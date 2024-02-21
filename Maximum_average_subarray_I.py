'''
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
Any answer with a calculation error less than 10-5 will be accepted.
'''

def get_max_average(nums, k):
    l = 0
    r = k - 1
    now_sum = sum(nums[l:r+1])
    max_sum = now_sum
    while r < len(nums) - 1:
        r += 1
        l += 1
        now_sum = now_sum - nums[l - 1] + nums[r]
        if now_sum > max_sum:
            max_sum = now_sum
    return max_sum / k

nums = [1,12,-5,-6,50,3]
k = 4
# nums = [5]
# k = 1
ans = get_max_average(nums, k)
print(ans)
# Output: 12.75000