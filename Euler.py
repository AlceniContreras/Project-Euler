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