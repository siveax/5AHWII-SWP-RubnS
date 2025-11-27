import random

def fill_list(anz):
    jahreseinkommen = []

    if anz <= 0:
        return None

    for _ in range(anz):
        jahreseinkommen.append(random.randint(5000, 100000))

    return jahreseinkommen

def berechne_steuer(jahreseinkommen: list[int]):
    steuern = {}

    for e in jahreseinkommen:
        if e <= 10000:
            steuern[e] = e*0.4 # berechnet die Steuern
        elif 10000 < e <= 30000:
            steuern[e] = e*0.55
        elif 30000 < e <= 70000:
            steuern[e] = e*0.75
        else:
            steuern[e] = e*0.82

    return steuern

def berechne_gruppen(jahreseinkommen):
    anz_steuerzahler = {}

    for e in jahreseinkommen:
        if e <= 10000:
            anz_steuerzahler["<= 10000"] = anz_steuerzahler.get("<= 10000", 0) + 1
        elif 10000 < e < 30000:
            anz_steuerzahler["10000 < e < 30000"] = anz_steuerzahler.get("10000 < e < 30000", 0) + 1
        elif 30000 < e <= 70000:
            anz_steuerzahler["30000 < e <= 70000"] = anz_steuerzahler.get("30000 < e <= 70000", 0) +1
        else:
            anz_steuerzahler["> 70000"] = anz_steuerzahler.get("> 70000", 0) + 1

    return anz_steuerzahler

def main():
    einkommen = fill_list(1000)
    print("Zufällige Jahreseinkommen: " + str(einkommen))

    steuern = berechne_steuer(einkommen)
    print("Jahreseinkommen | Steuern")
    for n in steuern:
        print(f"{n:15.2f} | {steuern[n]:.2f}")

    gruppen = berechne_gruppen(einkommen)
    print("\nEinkommenssteuergruppe | Anzahl der Steuerzahler")
    for n in gruppen:
        print(f"{n:<22} | {gruppen[n]:<22}")

if __name__ == "__main__":
    main()