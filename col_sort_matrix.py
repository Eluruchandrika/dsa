matrix= [
    [1, 6, 10],
    [8, 5, 9],
    [9, 4, 15],
    [7, 3, 60]
]

# Transpose the matrix to easily access columns
def transpose_matrix(matrix):
  transpose=zip(*matrix)
  transposed_matrix=[list(i) for i in transpose]
  return transposed_matrix
def sort_matrix(transposed_matrix1):
  for i in transposed_matrix1:
    i.sort()
  return transposed_matrix1
def print_matrix(matrix):
  transposed_matrix1=transpose_matrix(matrix)
  sorted_matrix=sort_matrix(transposed_matrix1)
  transposed_matrix2=transpose_matrix(sorted_matrix)
  return transposed_matrix2
print(print_matrix(matrix))


