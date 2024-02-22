'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.
'''

def get_max(nums):
    counter = 0
    counter_max = 0
    for i in range(0,len(nums)):
        if nums[i] == 1:
            counter += 1
        else:
            if counter > counter_max:
                counter_max = counter
            counter = 0
    if counter > counter_max:
                counter_max = counter
    return counter_max

nums = [1,1,0,1,1,1]
ans = get_max(nums)
print(ans)
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

# nums = [1,0,1,1,0,1]
# Output: 2