def max_sum_from_ends(A, B):
    left_sum = 0
    right_sum = 0

    for i in range(B):
        left_sum += A[i]

    for i in range(B):
        right_sum += A[-i-1]

    return max(left_sum, right_sum)

# Test the function 
A = [5, -2, 3, 1, 2]
B = 3
print(max_sum_from_ends(A, B))  

A = [1, 2]
B = 1
print(max_sum_from_ends(A, B))  