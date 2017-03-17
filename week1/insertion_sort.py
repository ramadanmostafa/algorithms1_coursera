def insertion_sort(input_lst):
    for i in range(len(input_lst)):
        valueToInsert = input_lst[i]
        holePosition = i
        while holePosition > 0 and input_lst[holePosition-1] > valueToInsert:
            input_lst[holePosition] = input_lst[holePosition-1]
            holePosition = holePosition -1

        input_lst[holePosition] = valueToInsert

    return input_lst


from random import shuffle
test1_list = [2,34,4,4,43,3,3,2,3,2]
assert insertion_sort(test1_list) == sorted(test1_list)
test2_list = [32432,3,32,2134249,435,43,3,-1,0,435,2,1,594,94,2,-90,-3,1]
shuffle(test2_list)
assert insertion_sort(test2_list) == sorted(test2_list)
shuffle(test2_list)
assert insertion_sort(test2_list) == sorted(test2_list)
shuffle(test2_list)
assert insertion_sort(test2_list) == sorted(test2_list)
shuffle(test2_list)
assert insertion_sort(test2_list) == sorted(test2_list)
shuffle(test2_list)
assert insertion_sort(test2_list) == sorted(test2_list)
shuffle(test2_list)
assert insertion_sort(test2_list) == sorted(test2_list)
shuffle(test2_list)
assert insertion_sort(test2_list) == sorted(test2_list)
shuffle(test2_list)
assert insertion_sort(test2_list) == sorted(test2_list)
shuffle(test2_list)
assert insertion_sort(test2_list) == sorted(test2_list)
