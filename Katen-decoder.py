import tdqcencoder

def lekhmus(num):
    output = 15 - num
    return output

def katen(num):
    num = num / 2
    if num > 0:
        num = (num ** (1/3))
        output = round(num.real) + round(num.imag)
    else:
        num = (num ** (1/3))
        output = round((num.real * 2) * -1)
    return output
    
def morgan(num):
    output = num - 2
    return output
    
def lucas(num):
    output = num / 2
    return output
    
def miano(num):
    output = num * 2
    return round(output)

x = tdqcencoder.main()
x = lekhmus(x)
x = katen(x)
x = morgan(x)
x = lucas(x)
x = miano(x)
result = x
bresult = result + 1
print('{l}, {y}'.format(l = result, y=bresult))

#I made it work with most negative numbers.
#Your floor division in Miano's function breaks some values because it "rounds down".
#Made the encoder into a function and imported it to use it in this script. See edits to encoder.py below
#Also, thank you for the answer to my garbage function.
"""
def main():
    num = int(input("Enter a number: "))
    #Add your function below mine and assign the return value to the variable 'num'
    #We'll create a series of calculations that will be our encoder 
    num = miano(num)
    num = lucas(num)
    num = morgan(num)
    num = katen(num)
    num = lekhmus(num)
    print ("Your encoded number is",num)
    return(num)
    
"""
