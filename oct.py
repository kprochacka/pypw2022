def dec2oct(x):
#pass -> (no operation/noop) zaslepka
     if x == 0:
            return "0"
     result = ""
     while x != 0:
            x, reminder = divmod(x,8)
            result = str(reminder) + result
     return result

def oct2dec(x):
    result = 0
    # i = 0 i reverse (x) lub tylko enumerate (x)
    #for digit in reversed(x): #reverse odwraca listę x z 123 na 321
    for digit in enumerate(reversed(x)):
        result += int(digit) * 8 ** i
        #i +=1
    return result

if __name__ == "__main__":
    x = 42
    result = dec2oct(x)
    print(x, result, int(result, base=8), oct2dec(result))

