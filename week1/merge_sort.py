def merge(lst1, lst2):
    i, j = 0, 0
    result = []
    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            result.append(lst1[i])
            i += 1
        else:
            result.append(lst2[j])
            j += 1
    if i < len(lst1):
        result += lst1[i:]
    if j < len(lst2):
        result += lst2[j:]

    return result

def merge_sort(input_lst):
    if len(input_lst) <= 1:
        return input_lst
    lst = merge(
        merge_sort(input_lst[:len(input_lst) / 2]),
        merge_sort(input_lst[len(input_lst) / 2:])
    )
    print "lst", lst
    return lst
merge_sort([5,3,8,9,1,7,0,2,6,4])
#
# from random import shuffle
# test1_list = [2,34,4,4,43,3,3,2,3,2]
# assert merge_sort(test1_list) == sorted(test1_list)
# test2_list = [32432,3,32,2134249,435,43,3,-1,0,435,2,1,594,94,2,-90,-3,1]
# shuffle(test2_list)
# assert merge_sort(test2_list) == sorted(test2_list)
# shuffle(test2_list)
# assert merge_sort(test2_list) == sorted(test2_list)
# shuffle(test2_list)
# assert merge_sort(test2_list) == sorted(test2_list)
# shuffle(test2_list)
# assert merge_sort(test2_list) == sorted(test2_list)
# shuffle(test2_list)
# assert merge_sort(test2_list) == sorted(test2_list)
# shuffle(test2_list)
# assert merge_sort(test2_list) == sorted(test2_list)
# shuffle(test2_list)
# assert merge_sort(test2_list) == sorted(test2_list)
# shuffle(test2_list)
# assert merge_sort(test2_list) == sorted(test2_list)
# shuffle(test2_list)
# assert merge_sort(test2_list) == sorted(test2_list)
