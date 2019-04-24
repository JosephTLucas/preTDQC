import encoder

num = float(input("Enter a number: "))

num = miano(num)
num = lucas(num)
num = morgan(num)
num = katen(num)
num = lekhmus(num)

encoded = num

def miano(num):
    decoded = num * 2
    return round(decoded)

def lucas(num)
    decoded = num / 2
    return decoded

def morgan(num)
    decoded = num - 2
    return decoded

def katen(num)
    decoded = round(((num - num) / (num / num)))
    return decoded

def lekhmus(num)
    decoded = num + 15
    return decoded

print ("Your encoded number is",num)
print ("Your decoded number is",decoded)
print (num,decoded)
