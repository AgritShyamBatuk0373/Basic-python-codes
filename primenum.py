A= int(input("Enter a numn"))
for a in range (1,(A+1)):
    p=0
for i in range (2,(a//2+1)):
    
    if(a%i==0):
        p+=1
        break
    
        
    if (p==0 and a!=1):
        print("%d"%a,end=' ')
    
    
