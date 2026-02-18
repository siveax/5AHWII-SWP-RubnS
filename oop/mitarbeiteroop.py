class Person:
    def __init__(self, name, geschlecht):
        self.name = name
        self.geschlecht = geschlecht  # 'm' oder 'w'

    def __str__(self):
        return f"{self.name} ({self.geschlecht})"

class Mitarbeiter(Person):
    def __init__(self, name, geschlecht, abteilung):
        super().__init__(name, geschlecht)
        self.abteilung = abteilung
        abteilung.mitarbeiter_hinzufuegen(self)

    def __str__(self):
        return f"Mitarbeiter: {self.name} ({self.geschlecht}) - {self.abteilung.name}"

class Abteilungsleiter(Mitarbeiter):
    def __init__(self, name, geschlecht, abteilung):
        super().__init__(name, geschlecht, abteilung)
        abteilung.leiter_setzen(self)

    def __str__(self):
        return f"Abteilungsleiter: {self.name} ({self.geschlecht}) - {self.abteilung.name}"

class Abteilung:
    def __init__(self, name):
        self.name = name
        self.mitarbeiter = []
        self.leiter = None


    def mitarbeiter_hinzufuegen(self, mitarbeiter):
        self.mitarbeiter.append(mitarbeiter)

    def leiter_setzen(self, leiter):
        if self.leiter is not None:
            raise ValueError(f"Abteilung {self.name} hat bereits einen Leiter!")
        self.leiter = leiter

    def anzahl_mitarbeiter(self):
        return len(self.mitarbeiter)

    def __str__(self):
        leiter_name = self.leiter.name if self.leiter else "kein Leiter"
        return f"Abteilung {self.name}: {len(self.mitarbeiter)} Mitarbeiter, Leiter: {leiter_name}"

class Firma:
    def __init__(self, name):
        self.name = name
        self.abteilungen = []

    def abteilung_hinzufuegen(self, abteilung):
        self.abteilungen.append(abteilung)

    def anzahl_mitarbeiter(self):
        gesamt = 0
        for abt in self.abteilungen:
            gesamt += abt.anzahl_mitarbeiter()
        return gesamt

    def anzahl_abteilungsleiter(self):
        anzahl = 0
        for abt in self.abteilungen:
            if abt.leiter is not None:
                anzahl += 1
        return anzahl

    def anzahl_abteilungen(self):
        return len(self.abteilungen)

    def groesste_abteilung(self):
        if not self.abteilungen:
            return None
        groesste = self.abteilungen[0]
        for abt in self.abteilungen:
            if abt.anzahl_mitarbeiter() > groesste.anzahl_mitarbeiter():
                groesste = abt

        return groesste

    def geschlechterverteilung(self):
        alle_mitarbeiter = []
        for abt in self.abteilungen:
            for mitarbeiter in abt.mitarbeiter:
                alle_mitarbeiter.append(mitarbeiter)

        if len(alle_mitarbeiter) == 0:
            return 0.0, 0.0

        frauen = 0
        for m in alle_mitarbeiter:
            if m.geschlecht == 'w':
                frauen += 1

        maenner = 0
        for m in alle_mitarbeiter:
            if m.geschlecht == 'm':
                maenner += 1

        gesamt = len(alle_mitarbeiter)
        frauen_prozent = (frauen / gesamt) * 100
        maenner_prozent = (maenner / gesamt) * 100

        return frauen_prozent, maenner_prozent

    def __str__(self):
        return f"Firma {self.name}: {self.anzahl_abteilungen()} Abteilungen, {self.anzahl_mitarbeiter()} Mitarbeiter"

def main():
    firma = Firma("HTL GmbH")

    wi_abteilung = Abteilung("Wirtschaft")
    it_abteilung = Abteilung("IT")
    bio_abteilung = Abteilung("Biomedizin")

    firma.abteilung_hinzufuegen(wi_abteilung)
    firma.abteilung_hinzufuegen(it_abteilung)
    firma.abteilung_hinzufuegen(bio_abteilung)

    leiter_wi = Abteilungsleiter("Andreas Reimair", "m", wi_abteilung)
    leiter_it = Abteilungsleiter("Enese Duyar", "w", it_abteilung)
    leiter_bio = Abteilungsleiter("Martin Huber", "m", bio_abteilung)

    Mitarbeiter("Tim Hoepman", "m", wi_abteilung)
    Mitarbeiter("Raphaela Annewanter", "w", it_abteilung)
    Mitarbeiter("Felicitas Schett", "w", it_abteilung)
    Mitarbeiter("Nathan Lenz", "m", bio_abteilung)

    print(f"{firma}")

    print("Statistiken:")
    print(f"- Mitarbeiter gesamt: {firma.anzahl_mitarbeiter()}")
    print(f"- Abteilungsleiter: {firma.anzahl_abteilungsleiter()}")
    print(f"- Abteilungen: {firma.anzahl_abteilungen()}")

    groesste = firma.groesste_abteilung()
    print(f"- Größte Abteilung: {groesste.name} ({groesste.anzahl_mitarbeiter()} Mitarbeiter)")

    frauen_prozent, maenner_prozent = firma.geschlechterverteilung()
    print(f"- Frauen: {frauen_prozent:.1f}% | Männer: {maenner_prozent:.1f}%\n")

if __name__ == "__main__":
    main()