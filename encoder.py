def lucas(data):
    output = 2*data
    return output

def lekhmus(data):
    output = 15-data
    return output
num = int(input("Enter a number: "))
num = lucas(num)
num = lekhmus(num)
print ("Your encoded number is",num)
