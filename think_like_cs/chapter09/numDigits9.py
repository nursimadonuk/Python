def numDigits(n):
    n = str(n)
    i = 0
    for digit in n:
        i += 1
    return i
print(numDigits(191203727483))