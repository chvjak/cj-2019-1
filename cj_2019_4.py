import sys
sys.setrecursionlimit(2000)

def generate_query(n, b):
    b = max(b, 3)
    zeros = "0" * (b - 1)
    res = []
    for i in range(n // b):
        res.append(zeros)

    res.append("0" * (n % b))

    #return "10010001"
    return "1".join(res)

#def query(input_data, bad_bits = {0, 10, 25, 37, 38}): 
def query(input_data, bad_bits = {990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000}): 
    return "".join([x for i,x in enumerate(input_data) if i not in bad_bits])

def query1(input_data): 
    print(input_data)
    output_data = input()
    return output_data 


def rotate(l):
    l = list(l)
    l.append(l.pop(0))

    return "".join(l)

# TODO: DP
def get_possible_bad_bits1(input_data, output_data, b):   

    if (not len(input_data) == (len(output_data) + b)):
        return False, []

    if (len(output_data) == 0):
        return True, [[False] * len(input_data)] 

    if b == 0:
        if input_data == output_data :
            return True, [[True] * len(input_data)] 
        else:
            return False, []

    # current bit is good 
    if input_data[0] == output_data[0]:
        current_good_possible, current_good_solutions = get_possible_bad_bits(input_data[1:], output_data[1:], b)
    else:
        current_good_possible = False

    # current bit is bad 
    current_bad_possible, current_bad_solutions = get_possible_bad_bits(input_data[1:], output_data, b - 1)

    result = []
    if current_good_possible:
        result  += [[True] + s for s in current_good_solutions]

    if current_bad_possible:
        result  += [[False] + s for s in current_bad_solutions]

    return current_good_possible or current_bad_possible, result

def get_possible_bad_bits(input_data, output_data, B):   
    MAX_IX = len(input_data)
    MAX_OX = len(output_data)

    bits = [[None] * (MAX_OX + 1)][:] * (MAX_IX + 1)
    solution_valid = [[None] * (MAX_OX + 1)][:] * (MAX_IX + 1)

    for ix in range(MAX_IX + 1):
        for ox in range(MAX_OX + 1):
            bits[ix][ox] = [[]] * (B + 1)
            solution_valid[ix][ox] = [False] * (B + 1)

    for ox in range(MAX_OX):
        if input_data[MAX_IX - MAX_OX + ox:] == output_data[ox:]:
            bits[MAX_IX - MAX_OX + ox][ox][0] = [[True] * (MAX_OX - ox)] 
            solution_valid[MAX_IX - MAX_OX][ox][0] = True

    for b in range(B + 1):
        bits[MAX_IX - B + b][MAX_OX][b] = [[False]] * (MAX_IX - b)
        solution_valid[MAX_IX - B + b][MAX_OX][b] = True

    for ix in reversed(range(MAX_IX)):
        for ox in reversed(range(MAX_OX)):
            for b in range(B + 1):
                if (MAX_IX - ix == MAX_OX - ox + b):
                    result = []

                    if input_data[ix] == output_data[ox]:
                        if solution_valid[ix + 1][ox + 1][b]:
                            result += [[True] + s for s in bits[ix + 1][ox + 1][b]]
                            solution_valid [ix][ox][b] = True

                    if solution_valid[ix + 1][ox][b - 1]:
                        result += [[False] + s for s in bits[ix + 1][ox][b - 1]]
                        solution_valid [ix][ox][b] = True

                    bits[ix][ox][b] = result

    return bits[0][0][B]

res = get_possible_bad_bits("10110", "101", 2)
exit()


t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    n, b, f = [int(x) for x in input().strip().split(' ')]

    input_data  = generate_query(n, b) # TODO: should be regular seq of b zeros separated by ones
    output_data = query(input_data)
    sink, possible_bad_bits = get_possible_bad_bits(input_data, output_data, b)

    # TODO: generate as set
    pbb_set = set([tuple(x) for x in possible_bad_bits]) 
    prev_pbb_set = pbb_set 

    while len(pbb_set) > 1:
        input_data = rotate(input_data)
        output_data = query(input_data)     # TODO
        sink, possible_bad_bits = get_possible_bad_bits(input_data, output_data, b)

        pbb_set = set([tuple(x) for x in possible_bad_bits]).intersection(pbb_set)

    print(" ".join([str(i) for i, x in enumerate(pbb_set.pop()) if not x]))
    verdict = input()
    
    import sys
    sys.stdout.flush()