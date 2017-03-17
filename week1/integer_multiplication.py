def int_mul(x, y):
    x = str(x)
    y = str(y)
    shift = 0
    result = 0
    for num1 in y[::-1]:
        shift_tmp = 0
        tmp_result = 0
        for num2 in x[::-1]:
            tmp_result += int(num2) * int(num1) * (10 ** shift_tmp) * (10 ** shift)
            shift_tmp += 1

        result += tmp_result
        shift += 1

    return result

assert int_mul(34, 12) == 34 * 12
assert int_mul(343, 666) == 343 * 666
assert int_mul(23, 443) == 23 * 443
assert int_mul(3444, 12234) == 3444 * 12234
assert int_mul(367904, 1243545) == 367904 * 1243545
assert int_mul(3435434, 122) == 3435434 * 122
assert int_mul(334557654, 120353) == 334557654 * 120353
assert int_mul(3994, 12043593) == 3994 * 12043593
assert int_mul(335983470597345893740572034824, 1200546954) == 335983470597345893740572034824 * 1200546954
assert int_mul(33247324, 1203856943) == 33247324 * 1203856943

x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627
print int_mul(x, y)
