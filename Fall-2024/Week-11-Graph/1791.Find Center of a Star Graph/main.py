class Solution:
   def findCenter(self, edges: List[List[int]]) -> int:
       hashMap = {}
       center = 0
       max_frequency = 0


       for edge in edges:
          for node in edge:
               if node not in hashMap:
                   hashMap[node] = 1
               else:
                   hashMap[node] += 1
               if  hashMap[node] > max_frequency:
                   max_frequency = hashMap[node]
                   center = node
      
       return center