# This is a sample Python script.
from algorithms.binarySearch import search
from algorithms.mergeSort import initMergeSort
from algorithms.quickSort import init


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

arr1 = [3, 6, 8, 10, 1, 2, 1]
arr = [1, 3, 3, 4, 5, 6, 7, 8]
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sorted  = init(arr1)
    mergeSort = initMergeSort(arr1)
    binarySearch = search(arr, 6)
    print("should be 5th index return:", binarySearch)
    binarySearch2 = search(arr, 23)
    print("should be -1 since not in arr return:", binarySearch2)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
