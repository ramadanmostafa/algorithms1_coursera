def brute_force(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[i]:
                count += 1
    return count

assert brute_force([1,3,5,2,4,6]) == 3
assert brute_force([6,5,4,3,2,1]) == 15
assert brute_force([1,3,5,6]) == 0

def count_split_invertion(lst1, lst2):
    i, j, count = 0, 0, 0
    result = []
    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            result.append(lst1[i])
            i += 1
        else:
            result.append(lst2[j])
            count += len(lst1[i:])
            j += 1
    if i < len(lst1):
        result += lst1[i:]
    if j < len(lst2):
        result += lst2[j:]
    return result, count

def divide_conquer_invertions(lst):
    length = len(lst)
    if length < 2:
        return lst, 0
    left_lst, left_count = divide_conquer_invertions(lst[:length / 2])
    right_lst, right_count = divide_conquer_invertions(lst[length / 2:])
    lst_merged, split_count = count_split_invertion(left_lst, right_lst)
    return lst_merged, left_count + right_count + split_count

assert divide_conquer_invertions([1,3,5,2,4,6])[1] == 3
assert divide_conquer_invertions([6,5,4,3,2,1])[1] == 15
assert divide_conquer_invertions([1,3,5,6])[1] == 0

f = open("IntegerArray.txt")
lst = []
for line in f:
    lst.append(int(line))

print "answer"
print divide_conquer_invertions(lst)[1]
