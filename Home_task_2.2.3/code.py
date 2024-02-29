def sorting(s):
     # Split into individual words
    words = s.split()
     # Sort the words 
    words.sort(key=lambda x: int(''.join(filter(str.isdigit, x)))) 
    return ' '.join(word[:-1] for word in words)  # Join  and remove numeric suffix

# Example usage
input1 = "is2 sentence4 This1 a3"
output1 = sorting(input1)
print(output1)  

input2 = "Myself2 Me1 I4 and3"
output2 = sorting(input2)
print(output2) 
