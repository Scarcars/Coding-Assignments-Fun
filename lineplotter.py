a = float (input("Enter coefficiant a: "))
b = float (input("Enter coefficiant b: "))
c = float (input("Enter coefficiant c: "))

def QuadPlotter ():
    print ("Parabola y = ", a,"x^2 + ", b,"x + ", c,)
    return (calc)

def calc ():
    QuadPlotter()
    for x in range (0, 11, 1):
        if x <= 10:
            y = a * (x ** 2) + b * x + c
            print("At x =", x, "y =", y)
    while x <= 1000000:
        x = x * 10
        y = a * (x ** 2) + b * x + c
        print("At x =", x, "y =", y)
        
            

calc ()
