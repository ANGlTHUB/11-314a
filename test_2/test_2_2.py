def min_board_size(w, h, n):
    h_fit = (max(w, h) + w) // (w + h)                    # Calculate the maximum number of diplomas  horizontally
    v_fit = (max(w, h) + h) // (w + h)                    # Calculate the maximum number of diplomas  vertically
    total = h_fit * v_fit                                 # Calculate the total number of diplomas on the board
    
    if total >= n:                                        # If the total fit --> return the max side length
        return max(w, h)
    else:
        additional_squares = (n + total - 1) // total     # Calculate additional squares needed 
        return additional_squares * max(w, h)             # Return the minimum side length

# Input values
w, h, n = map(int, input().split())
print(min_board_size(w, h, n))
