def bin2dec(z):
    result = 0
    i = len(z) - 1
    for bit in z:
        result += int(bit) * 2 ** i
        i -= 1
    return result


z = "11111000"
print(bin2dec(z), int(z, base=2))
