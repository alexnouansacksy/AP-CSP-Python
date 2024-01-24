def split_list(a_list):
    half = len(a_list) // 2
    return a_list[:half], a_list[half:]

def MergeSort(A):
    if len(A) > 1:
        L, R = split_list(A)
        L = MergeSort(L)
        R = MergeSort(R)
        A = Merge(A, L, R)

    return A
def Merge(A, L, R):
    i = 0
    j = 0
    k = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
        k = k + 1
    while i < len(L):
        A[k] = L[i]
        i = i + 1
        k = k + 1
    while j < len(R):
        A[k] = R[j]
        j = j + 1
        k = k + 1

    return A
