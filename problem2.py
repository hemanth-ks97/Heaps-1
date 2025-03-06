# Time Complexity : O(nlogk)
# Space Complexity : O(k)
# Did this code successfully run on Leetcode : YES
# Any problem you faced while coding this : NO


from collections import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        dummy = ListNode(-99)
        cur = dummy
        seen = set()

        while True:
            # end condition check
            null_count = 0
            for cur_node in lists:
                if cur_node == None:
                    null_count += 1
            
            if null_count == len(lists):
                break
            
            for i, headk in enumerate(lists):
                if headk and headk not in seen:
                    seen.add(headk)
                    heapq.heappush(min_heap, (headk.val, i))
            
            _,index = heapq.heappop(min_heap)
            seen.remove(lists[index])
            cur.next = lists[index]
            cur = cur.next
            lists[index] = lists[index].next
        
        return dummy.next
