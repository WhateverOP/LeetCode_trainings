'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''

def mergeTwoLists(list1, list2):
    list3 = []
    i1 = 0
    i2 = 0
    while i1 < len(list1) or i2 < len(list2):

        if i1 == len(list1):
            list3.extend(list2[i2:])
            return list3
        if i2 == len(list2):
            list3.extend(list1[i1:])
            return list3

        if list1[i1] < list2[i2]:
            list3.append(list1[i1])
            i1 += 1
        else:
            list3.append(list2[i2])
            i2 += 1
    return list3

list1 = [1,2,4]
list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

list1 = []
list2 = []

list1 = []
list2 = [0]

ans = mergeTwoLists(list1, list2)
print(ans)


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def mergeTwoLists(list1, list2):
#     while list1 and list2:               
#             if list1.val < list2.val: