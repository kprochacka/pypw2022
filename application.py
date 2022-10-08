if __name__ == "__main__":
    items = [1,2,3,4,5]
    print (items[0])

    #n = len(items)
    # [n-1] - przedostatnia liczba z listy
    # [1:5:2] 1-> zaczynamy przedziałem domknietym 5 lub -1-> konczymy niedomkniętym, 2-> co druga wartość
    # [:5]-> wszystkie elem od samego poczAtku do niedomknietego
    # [1:]-> wszystkie elem od 1. z przedziałem dom
    # [::-1] -> wszystkie w odwrotnej kolejnosci

    #append dodaje pojedyncze osobne elementy na koncu
    items.append(10)
    print("append", items)
    # extend dodaje kolekcję do listy - nie da się jednej wartości dać, chyba ze z []
    items.extend([10,11,12])
    print("extend", items)
    #sort sortuje listę, na której jest przywołana, ale nie zwróci wyniku
    #sortred nie zmienia zawartości przekazanej listy, ale zwraca nową przesortowaną

    #reverse odwróci listę ale nie zwróci wyniku
    #reversed zwraca nową odwróconą listę

    #pop zmienia przekazaną listę i zwraca wynik
    #count liczy częstotliwość występowania elementów
    #index wyświetla wartość z wskazanej pozycji
##  items.index (1,1,5)
##  print("index", items)
    #remove usuwanie danego elementu
    #insert wstrzykujemy w daną pozycje wartość (gdzie, co)
    items.insert(1,99)
    print("insert", items)
##  pytanie : co zrobić żeby w liście insert nie było komendy z listy extend?
## PĘTLA FOR
    print("pętla FOR + item")
    for item in items:
        print (item)
    #####
    print("pętla FOR + range")
    for i in list(range (10)):
        print (i,items[i])
    # range ukryta lista, która po kolei policzy cyfry z listy (10)-> miejsca 0-9
    print("pętla WHILE")
    x=10
    while x>10:
        print (x)

    #x += 1 x = x + 1
    #x -= 1 x = x - 1
    #x /= 2 x = x/2  dzielenie w liczbach całkowitych -> //
    #x >= 10 x > lub = 10
    #! = to !=