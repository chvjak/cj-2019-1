def mirror_path(other_path):
    my_path = list()
    for c in other_path:
        my_path.append('S' if c == 'E' else 'E')

    return "".join(my_path)
            

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    n = int(input()) # read a line with a single integer
    other_path = input() # read a line with a single integer

    my_path = mirror_path(other_path)
    print("Case #{}: {}".format(i, my_path))
    # check out .format's specification for more formatting options