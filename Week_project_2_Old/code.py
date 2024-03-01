def countPairs(nums, target):
    nums.sort()  
    count = 0  
    n = len(nums)
    # Initialize pointers
    lft = 0  
    rgt = n - 1  
    
    while lft < rgt:  
        if nums[lft] + nums[rgt] < target:
            count += (rgt - lft)  # Increment count by pairs numbers
            lft += 1
        else:
            rgt -= 1
    
    return count  

# Exemples arrays


nums2 = [-6, 2, 5, -2, -7, -1, 3]
target2 = -2

#  testing
output2 = countPairs(nums2, target2)
print("nums2:", output2)

#Seems correct!
