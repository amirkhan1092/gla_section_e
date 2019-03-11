def size(A):
    return len(A),len(A[0])


# A = [[2,4,0],[3,6,9],[3,5,9]]
# B = [[3,5,6],[5,0,6],[2,3,4]]
#
# if size(A) == size(B):
#     result = [[0,0,0],
#               [0,0,0],
#               [0,0,0]]
#     for r in range(len(A)):
#         for c in range(len(A[0])):
#             result[r][c]=A[r][c]+B[r][c]
#
# else:
#     print('dimension not agree ')
#
# print(result)
# for i in result:
#     for j in i:
#         print(j,end='\t')
#     print()

def matrix_valid(A):
    l=len(A[0])
    for k in range(len(A)):
        if l!=len(A[k]):
            return False
    return True

a = [[2,4],
     [3,5,3],
     [3,5]]
print(matrix_valid(a))




