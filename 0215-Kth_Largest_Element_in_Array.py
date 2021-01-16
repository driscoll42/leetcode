'''
Difficulty: Medium

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''
import heapq

# Naive O(n Log n)
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         return sorted(nums, reverse=True)[k-1]


# Better O(n log k)
# class Solution(object):
#     def findKthLargest(self, nums, k):
#         nums = [x * -1 for x in nums]
#
#         heapq.heapify(nums)
#
#         for i in range(k):
#             return_val = heapq.heappop(nums)
#
#         return -1 * return_val

# O(n log k) but a bit more efficient
class Solution(object):
    def findKthLargest(self, nums, k):
        curr_val = -9999
        heap = []

        heapq.heapify(heap)

        for n in nums[:k]:
            heapq.heappush(heap, n)

        for n in nums[k:]:
            if n >= curr_val:
                heapq.heappush(heap, n)

            if len(heap) > k:
                curr_val = heapq.heappop(heap)

        return heap[0]