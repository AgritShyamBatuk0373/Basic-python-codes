# A is used as variable for string
A=str(input(" Enter a string value")) 
rev=""
counter= len(A)
for i in A:
    rev= i + rev
    

if( rev==A):
    print(" string is a palindrome")
else:
    print("string is not a palidrome")
    
