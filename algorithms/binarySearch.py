from typing import List

arr = [1, 3, 3, 4, 5, 6, 7, 8]


def search( nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        # (l + r) // 2 can lead to overflow
        m = l + ((r - l) // 2)

        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m
    return -1