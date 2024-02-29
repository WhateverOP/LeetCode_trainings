'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
'''

# если ноль один - то все элементы кроме того что на его позиции будут 0 (см пример 2)
# если нуля два - то вообще все элементы 0
# если нет нулей, то можем использоват произведение всех элементов и делить его на текущий?

def get_product(nums):
    counter = 0
    zero_pos = 0
    product = 1
    ans = [0] * len(nums)
    for i in range(0, len(nums)):
        if nums[i] == 0:
            counter += 1
            if counter == 1:
                zero_pos = i
                continue
            else:
                return ans
        product = product*nums[i]
    if counter == 1:
        ans[zero_pos] = product
        return ans
    for i in range(0, len(nums)):
        ans[i] = product // nums[i]
    return ans

# nums = [1,2,3,4]
# Output: [24,12,8,6]

# nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

nums = [-1,1,0,-3,3,0]

ans = get_product(nums)
print(ans)
