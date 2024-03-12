"""
This code was originally written in the "InterviewBit" online compiler. 
It has been moved to my local IDE .
Additional examples have been added to test its functionality.
"""
import resource
class Solution:
    def sortColors(self, A):
        red, white, blue = 0, 0, len(A) - 1          # Initialize pointers red, white, and blue.

        while white <= blue:                         # Loop through the array
            if A[white] == 0:
                A[red], A[white] = A[white], A[red]  # If the current element is red (0), swap it with the element at the red pointer
                red += 1                             # Move both red to the right
                white += 1                           # Move both White to the right
            elif A[white] == 1:
                white += 1                            # If the current element is white (1), just move the white pointer to the right
            else:
                A[white], A[blue] = A[blue], A[white] # If the current element is blue (2), swap it with the element at the blue pointer
                blue -= 1                             # Move the blue pointer to the left
        
        return A

# Testing the function
solution = Solution()
print(solution.sortColors([0, 1, 2, 0, 1, 2]))  
print(solution.sortColors([0]))    
         
# Print memory usage
mem_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
print(f"Memory Usage: {mem_usage} KB")