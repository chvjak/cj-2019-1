f = open("input3.txt")

def input():
    return f.readline()

import string

def factorize(primes_multiple, all_primes):
    for p in all_primes:
        if primes_multiple % p == 0:
            return p, primes_multiple // p

    assert(False, "Could not find primes")

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
for i in range(T):
    N, MESSAGE_LEN = [int(x) for x in input().strip().split(" ")]
    encoded_message = [int(x) for x in input().strip().split(" ")]
    
    all_primes = primes(N)
  

    used_primes = set()
    pos_to_encoded = [0] * MESSAGE_LEN

    for j, (primes_multiple, next_primes_multiple) in enumerate(zip(encoded_message[:-1], encoded_message[1:])):
        p1, p2 = factorize(primes_multiple, all_primes)
        p3, p4 = factorize(next_primes_multiple, all_primes)
        
        if p1 != p3 and p1 != p4:
            pos_to_encoded[j] = p1
        else:
            pos_to_encoded[j] = p2

        if p4 == p1 or p4 == p2:
            p3, p4 = p4, p3

        
        used_primes.add(p1)
        used_primes.add(p2)
        used_primes.add(p3)
        used_primes.add(p4)
        

    used_primes_list = list(used_primes)
    used_primes_list.sort()
    
    primes_to_decoded_letter_map = {used_primes_list[i]:l for i, l in enumerate(string.ascii_uppercase)}
    
    assert(len(used_primes_list) == 26)

    #decode:
    res = []
    for j in range(MESSAGE_LEN - 1):
        res.append(primes_to_decoded_letter_map[pos_to_encoded[j]])

    res.append(primes_to_decoded_letter_map[p3])
    res.append(primes_to_decoded_letter_map[p4])

        
    print("Case #{}: {}".format(i + 1, "".join(res)))