import library
import time


def main():
    try:
        list = []
        with open("data/prog408b.dat", 'r') as f:
            for line in f:
                ldata = line.split(" ")
                claire = int(ldata[0])
                list.append(claire)

        sortedList = sorted(list)

        num = int(input("Enter the number to search: "))

        start = time.perf_counter()
        linearUnsorted = library.linearSearch(list, num)
        end = time.perf_counter()
        linearUnsortedTime = end - start

        if linearUnsorted == -1:
            print("\nLinear Search (Unsorted): Number not found")
        else:
            print(f"\nLinear Search (Unsorted): Number found at index {linearUnsorted}")
        print(f"Search Time: {linearUnsortedTime}")

        start = time.perf_counter()
        linearSorted = library.linearSearch(sortedList, num)
        end = time.perf_counter()
        linearSortedTime = end - start

        if linearSorted == -1:
            print("\nLinear Search (Sorted): Number not found")
        else:
            print(f"\nLinear Search (Sorted): Number found at index {linearSorted}")
        print(f"Search Time: {linearSortedTime}")

        start = time.perf_counter()
        binary = library.binarySearch(sortedList, num)
        end = time.perf_counter()
        binaryTime = end - start

        if binary == -1:
            print("\nBinary Search:  Number not found")
        else:
            print(f"\nBinary Search:  Number found at index {binary}")
        print(f"Search Time: {binaryTime}")

    except Exception as e:
        print("Error: ", e)

    return


if __name__ == "__main__":
    main()

"""
Enter the number to search: 50

Linear Search (Unsorted): Number found at index 77
Search Time: 4.37e-05

Linear Search (Sorted): Number found at index 16
Search Time: 1.1200000000000001e-05

Binary Search:  Number found at index 16
Search Time: 1.2800000000000013e-05

Process finished with exit code 0



Enter the number to search: 102012

Linear Search (Unsorted): Number not found
Search Time: 7.439999999999999e-05

Linear Search (Sorted): Number not found
Search Time: 6.539999999999999e-05

Binary Search:  Number not found
Search Time: 1.839999999999996e-05

Process finished with exit code 0
"""