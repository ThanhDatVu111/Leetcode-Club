def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
    # Create empty array
    result = []
    # Create row for each column
    for j in range(len(matrix[0])): #j is column (we append every number in the sam column into one row)
        result.append([])
        # Get each element from same column and insert into row
        for i in range(len(matrix)): #i is row.
            result[j].append(matrix[i][j])
    # Return result
    return result