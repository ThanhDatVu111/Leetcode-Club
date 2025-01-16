class Solution:
   def climbStairs(self, n: int) -> int:
       hash_map = {1:1,2:2}
       def f(x):
           if x in hash_map:
               return hash_map[x]
           else:
               hash_map[x] = f(x-2) + f(x-1)
               return hash_map[x]
       return f(n)
       # Time: O(n)
       # Space: O(n)