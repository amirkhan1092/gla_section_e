
# searching algorithm
# binary
# linear search
def binary_search(A,L,H,num):
    while L<=H:
        mid = int(L + (H-L)/2)
        if A[mid]==num:
            return True
        elif A[mid]>num:
            H = mid-1
        elif A[mid]<num:
            L = mid+1
    else:
        return False



a = [1,2,3,8,6,7,3]
a.sort()
# a = [1,2,3,3,6,7,8]
k = int(input('enter the value for search '))
data = binary_search(a,0,len(a)-1,k)
print(data)

