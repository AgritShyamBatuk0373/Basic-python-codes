A=int(input("Enter a number"))
B=A
rev=0
while(A!=0):
    rem= A%10
    rev = rev*10+rem
    A= A//10
if(rev==B):
    print(" The number is palidrome.")
else:
    print(" The number is not a palidrome.")

