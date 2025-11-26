def iterative_pow(x, n):
    if n < 0:
        # to handle negative exponent by computing positive power and also invert
        return 1.0 / iterative_pow(x, -n)
    result = 1.0
    for _ in range(n):
        result *= x
    return result

print(iterative_pow(2.0, 10))  # Output: 1024.0
