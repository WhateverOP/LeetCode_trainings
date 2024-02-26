'''
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2.
If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

Constraints:
    1 <= nums1.length <= nums2.length <= 1000
    0 <= nums1[i], nums2[i] <= 104
    All integers in nums1 and nums2 are unique.
    All the integers of nums1 also appear in nums2.
'''

def find_NGE(nums1, nums2):
    nums1_nums2_index_dict = {}
    for i in range(0, len(nums2)):
        if nums2[i] in nums1:
            nums1_nums2_index_dict[nums2[i]] = i
    NGE_list = [-1] * len(nums1)
    for i in range(0, len(nums1)):
        for j in range(nums1_nums2_index_dict[nums1[i]] + 1, len(nums2)):
            if nums2[j] > nums1[i]:
                NGE_list[i] = nums2[j]
                break
    return NGE_list

def find_NGE_effective_my(nums1, nums2):
    nums2_NGE_of_nums2_dict = {}
    stack_of_nums2 = []
    NGE_list = []

    stack_of_nums2.append(nums2[0])
    for i in range(1, len(nums2)):
        while len(stack_of_nums2) != 0 and nums2[i] > stack_of_nums2[-1]:
            nums2_NGE_of_nums2_dict[stack_of_nums2[-1]] = nums2[i]
            stack_of_nums2.pop()
        stack_of_nums2.append(nums2[i])

    for element in stack_of_nums2:
        nums2_NGE_of_nums2_dict[element] = -1
    
    for i in range(len(nums1)):
        NGE_list.append(nums2_NGE_of_nums2_dict[nums1[i]])

    return NGE_list

# hash = {}
#         for i in range(len(nums2)):
#             hash[nums2[i]] = i
#         res = []
#         for n in nums1:
#             s = -1
#             for i in range(hash[n], len(nums2)):
#                 if nums2[i] > n:
#                     s = nums2[i]
#                     break
#             res.append(s)
#         return res


# nums1 = [4,1,2]
# nums2 = [1,3,4,2]
# # Output: [-1,3,-1]

# nums1 = [2,4]
# nums2 = [1,2,3,4]
# # Output: [3,-1]

# ans = find_NGE(nums1, nums2)
# print(ans)

# ans = find_NGE_effective(nums1, nums2)
# print(ans)

nums1 = [1,3,5,2,4]
nums2 = [6,5,4,3,2,1,7]

# Output
# [7,-1,-1,-1,-1]
# Expected
# [7,7,7,7,7]

ans = find_NGE_effective_my(nums1, nums2)
print(ans)