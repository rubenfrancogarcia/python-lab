input1 = [3, 6, 8, 10, 1, 2, 1]



def initMergeSort(arr: list[int]):
    print("inputs for mergeSort:", arr)
    start = 0
    end = len(arr) -1
    result = mergeSort(start,end,arr)
    print("sorted array:", result )


def mergeSort(start, end, arr):
    if end-start +1<= 1:
        return arr[start:end +1]
    middle = start + (end-start)//2
    mergeSort(start, middle, arr)
    mergeSort(middle +1, end, arr)

    return merge(start, middle, end, arr)

def merge(start, middle, end, arr):
    leftSide = arr[start:middle+1]
    rightSide = arr[middle+1:end+1]
    newArr = [0]* (end-start+1)
    i = 0
    j = 0
    k = 0
    while(i<len(leftSide) and j < len(rightSide)):
        if leftSide[i] <= rightSide[j]:
            newArr[k] = leftSide[i]
            i+=1
            k+=1
        else:
            newArr[k] = rightSide[j]
            j+=1
            k+=1

    while i<len(leftSide):
        newArr[k] = leftSide[i]
        i+= 1
        k+=1
    while j < len(rightSide):
        newArr[k] = rightSide[j]
        j+=1
        k+=1
    return newArr