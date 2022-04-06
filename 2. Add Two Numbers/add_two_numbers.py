from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
      aux_1 = self
      aux_2 = other


      isEqual = True

      while(aux_1 is not None or aux_2 is not None):


        # checks for different lengths
        if(aux_1 is None or aux_2 is None):
          # if either one is None, and the other isn't
          # then they're different lengths, and therefore not equal
          isEqual = False
          break


        if(aux_1.val != aux_2.val):
          isEqual = False
          break

        aux_1 = aux_1.next
        aux_2 = aux_2.next

      return isEqual


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return ListNode(val = 0, next = None)