def gen_lines(filename):
    try:
        file_handle = open(filename)
    except IOError as e:
        print "cannot open the file", e
    else:
        for line in file_handle:
            yield line

for i in gen_lines("10000.txt"):
    print i.strip()
