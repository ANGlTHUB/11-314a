def count_pairs(nums, k):
    nums.sort()
    count = 0
    i, j = 0, 1
    while j < len(nums):
        diff = abs(nums[j] - nums[i])
        if diff == k:
            count += 1
            j += 1
        elif diff < k:
            j += 1
        else:
            i += 1
            if i == j:
                j += 1
    return count

# Testing
nums1 = [1, 2, 2, 1]
k1 = 1
print(count_pairs(nums1, k1)) 

nums2 = [1, 3]
k2 = 3
print(count_pairs(nums2, k2))  

nums3 = [3, 2, 1, 5, 4]
k3 = 2
print(count_pairs(nums3, k3))
