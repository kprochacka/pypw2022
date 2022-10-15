import numpy as np

if __name__ == "__main__":
    x = [0, 1, 2, 3]
    y = np.fft.fft(x)
    print(y)

print("_________________ZAPOŻYCZENIE def Z INNEGO PLIKU___________")

from asbin import as_bin, bin2dec
if __name__ == "__main__":
    print(asbin.as_bin(10))
    print(asbin.bin2dec("1010"))