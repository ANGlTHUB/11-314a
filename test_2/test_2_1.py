def min_diff(stones, n, sum1, sum2, index):                       # find the minimum difference between two piles of stones
    if index == n:                                                # return the absolute difference between the sums of the two piles
        return abs(sum1 - sum2)

    # Recursive case:
    diff1 = min_diff(stones, n, sum1 + stones[index], sum2, index + 1)
    diff2 = min_diff(stones, n, sum1, sum2 + stones[index], index + 1)

    # Return the minimum difference between the two recursive calls diff1 and diff2
    return min(diff1, diff2)

# Define a wrapper to initialize the recursive function 
def min_diff_wrapper(stones):
    n = len(stones)
    return min_diff(stones, n, 0, 0, 0)

if __name__ == "__main__":
    n = int(input())                                 # number of stones
    stones = [int(input()) for _ in range(n)]        # list of weights of the stones
    min_difference = min_diff_wrapper(stones)        # Find the minimum difference of two piles of stones
    # Output 
    print(min_difference)
