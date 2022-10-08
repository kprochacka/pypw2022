#krotka jest niezmienialna a lista zmienialna
# [] i () -> [1,1,2,2,3,4,10,11,15,16]
# {} -> {1, 2, 3, 4, 10, 11, 15, 16}
if __name__ == "__main__":
    items = {1,1,2,2,3,4,10,11,15,16}

    for item in items:
        print(item)

    print(42 in items)
    #items.add(100000)
    #print(items)
