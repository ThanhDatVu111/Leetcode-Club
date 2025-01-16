def flipAndInvertImage(image: List[List[int]]) -> List[List[int]]:
       for i in range (0, len(image)):
           image[i].reverse()
           for j in range (0, len(image[i])):
               if image[i][j] == 1:
                   image[i][j] = 0
               else:
                   image[i][j] = 1
      
       return image
