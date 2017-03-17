def sequential_search(lst, key):
    for i in range(len(lst)):
        if lst[i] == key:
            return i
    return -1

assert sequential_search([1,2,3,4,9,10], 2) == 1
assert sequential_search([1,2,3,4,9,10], 9) == 4
assert sequential_search([1,2,3,4,9,10], 1) == 0
assert sequential_search([1,2,3,4,9,10], 3) == 2
assert sequential_search([1,2,3,4,9,10], -5) == -1
assert sequential_search([1,2,3,4,9,10], 4) == 3
assert sequential_search([1,2,3,4,9,10], 10) == 5
assert sequential_search([1,2,3,4,9,10], 15) == -1
assert sequential_search([1,2,3,4,9,10], 5) == -1
assert sequential_search([1,2,3,4,9,10], 8) == -1
assert sequential_search([1,2,3,4,9,10], 15) == -1

def binary_search(lst, key, start, end):
    if len(lst) < 1:
        return -1
    elif start < 0 or start > end or end >= len(lst):
        return -1
    else:
        mid = (start + end) / 2
        if lst[mid] == key:
            return mid
        elif lst[mid] > key:
            return binary_search(lst, key, start, mid - 1)
        else:
            return binary_search(lst, key, mid + 1, end)

assert binary_search([1,2,3,4,9,10], 2, 0, 5) == 1
assert binary_search([1,2,3,4,9,10], 9, 0, 5) == 4
assert binary_search([1,2,3,4,9,10], 1, 0, 5) == 0
assert binary_search([1,2,3,4,9,10], 3, 0, 5) == 2
assert binary_search([1,2,3,4,9,10], -1, 0, 5) == -1
assert binary_search([1,2,3,4,9,10], 4, 0, 5) == 3
assert binary_search([1,2,3,4,9,10], 10, 0, 5) == 5
assert binary_search([1,2,3,4,9,10], 11, 0, 5) == -1
assert binary_search([1,2,3,4,9,10], 5, 0, 5) == -1
assert binary_search([1,2,3,4,9,10], 8, 0, 5) == -1
assert binary_search([1,2,3,4,9,10], 101, 0, 5) == -1
