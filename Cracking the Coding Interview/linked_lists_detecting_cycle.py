###########################################################
#                                                         #
#   HackerRank Cracking the Coding Interview Challenges   #
#                                                         #
#             Linked Lists: Detect a Cycle                # 
#                                                         # 
###########################################################


"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    if head == None or head.next == None: return False
    tail, ahead = head, head.next.next
    while ahead != None:
        if ahead == tail: return True
        elif ahead.next != None: ahead=ahead.next
        else: return False
        tail, ahead = tail.next, ahead.next
    return False