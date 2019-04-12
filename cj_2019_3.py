f = open("input3.txt")
def input():
    return f.readline()
# LOCAL
#------------------------------------------------------------------------------------------------

import string

def gcd(a, b):
    a, b = (a, b) if a > b else (b, a)
    while a != b:
        a = a - b
        a, b = (a, b) if a > b else (b, a)

    return a

T = int(input())
for i in range(T):
    N, MESSAGE_LEN = [int(x) for x in input().strip().split(" ")]
    encoded_message = [int(x) for x in input().strip().split(" ")]
    
    used_primes = set()
    pos_to_encoded = [0] * (MESSAGE_LEN + 1)

    # primes_multiple, next_primes_multiple = p1 * p2, p2 * p3 ; next step: p1 * p2 == prev_p2 * prev_p3 = => p1 == prev_p2
    for j, (primes_multiple, next_primes_multiple) in enumerate(zip(encoded_message[:-1], encoded_message[1:])):
        if (primes_multiple == next_primes_multiple):
            if j != 0:
                prev_prime = pos_to_encoded[j - 1]
                this_prime = primes_multiple // prev_prime
            else:
                # _first_ 4 symbols in decoded seq are repeated pairs XYXY... => e.g primes12 = {3*5, 3*5}
                k = j
                while encoded_message[k] == encoded_message[k + 1]:
                    k += 1

                last_prime_in_pair_sequence = gcd(encoded_message[k], encoded_message[k + 1]) # => p2 is last of the letters in repeating seq.
                second_last_prime_in_pair_sequence = primes_multiple // last_prime_in_pair_sequence                    # => p1 is the other letter. Whic is first?

                # even number of code numbers => odd numbers of decoded letters => p2 is p1
                if (k - j + 1) % 2 == 0:
                    this_prime, next_prime = last_prime_in_pair_sequence, second_last_prime_in_pair_sequence 
                else:
                    this_prime, next_prime = second_last_prime_in_pair_sequence, last_prime_in_pair_sequence

        else:
            next_prime = gcd(primes_multiple, next_primes_multiple)
            this_prime = primes_multiple // next_prime 
        
        pos_to_encoded[j] = this_prime           

    last_prime = encoded_message[-1] // next_prime
    pos_to_encoded[MESSAGE_LEN] = last_prime
        
    used_primes_list = list(set(pos_to_encoded))
    used_primes_list.sort()
    
    primes_to_decoded_letter_map = {used_primes_list[i]:l for i, l in enumerate(string.ascii_uppercase)}
    
    assert len(used_primes_list) == 26

    #decode:
    res = []
    for encoded_letter_prime in pos_to_encoded:
        res.append(primes_to_decoded_letter_map[encoded_letter_prime])
        
    print("Case #{}: {}".format(i + 1, "".join(res)))