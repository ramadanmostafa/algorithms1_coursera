# Rselect(Array A, length n, order statistic i)
# 0- if n = 1 return A[1]
# 1- choose pivot p from A uniformly at random
# 2- partition A around p let j = new index of p
# 3- if j = i return p
# 4- if j > i return Rselect(1st part of A, length j - 1, order statistic i)
# 5- if j < i return Rselect(2nd part of A, length n - j, order statistic i - j)
def choose_pivot_first(lst):
    return 0

def choose_pivot_last(lst):
    return -1

def choose_pivot_random(lst):
    #random pivots
    from random import randrange
    return randrange(0, stop=len(lst))

def choose_pivot_median(lst):
    if len(lst) % 2 == 0:
        mid_index = len(lst) / 2 - 1
    else:
        mid_index = len(lst) / 2
    tmp_lst = sorted([lst[0], lst[mid_index], lst[-1]])
    return lst.index(tmp_lst[1])

def partition(lst, pivot):
    if lst[0] != lst[pivot]:
        lst[0], lst[pivot] = lst[pivot], lst[0]
    i = 1
    for j in range(1, len(lst)):
        if lst[j] < lst[0]:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
    lst[0], lst[i-1] = lst[i-1], lst[0]
    return lst[:i-1], lst[i:], i - 1

def randomized_selection(lst, order_statistic, choose_pivot_func):
    if len(lst) == 1:
        return lst[0]
    pivot = choose_pivot_func(lst)
    p_val = lst[pivot]
    less_part, greater_part, pivot_index = partition(lst, pivot)
    if pivot_index == order_statistic:
        return p_val
    elif pivot_index > order_statistic:
        return randomized_selection(less_part, order_statistic, choose_pivot_func)
    else:
        return randomized_selection(greater_part, order_statistic - pivot_index, choose_pivot_func)

print randomized_selection([9,8,7,6,5,4,3,2,1], 3, choose_pivot_random)
