def is_prime(n):
    if n < 0:
        return False
    s = int(n ** 0.5) + 1
    for i in range(2, s):
        if n % i == 0:
            return False
    return True

def get_key(my_dict, val): 
    for key, value in my_dict.items(): 
         if val == value: 
             return key 
    return "key doesn't exist"
    
def get_primes(N=20):
    numbers = [True] * (N + 1)
    last_prime = 2
    i = last_prime
    while last_prime ** 2 <= N:
        i += last_prime
        while i <= N:
            numbers[i] = False
            i += last_prime
        j = last_prime + 1
        while j <= N:
            if numbers[j]:
                last_prime = j
                break
            j += 1
        i = last_prime
    return [x for x in range(2, N) if numbers[x]]
