A=int(input("Enter a number"))
rev=0
while(A!=0):
    rem= A%10
    rev = rev*10+rem
    A= A//10

print(" Reverse of number is ", rev)
