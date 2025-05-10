input1 = [3, 6, 8, 10, 1, 2, 1]


def init(arr: list[int]):
    print("inputs:", arr)
    start = 0
    end = len(arr) -1
    result = quickSort(start,end,arr)
    print("sorted array:", result )

##you can mess around with the initial pivot point. this uses the far right element as the pivot. you can have this same logic but swap the end and whatever index you want to use as pivot generally like a random value within range or the median value
def quickSort(start: int, end: int, arr: list[int]):
    if end - start + 1 <= 1: ## base case when arr is of size 1 or less
        return

    pivot = arr[end]
    left = start
    for i in range(start,end):
        if arr[i] < pivot:
            tmp = arr[i]
            arr[i] = arr[left]
            arr[left] = tmp
            left += 1
    arr[end] = arr[left]
    arr[left] = pivot
    ##here we partition one less and greater than pivot since pivot is already in the correct place
    quickSort(start, left-1, arr)
    quickSort(left + 1, end, arr)
    return arr