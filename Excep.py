def koordnation_setzen(x,y):
    if x < 0 or y < 0:
        raise(ValueError("Ungültige Koordination:",x,y))
    print("Koordinaten gesetzt")
def main():
    try:
        koordnation_setzen(10,-5)
        print("Scheint geklappt zu haben!")
    except ValueError:
        print("Fehler abgefangen")

main()