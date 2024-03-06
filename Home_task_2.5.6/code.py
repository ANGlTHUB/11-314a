"""
This code was originally written in the "InterviewBit" online compiler. 
It has been moved to my local IDE .
Additional examples have been added to test its functionality.
"""

class Solution:
    def solve(self, A):
        n = len(A)
        t = [0] * n                              # Initialize new result array with zeros.
        left, right = 0 , n - 1                  # Initialize left and right pointers.
        for i in range(n - 1, -1, -1):           # Traverse the array in reverse order, from right to left.
            if abs(A[left]) > abs(A[right]):     # Compare element absolute values.
                t[i] = A[left] * A[left]         # Insert left pointer element's square into result array.
                left += 1                        # Move left pointer to the center.
            else:
                t[i] = A[right] * A[right]       #Insert right pointer element's square into result array.
                right -= 1                       #Move right pointer to the center.
        return t                                 

#For testing 
solution = Solution()
# Exemple 1
input1 = [-6, -3, -1, 2, 4, 5]
print (solution.solve(input1))
#Exemple 2
input2 = [-5, -4, -2, 0, 1]
print (solution.solve(input2))




