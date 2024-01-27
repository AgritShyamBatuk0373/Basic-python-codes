
a=int(input( "Enter a number a"))
b=int(input( "Enter a number b"))

i=0
while(i<a and i<b):
    i+=1
    if(a%i==0 and b%i==0):
        x=i

print(x)
