matrix= [
    [1, 6, 10],
    [8, 5, 9],
    [9, 4, 15],
    [7, 3, 60]
]

# row traversal
print("row traversal:")
for i in matrix:
  for j in i:
    print(j,end=" ")
print()

# column traversal 
print("column traversal: ")
transpose_matrix=zip(*matrix)
transposed_matrix=[list(i) for i in transpose_matrix]
for i in transposed_matrix:
  for j in i:
    print(j,end=" ")
