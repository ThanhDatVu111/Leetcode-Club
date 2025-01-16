class Solution:
   def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
       neighborList = defaultdict(list)
       for s,d in edges:
           neighborList[s].append(d)
           neighborList[d].append(s)
           # 0: [1, 2],
           # 1: [0, 2],
           # 2: [1, 0]
      
       def dfs(vertex):
           if vertex in visited:
               return
           if vertex == destination:
               return True
           visited.add(vertex)
           for neighbor in neighborList[vertex]:
               if dfs(neighbor) == True:
                   return True
           return False


       visited = set()
       return dfs(source)