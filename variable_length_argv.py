
def search_binary(A,L,H,k):
    while L<=H:
        mid = int(L + (H-L)/2)
        if A[mid] == k:
            return True
        elif A[mid] > k:
            H = mid - 1
        elif A[mid] < k:
            L = mid + 1
    else:
        return False


















