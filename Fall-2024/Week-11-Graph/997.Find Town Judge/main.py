class Solution:
   def findJudge(self, n: int, trust: List[List[int]]) -> int:
       outgoing = defaultdict(int)
       incoming = defaultdict(int)
      
       for person1, person2 in trust:
           outgoing[person1] += 1
           incoming[person2] += 1
      
       for i in range(1, n+1): #since 1 <= n <= 1000
           if outgoing[i] == 0 and incoming[i] == n-1:
               return i
       return -1