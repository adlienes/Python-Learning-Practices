
#equation :ax^2+ bx + c
#delta : b^2 - 4ac
#x1: (-b -(delta^0.5)/2a)
#x2: (-b +(delta^0.5)/2a)


a=int(input("Enter A Value: "))
b=int(input("Enter B Value: "))
c=int(input("Enter C Value: "))

delta=b**2-4*a*c
x1=(-b-delta**0.5)/(2*a)
x2=(-b+delta**0.5)/(2*a)

print("Equation: {}x^2+{}x+{}".format(a,b,c))

print("X1: {}\n X2: {}".format(x1,x2))
