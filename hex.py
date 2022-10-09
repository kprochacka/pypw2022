def dec2hex(x):
    if x == 0:
        return "0"
    mapping = {
        10: "A", 11: "B", 12: "C",
        13: "D", 14: "E", 15: "F",
    }
    result = ""
    while x != 0:
        x, reminder = divmod(x, 16)
        if reminder <= 9:
            result = str(reminder) + result
        else:
            result = mapping[reminder] + result
    return result


def hex2dec(x): #FFAC5
    if x == 0:
        return "0"
    mapping = { #słownik definiuje sie w nawiasach klamrowych
        "A": 10, "B": 11, "C": 12,
        "D": 13, "E": 14, "F": 15,
    }
    # for digit in reversed(x): #reverse odwraca listę x z 123 na 321

    for digit in enumerate(reversed(x)):
        result += int(mapping.get(digit,digit)) * 16 ** i
    return result


if __name__ == "__main__":
    x = 2553
    value= dec2hex(x)
    print(x, value, hex2dec(value))