def numIdenticalPairs(nums):
    x = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                x += 1
    return x

# Example 1:
nums = [1, 2, 3, 1, 1, 3]
print (numIdenticalPairs(nums))

# Example 2:
nums = [1,1,1,1]
print(numIdenticalPairs(nums))

# Example 3:
nums = [1, 2, 3]
print(numIdenticalPairs(nums))



