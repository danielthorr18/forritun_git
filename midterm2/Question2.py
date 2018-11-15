def get_prime_list(arr):
    result = []
    for i in arr:
        if is_prime(i):
            result.append(i)