x = 4

# Check if x is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Find two prime x  whose sum equals the given even numbers
for i in range(2, x):
    if is_prime(i) and is_prime(x - i):
        result = [i, x - i]
        break

print(result)  # Output: [2, 2]
