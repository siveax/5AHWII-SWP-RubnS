import sys

def fehlwerte_filtern(datenliste):

    bereinigte_liste = []
    fehler_count = 0

    for temp in datenliste:
        if -60 <= temp <= 60:
            bereinigte_liste.append(temp)
        else:
            fehler_count += 1

    return bereinigte_liste, fehler_count

def calc_durchschnitt(datenliste):

    if not datenliste:
        return "Datenliste ist nicht leer"

    summe = sum(datenliste)
    anzahl = len(datenliste)

    return summe/anzahl

def main():
    temp = [-7, -6, -4, -103, -2, 0, 68, 2, 3, -81, 4, 76]
    bereinigte_liste, fehler_count = fehlwerte_filtern(temp)
    print(f"Bereinigte Liste: {bereinigte_liste}")
    print(f"Fehleranzahl: {fehler_count}")

    avg = calc_durchschnitt(bereinigte_liste)
    print(f"Durchschnittswert: {avg}")


if __name__ == "__main__":
    try:
        main()
    except:
        print("Fehler")
        sys.exit(1)