def sumOddLength(arr):
    result = 0
    n = len(arr)
    for i in range(n):
        result += ((i + 1) * (n - i) + 1) // 2 * arr[i]
    return result

# Test the function
arr1 = [1, 4, 2, 5, 3]
arr2 = [1, 2]
arr3 = [10, 11, 12]
print(sumOddLength(arr1))  
print(sumOddLength(arr2))  
print(sumOddLength(arr3)) 
