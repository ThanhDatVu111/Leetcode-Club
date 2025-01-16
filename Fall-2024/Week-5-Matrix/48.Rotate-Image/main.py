def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    # [[1, 2, 3],
    # [4, 5, 6],
    # [7, 8, 9]]

    # tmp = 1
    # matrix[0][0] = 7
    # matrix[2][0] = 9
    # matrix[2][2] = 3
    # matrix[0][2] = 1 (tmp)

    # [[7, 2, 1],
    # [4, 5, 6],
    # [9, 8, 3]]

    # tmp = 2
    # matrix[0][1] = 4
    # matrix[1][0] = 8
    # matrix[2][1] = 6
    # matrix[1][2] = 2 (tmp)

    # [[7, 4, 1],
    # [8, 5, 2],
    # [9, 6, 3]]

    n = len(matrix)
    # Tranpose
    for i in range(0,n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reflection
    for i in range(0,n):
        for j in range(0,1):
            matrix[i][j], matrix[i][n-1] = matrix[i][n-1], matrix[i][j]