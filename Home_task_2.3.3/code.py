def fn(nums):
    result = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if i != j and nums[j] < nums[i]:
                count += 1
        result.append(count)
    return result

# Example usage
input1 = [8, 1, 2, 2, 3]
output1 = fn(input1)
print(output1)  # Output: [4, 0, 1, 1, 3]

input2 = [6, 5, 4, 8]
output2 = fn(input2)
print(output2)  # Output: [2, 1, 0, 3]
