f = open("input3_raw.txt")

def input():
    return f.readline()

import string


def primes(N):
    is_prime = [True] * (N + 1)
    
    is_prime[0] = is_prime[1]  = False

    for i in range(2, N + 1):
        j = 2 * i
        while j <= N:
            is_prime[j] = False
            j += i
            
    return {i for i, x in enumerate(is_prime) if x}

T = int(input())
N = 103
all_primes = primes(N)
all_primes_list = list(all_primes)

all_primes_list.sort()
print(T)
for i in range(T):
    decoded_message = input().strip()
    
    used_primes_list = all_primes_list[-26:]
    assert(len(used_primes_list) == 26)

    letter_to_primes_map = {l:used_primes_list[i] for i, l in enumerate(string.ascii_uppercase)}
    
    encoded_message_numbers = [letter_to_primes_map[l] for l in decoded_message]

    res = []
    for j, (primes1, primes2) in enumerate(zip(encoded_message_numbers[:-1], encoded_message_numbers[1:])):
        res.append(primes1*primes2)

    print(N, len(res))
    print(" ".join([str(x) for x in res]))