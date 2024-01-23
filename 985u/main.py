import library
import time
from helper import node
def main():
    try:
        print("ID\tScore")
        list = []
        with open("data/prg408a.txt", 'r') as f:
            for line in f:
                ldata = line.split(" ")
                myid = int(ldata[0])
                score = int(ldata[1])
                claire = node(myid, score)
                list.append(claire)

        for n in list:
            print(f"{n}")

        print("Quicksort Sort")
        start = time.perf_counter()
        quicksort = library.Quicksort(list)
        end = time.perf_counter()
        sortingTime = end - start

        for n in quicksort:
            print(f"{n}")
        print(f"Sorting Time: {sortingTime} seconds")


        '''
        bestTime = min(bubbleTime, selectionTime, insertionTime)
        if bestTime == bubbleTime:
            bestTime = "bubble sort"
        if bestTime == selectionTime:
            bestTime = "selection sort"
        if bestTime == insertionTime:
            bestTime = "insertion sort"


        print(f"\nFastest sort (our implementation): {bestTime}")

        '''

    except Exception as e:
        print("Error: ", e)

    return

if __name__ == "__main__":
    main()