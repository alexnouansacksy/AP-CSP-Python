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

        print("Bubble Sort")
        start = time.perf_counter()
        bubblesort = library.bubblesort(list)
        end = time.perf_counter()
        sortingTime = end - start
        bubbleTime = sortingTime

        for n in bubblesort:
            print(f"{n}")
        print(f"Sorting Time: {sortingTime} seconds")

        print("\nSelection Sort")
        start = time.perf_counter()
        selectionsort = library.selectionsort(list)
        end = time.perf_counter()
        sortingTime = end - start
        selectionTime = sortingTime

        for n in selectionsort:
            print(f"{n}")
        print(f"Sorting Time: {sortingTime} seconds")

        print("\nInsertion Sort")
        start = time.perf_counter()
        insertionsort = library.insertionsort(list)
        end = time.perf_counter()
        sortingTime = end - start
        insertionTime = sortingTime

        for n in insertionsort:
            print(f"{n}")
        print(f"Sorting Time: {sortingTime} seconds")

        print("\nPython Sort")
        start = time.perf_counter()
        pythonsort = library.pythonSort(list)
        end = time.perf_counter()
        sortingTime = end - start
        insertionTime = sortingTime

        for n in pythonsort:
            print(f"{n}")
        print(f"Sorting Time: {sortingTime} seconds")

        bestTime = min(bubbleTime, selectionTime, insertionTime)
        if bestTime == bubbleTime:
            bestTime = "bubble sort"
        if bestTime == selectionTime:
            bestTime = "selection sort"
        if bestTime == insertionTime:
            bestTime = "insertion sort"


        print(f"\nFastest sort (our implementation): {bestTime}")

    except Exception as e:
        print("Error: ", e)

    return

if __name__ == "__main__":
    main()