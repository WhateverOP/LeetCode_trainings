'''Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

'''

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    center = arr[0]
    left = [arr[i] for i in range(1,len(arr)) if arr[i] < center]
    right = [arr[i] for i in range(1,len(arr)) if arr[i] >= center]
    return quick_sort(left) + [center] + quick_sort(right)

def get_majority_element(nums):
    elements_dict = {}
    for i in nums:
        if i not in elements_dict:
            elements_dict[i] = 0
        elements_dict[i] += 1
        if elements_dict[i] > len(nums) / 2:
            return i
        
def get_majority_element_qs(nums):
    if len(nums) == 1:
        return nums[0]
    nums_sorted = quick_sort(nums)
    center_index = len(nums) // 2
    return(nums_sorted[center_index])

# nums = [3,2,3]
# Output: 3

# nums = [2,2,1,1,1,2,2]
# Output: 2

nums = [2,2]

# ans = get_majority_element(nums)
ans = get_majority_element_qs(nums)
print(ans)

# qs = quick_sort(nums)
# print(qs)