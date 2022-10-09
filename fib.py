def fib(n): #globalna funkcja
    cache = {
        0: 0,
        1: 1,
    }

    def _fib(n): #funkcja wewnetrzna widzi cache
        # lokalna funkcja
        #F[n] = F[n-1] + F[n-2], F[0] = 0, F[1] = 1
        if n not in cache:
            cache[n] = fib(n-1) + fib(n-2)
        return cache [n]
    return _fib(n)


if __name__ == "__main__":
        print(
            fib(400)
        )

###########################################################
def fib2(n):
    a,b  = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
    return a

if __name__ == "__main__":
    #for val in fib(10):
        #print(val)
    fib_nums = list(fib2(10))
    print(fib_nums)