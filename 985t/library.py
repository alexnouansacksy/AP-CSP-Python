import numpy as np

def MergeSort(A):
    if len(A) > 1:
        arr = np.array_split(A, 2)
        L = arr[0]
        R = arr[1]
        MergeSort(L)
        MergeSort(R)
        Merge(A, L, R)
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
