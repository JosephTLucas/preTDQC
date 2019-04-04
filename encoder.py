#Create a function with your name.  Below is an example.
#Your function should accept an integer, modify it, and return the new integer.
def lucas(data):
    output = 2*data
    return output

num = int(input("Enter a number: "))
#Add your function below mine and assign the return value to the variable 'num'
#We'll create a series of calculations that will be our encoder 
num = lucas(num)
print ("Your encoded number is",num)
