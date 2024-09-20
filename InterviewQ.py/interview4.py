# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        # Create a dummy node to start the merged list
        dummy = ListNode(0)
        current = dummy
        
        # Traverse both lists and compare nodes
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # If one list is longer, append the rest of it
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        
        # Return the head of the merged list (skip the dummy node)
        return dummy.next

# Helper function to create a linked list from a Python list
def create_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a Python list for printing
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test the function
solution = Solution()

# Example 1 (implied from previous examples)
list1 = create_linked_list([1,2,4])
list2 = create_linked_list([1,3,4])
result1 = solution.mergeTwoLists(list1, list2)


# Example 2
list1 = create_linked_list([])
list2 = create_linked_list([])
result2 = solution.mergeTwoLists(list1, list2)


# Example 3
list1 = create_linked_list([])
list2 = create_linked_list([0])
result3 = solution.mergeTwoLists(list1, list2)
