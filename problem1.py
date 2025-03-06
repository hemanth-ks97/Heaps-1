# Time Complexity : O(nlogk)
# Space Complexity : O(k)
# Did this code successfully run on Leetcode : YES
# Any problem you faced while coding this : NO
from collections import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return min_heap[0]