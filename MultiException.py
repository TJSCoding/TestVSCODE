while True:
    try:
        eingabe = int(input("Eingabe: "))
        ergebnis = 10/eingabe

        print(ergebnis)
        break
    except (ValueError, ZeroDivisionError):
        print("Fehler bei der Berechnung!")
