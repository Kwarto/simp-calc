#vCalc  is the outermost function where math func are 
#Define
def vCalc():
    ##Perform Multiplication
    def multiplyAnyInput():
        #Above func handle multiplication

        print("Perform Multiplication!") 
        #print() is also a function it can take the following argument
        #print(*values: objects, sep="", end="/n") visit: docs.python.org 
        #to learn more - Print is use to display or as the name is to print 
        #something 

        x = float(input("What's x?: "))
        #Here, x is a variable that contains whatever the user will input
        #float() - is another function in python 
        #And it is use to convert floating-ppoint numbers (decimals) and also 
        #covert userInput from text(str) to number(int)
        y = float(input("What's y?: "))
        ##Refer from x:

        ##get ans
        output = round(x * y)
        #Here the ans for x,y is stored in output variable and we can see
        #Another function round() and it's use to round number to it precision decimal 
        #Number

        ##return ans
        print(x, "times", y, "=", f"{output:,}")
        #Here we're trying to the ans to the user
        # x - to print whatever the user input
        #"times" / "=" - is a str and y also to print whatever user input
        # f"{output:,}" f - help accept variable in a str ie: f"{join}"
        # eg. x = 2, y = 3 = 6 ...print ..2 times 3 = output(6)
    multiplyAnyInput() #to close the function

    ##Perform Addition
    def addValues():
        print("Perform Addition!")
        a = float(input("What's a?: "))
        b = float(input("What's b?: "))

        addVal = round(a + b)
        ##return ans
        print(a, "plus", b, "=", f"{addVal:,}")   
        #NOTES: Refer Multiple func    
    addValues()

    ##Perform Subtraction
    def minusFormat():
        print("Perform Subtraction!")
        m = float(input("What's m?: "))
        n = float(input("What's n?: "))

        minus = round(m - n)
        ##return minus
        print(m, "minus", n, "=", f"{minus:,}")
        #NOTES: Refer multiple function
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
        #NOTES: Refer multiple function
    divideValues()

    ##Perform Square Root
    def sRoot():
        #Here we can see nested function as earlier where vCalc is the main
        #Or the outermost function that will run before the next...

        print("Perform Square Root!")
        #Whatever we get from the user will be assign to the variable s.
        s = int(input("What's s?: "))
        ##return sRoot
        print(s, "square is:", square(s))
        #Square(s) - This here we can see  the func accept a parameter and that 
        #parameter is the s - and it parse as an argument 


    def square(n):
        #Here we define the square function we created and we assign n as parameter
        #n - becomes the s = because we have reassign s to n.

        return pow(n, 2) # n ** 2

        #return - is also python function and it returns result from function or k
        #statement... pow() is also a function - is equivalent to base **exp ie the power or square 
        #of a number 
    sRoot()
vCalc()


