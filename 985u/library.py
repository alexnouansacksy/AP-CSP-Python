def Quicksort(A, low = 0, high = None):
    if high is None:
        high = len(A) - 1
    if low < high:
        pivot = Partition(A, low, high)
        Quicksort(A, low, pivot - 1)
        Quicksort(A, pivot + 1, high)
    return A

def Partition(A, low, high):
    pivot = A[high]
    i = low - 1
    for j in range(low, high): # doesn't include the highest number, don't need (high - 1)
        if A[j] < pivot:
            i = i + 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
    temp = A[i+1]
    A[i+1] = A[high]
    A[high] = temp
    return i + 1

'''
Quicksort Sort
222	223
203	224
207	228
213	229
223	230
110	238
112	239
104	239
208	242
302	242
218	243
113	243
323	245
321	245
116	246
325	246
123	253
311	256
115	257
306	262
365	265
Sorting Time: 0.00013539999999999998 seconds

Process finished with exit code 0
'''