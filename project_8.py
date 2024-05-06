def countPermutations(n, k):
    # Base cases
    if k == n:
        return 1
    elif k == 0:
        return derangements(n)
    
    result = 0
    for i in range(1, n+1):
        if i == k:
            result += countPermutations(n-1, k-1)
        else:
            result += countPermutations(n-1, k)
    
    return result

def derangements(n):
    if n == 0:
        return 1
    elif n == 1:
        return 0
    else:
        return (n-1) * (derangements(n-1) + derangements(n-2))

# Read input values
n, k = map(int, input().split())

# Call the countPermutations function and print the result
print(countPermutations(n, k))
