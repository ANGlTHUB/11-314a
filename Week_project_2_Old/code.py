def countPairs(nums, target):
    
    #Sort the array in non-decreasing order. 
    #Sorting helps in efficiently exploring pairs
    
    nums.sort()  
    count = 0  
    n = len(nums)

    # initialize two pointers, left and right, pointing to the first and last elements of the sorted array.
    left = 0  
    right = n - 1  
    
    while left < right:  
        if nums[left] + nums[right] < target:
            count += (right - left)  # Increment count by pairs numbers
            left += 1
        else:
            right -= 1
        
    return count  

# Exemples arrays


nums = [-1, 1, 1, 2, 3]
target = 2

#  testing
output = countPairs(nums, target)
print("nums:", output)

#Seems correct!

'''

    Sort the array: [-1, 1, 1, 2, 3]
    Initialize count to 0.
    Set left to 0 and right to 4.
    Since -1 + 3 < 2, increment count by 4 - 0 = 4 and move left to 1.
    Since 1 + 3 < 2, increment count by 4 - 1 = 3 and move left to 2.
    Since 1 + 2 < 2, increment count by 4 - 2 = 2 and move left to 3.
    Since 1 + 1 < 2, increment count by 4 - 3 = 1 and move left to 4.
    The process ends with count equal to 10, which is the desired answer.

'''