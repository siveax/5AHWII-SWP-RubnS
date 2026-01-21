class Tier:
    def __init__(self, name, art):
        self.name = name
        self.art = art

    def essen(self):
        print(f"Das Tier {self.name} frisst gerade.")

    def __str__(self):
        print(f"Dies ist ein {self.art} namens {self.name}.")


class Hund(Tier):
    def __init__(self, name, rasse):
        super().__init__(name, art="Hund")
        self.rasse = rasse

    def bellen(self):
        print(f"{self.name} sagt: Wuff! Wuff!")
        super()  # Nutzt eine Methode der Oberklasse


class Katze(Tier):
    def __init__(self, name, farbe):
        super().__init__(name, art="Katze")
        self.farbe = farbe

    def miauen(self):
        print(f"{self.name} sagt: Miau!")
        # Hier nutzen wir direkt ein Attribut der Oberklasse
        print(f"Diese {self.farbe} Katze hat Hunger.")


# Objekte erzeugen
mein_hund = Hund("Bello", "Labrador")
meine_katze = Katze("Luna", "getigert")

# Methoden testen
mein_hund.bellen()
mein_hund.essen()  # Geerbte Methode von Tier

print("---")

meine_katze.miauen()
meine_katze()  # Geerbte Methode von Tier