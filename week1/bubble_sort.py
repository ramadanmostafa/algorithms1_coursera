def buble_sort(input_lst):
    items_num = len(input_lst)
    for i in range(items_num - 1):
        swapped = False
        for j in range(items_num - 1):
            if input_lst[j] > input_lst[j + 1]:
                input_lst[j], input_lst[j + 1] = input_lst[j + 1], input_lst[j]
                swapped = True
        if not swapped:
            return input_lst
    return input_lst

from random import shuffle
test1_list = [2,34,4,4,43,3,3,2,3,2]
assert buble_sort(test1_list) == sorted(test1_list)
test2_list = [32432,3,32,2134249,435,43,3,-1,0,435,2,1,594,94,2,-90,-3,1]
shuffle(test2_list)
assert buble_sort(test2_list) == sorted(test2_list)
shuffle(test2_list)
assert buble_sort(test2_list) == sorted(test2_list)
shuffle(test2_list)
assert buble_sort(test2_list) == sorted(test2_list)
shuffle(test2_list)
assert buble_sort(test2_list) == sorted(test2_list)
shuffle(test2_list)
assert buble_sort(test2_list) == sorted(test2_list)
shuffle(test2_list)
assert buble_sort(test2_list) == sorted(test2_list)
shuffle(test2_list)
assert buble_sort(test2_list) == sorted(test2_list)
shuffle(test2_list)
assert buble_sort(test2_list) == sorted(test2_list)
shuffle(test2_list)
assert buble_sort(test2_list) == sorted(test2_list)
