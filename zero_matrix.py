from typing import List


def setZeroes(matrix: List[List[int]]) -> None:
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                ind = i - 1
                while ind >= 0:
                    if matrix[ind][j] != 0:
                        matrix[ind][j] = -1
                    ind -= 1
                ind = i + 1
                while ind < rows:
                    if matrix[ind][j] != 0:
                        matrix[ind][j] = -1
                    ind += 1
                ind = j - 1
                while ind >= 0:
                    if matrix[i][ind] != 0:
                        matrix[i][ind] = -1
                    ind -= 1
                ind = j + 1
                while ind < cols:
                    if matrix[i][ind] != 0:
                        matrix[i][ind] = -1
                    ind += 1
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] <= 0:
                matrix[i][j] = 0
    return matrix




if __name__ == "__main__":
    arr = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    setZeroes(arr)
    print("The Final Matrix is ")
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end=" ")
        print()