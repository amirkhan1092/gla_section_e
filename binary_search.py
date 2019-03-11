# sorted
def search_binary(A,L,H,k):
    if L<=H:
        mid = int(L + (H-L)/2)
        if A[mid] == k :
            return True
        elif A[mid] > k:
            return search_binary(A,L,mid-1,k)
        elif A[mid] < k:
            return search_binary(A,mid+1,H,k)
    else:
        return False



B = [2,4,5,563,0,43,5,23,3,2]
B.sort()
k = int(input('enter the value'))
result = search_binary(B,0,len(B)-1,k)
print(result)