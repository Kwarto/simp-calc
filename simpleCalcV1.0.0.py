'''
 Write a python program that perform 
 Simple calculation from userInput
 create separate function to do the following
 calc: subtraction, multiplication, Addition, 
 Square Root, Division, Decimal Rounding..
'''

def vCalc():
    ##Perform Multiplication
    def multiplyAnyInput():
        print("Perform Multiplication!")
        x = float(input("What's x?: "))
        y = float(input("What's y?: "))

        ##get ans
        output = round(x * y)

        ##return ans
        print(x, "times", y, "=", f"{output:,}")
    multiplyAnyInput()

    ##Perform Addition
    def addValues():
        print("Perform Addition!")
        a = float(input("What's a?: "))
        b = float(input("What's b?: "))

        addVal = round(a + b)
        ##return ans
        print(a, "plus", b, "=", f"{addVal:,}")       
    addValues()

    ##Perform Subtraction
    def minusFormat():
        print("Perform Subtraction!")
        m = float(input("What's m?: "))
        n = float(input("What's n?: "))

        minus = round(m - n)
        ##return minus
        print(m, "minus", n, "=", f"{minus:,}")
    minusFormat()

    ##Perform Division
    def divideValues():
        print("Perform Division")
        d = float(input("What's d?: "))
        e = float(input("What's e?: "))

        ##Divide
        dvd = round(d / e)

        ##return ans
        print(d, "divided by", e, "=", f"{dvd:,}") 
    divideValues()

    ##Perform Square Root
    def sRoot():
        print("Perform Square Root!")
        s = int(input("What's s?: "))
        ##return sRoot
        print(s, "square is:", square(s))

    def square(n):
        return pow(n, 2)
    sRoot()
vCalc()


