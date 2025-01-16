import heapq #built in is auto min heap so it return the min if we pop
class Solution:
   def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
       heap = []
       result = []
       if not nums1 and not nums2: # make sure 2 lists not empty
           return result
       for i in range (0, len(nums1)):
           heapq.heappush(heap, (nums1[i] + nums2[0], i, 0)) # push nums1[i] pair with nums2[0] into heap (first pairs)
           #ex2 [1,1] [1,1] [2,1]


       while k > 0 and heap:
           total, i, j = heapq.heappop(heap)
           result.append([nums1[i], nums2[j]])
           k -= 1


           #Push the next pair from the current row of nums1 into the heap
           if j + 1 < len(nums2):
               heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j+1)) #i is always 0, so it a smallest number


       return result