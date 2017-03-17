def selection_sort(input_lst):
    num_items = len(input_lst)
    for i in range(num_items - 1):
        min_val_idx = i
        for j in range(i + 1, num_items):
            if input_lst[j] < input_lst[min_val_idx]:
                min_val_idx = j
        if min_val_idx != i:
            input_lst[i], input_lst[min_val_idx] =  input_lst[min_val_idx], input_lst[i]
    return input_lst

from random import shuffle
test1_list = [2,34,4,4,43,3,3,2,3,2]
assert selection_sort(test1_list) == sorted(test1_list)
test2_list = [32432,3,32,2134249,435,43,3,-1,0,435,2,1,594,94,2,-90,-3,1]
shuffle(test2_list)
assert selection_sort(test2_list) == sorted(test2_list)
shuffle(test2_list)
assert selection_sort(test2_list) == sorted(test2_list)
shuffle(test2_list)
assert selection_sort(test2_list) == sorted(test2_list)
shuffle(test2_list)
assert selection_sort(test2_list) == sorted(test2_list)
shuffle(test2_list)
assert selection_sort(test2_list) == sorted(test2_list)
shuffle(test2_list)
assert selection_sort(test2_list) == sorted(test2_list)
shuffle(test2_list)
assert selection_sort(test2_list) == sorted(test2_list)
shuffle(test2_list)
assert selection_sort(test2_list) == sorted(test2_list)
shuffle(test2_list)
assert selection_sort(test2_list) == sorted(test2_list)
