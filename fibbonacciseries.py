a=int(input( "Enter a number a"))
x=0
b=1
i=0

while(i<a):
    fib= x+b
    x=b
    b=fib
    i+=1
    print(fib)
print(" are fibbonacci series upto",a)
