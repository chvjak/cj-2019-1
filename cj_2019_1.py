def split_no_4(n):
    nn = str(n)
    ln = len(nn)
    aa = list('0' * ln)
    bb = list('0' * ln)
    for i, c in enumerate(nn):
        if c == '4':
            aa[i] = '2'
            bb[i] = '2'
        else:
            aa[i] = c

    return int(("".join(aa))), int("".join(bb))
            

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    n = int(input()) # read a line with a single integer
    a,b = split_no_4(n)
    print("Case #{}: {} {}".format(i, a, b))
    # check out .format's specification for more formatting options