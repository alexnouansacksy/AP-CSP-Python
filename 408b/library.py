def linearSearch(A, key):
    for i in range(0, len(A) - 1):
        if int(A[i]) == key:
            return i
    return -1

def binarySearch(A, key):
    low = 0
    high = len(A) - 1
    while low <= high:
        mid = int(low + (high - low) / 2)
        if A[mid] == key:
            return mid
        elif A[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

