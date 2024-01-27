A=int(input("Enter a coeff of x^2"))
B=int(input("Enter a coeff of x"))
C=int(input("Enter a constant"))

D= B**2-(4*A*C)
if(D>=0):
    X1= (-B) +(D**(1/2))/(A*2)
    X2= (-B) -(D**(1/2))/(2*A)

    print("the roots of given quadratics are x1,x2=" ,X1,X2)

else:
    print(" the quadratic has not real roots")


