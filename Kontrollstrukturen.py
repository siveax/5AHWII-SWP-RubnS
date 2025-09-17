zahl = 11

# if-Abfrage

if zahl > 0 and zahl < 10:
    print("Die Zahl ist größer als Null und kleiner als Zehn.")
elif zahl == 10:
    print("Die Zahl ist Zehn.")
else:
    print("Die Zahl ist größer als Zehn.")

# for-Schleife

for i in range(zahl):
    print(i)

for i in range(5,10,2):
    print(i)

# while-Schleife

while zahl < 10:
    print(zahl)
    zahl += 1

# break

for aussen in range(12):               # äußere Schleife
    for innen in range(10):            # innere Schleife
        if innen == 4:
            print("Abbruch bei innen =", innen)
            break                      # bricht nur die innere Schleife ab
        print("Durchlauf:", innen)

    print("Nach der inneren Schleife, außen =", aussen)

# pass

for i in range(3):
    if i == 1:
        pass  # Platzhalter
    else:
        print(f"Wert: {i}")

# try-catch-finally

zahlen = [5, 0, "abc", 2]

for z in zahlen:
    try:
        print(f"Verarbeite:", z)
        result = 10 / z
    except ZeroDivisionError:
        print("Fehler: Division durch 0 nicht erlaubt!")
    except TypeError:
        print("Fehler: Falscher Datentyp, keine Zahl!")
    else:
        print("Ergebnis:", result)
    finally:
        print("Ende\n")