divmod(10,2) (10%2, 10//2)
#14 % 2 = 0
#14 // 2 = 7
def as_bin(x):
    x = float(input("podaj liczbę:"))
    if x == 0:
        return "0"
    result = ""
    while x != 0:
        x, bit = divmod(x,2)
        result = str(bit) + result
    return result

#####



if __name__ == "__main__":
    print(as_bin(0))