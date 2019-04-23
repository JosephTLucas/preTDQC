def decode(data):
    answer = []
    lehkmus = data*-1 + 15
    katen = round(((4 * lehkmus) ** (1.0/3.0))/2)
    morgan = katen - 2
    miano = morgan*2
    miano2 = morgan*2+2
    lucas = miano / 2
    lucas2 = miano2 / 2
    answer.append(lucas)
    answer.append(lucas2)
    return answer

num = int(input("Enter a number: "))
answer = decode(num)
print(answer)
