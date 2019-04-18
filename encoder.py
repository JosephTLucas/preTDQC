def lucas(data):
    output = 2*data
    return output

def miano(x):
    out = x//2 
    return out

def morgan(data):
    output = data+2
    return output

def katen(data):
    output = ((data + data) * (data * data))
    return(output)

def lekhmus(data):
    output = 15 - data
    return output
num = int(input("Enter a number: "))
#Add your function below mine and assign the return value to the variable 'num'
#We'll create a series of calculations that will be our encoder 
num = miano(num)
num = lucas(num)
num = morgan(num)
num = katen(num)
num = lekhmus(num)
print ("Your encoded number is",num)
