if __name__ == "__main__":
    phones = {
        "Bob Marley" : "11-22-33", #gdyby tu nie dać przecinka to python potraktuje tą linijkę i następna jako jedną warftość
        # #średnik jest przy wymienianiu kolekcji
        "Britney Spears" : "44-11-22", # warto dać na końcu wymieniania przecinek, w razie zamiany miejscami wymienionych żeczy - nie trzeba pamietać o dopisywaniu jego
        #x = 42, zrobi jednoelem krotkę (42,) nie zwracamy  42, tylko krotke
        #m0żna tu umieścić tylko niezmienialne rzeczy
        #słownik jest zmienialny i można dodawać do niego rzeczy, ale muszą to być dwie wartości - np.nazwa i tel
        "Justin Bieber": None # None to brak wartości -> potem możemy ją przypisać
    }
    print(
        phones # w [] przekazujemy klucz - liczba-string lub inna wartosć
    )

    phones ["Justin Bieber"] = "00-00-00" # przypisaliśmy biberowi tel
    print(phones)

    print(phones.keys()) #wyswietla pierwsze wartośći i unikatowe
    print(phones.values()) #wyswietla drugie watości

    #for value in phones.values:
    #for key in phones.keys: tautologia, zwraca listę
    # lepiej napisać:

    #for key in phones.items():
        #.items() zwraca listę krotek (klucz, value)
        #print(key, value)
    for person, phone_number in phones.items():
        print(person, phone_number)

    print("___________________GET_____________")
    print(phones.get("?????","No value")) # ta metoda zwróci pustą wartosc
    # drugi parametr sie pokaże, gdy nie będzie klucza

    print("___________________POP_____________")
    print(phones.pop("Britney Spears", None))

    print(phones)

    print("__________________METODA UPDATE__________________")
    phones.update({"Will Smith": "44-11-66", "Britney Spears": "99-88-77"})
    #dodaliśmy Willa i zmieniliśmy Britney numer
    prev_phones = phones.copy()
    phones.update(prev_phones) #zwracamy Britney numer
    print(phones)

    imiona = {}
    print(imiona.fromkeys(["Sam","Bob"], "???"))

    print(dict([("Sam", "11-22-33"),("Bob", "00-33-24")]))

    print("___________________SET DEFAULT_____________")
#wyświetli nie określoną rzecz
    print(phones.setdefault("Britney Spears", "No value"))

    print("_______CZY WARTOŚĆ JEST W ZBIORZE? TRUE/FALSE____________")
    print("Czy jest Britney w zbiorze numerów? Odp:", "Britney Spears" in phones)
#PESEL TO suma kontrolna -> prymitywny hash shasum hello.txt
#plik tekstowy to i tak ciąg binarny gra to olbrzymia liczba

