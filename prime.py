
def is_prime(n):

    if n == 1:
        return "to nie jest liczba pierwsza"
    i = 2
    while i * i <= n:
        if n % i == 0:
            return "to nie jest liczba pierwsza"
        i += 1
    return "to jest liczba pierwsza"


if __name__ == "__main__":
    n = float(input("podaj liczbę:"))
    print( is_prime(n))

    primes = [
        x for x in range(200) if is_prime(x)
    ]
    print(len(primes))
    print(primes)

def is_prime(n):
    for i in range (2, n):
        if n % i == 0:
            return False
    return True


