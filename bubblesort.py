#zeby zmienic wersje to zakratkowac kazdy run
def sort(items):
    right = len(items)
    run = True
    while run:
    #for _ in range(len(items)):
        run = False
        for i in range(right-1):
            if items[i] > items[i+1]:
                items[i], items[i+1] = items[i+1], items[i]
                run = True
        right -=1
    return items

if __name__ == "__main__":
    result = sort([100, 9, 8, 7, 6, 5, 3, 0])
    print(result)