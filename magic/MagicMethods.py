class Auto:
    def __init__(self, ps):
        self.ps = ps

    # Arithmetische Operationen
    def __add__(self, other):
        if isinstance(other, Auto):
            return self.ps + other.ps
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Auto):
            return self.ps - other.ps
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Auto):
            return self.ps * other.ps
        return NotImplemented

    # Vergleichsoperationen
    def __eq__(self, other):
        if isinstance(other, Auto):
            return self.ps == other.ps
        return False

    def __lt__(self, other):
        if isinstance(other, Auto):
            return self.ps < other.ps
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Auto):
            return self.ps > other.ps
        return NotImplemented

    # Repräsentation für die Ausgabe
    def __repr__(self):
        return f"Auto({self.ps} PS)"

a1 = Auto(50)
a2 = Auto(60)

print(f"Test Addition (50+60): {a1 + a2}")
print(f"Test Subtraktion (50-60): {a1 - a2}")
print(f"Test Multiplikation (50*60): {a1 * a2}")

print(f"Test EQ (50 == 60): {a1 == a2}")
print(f"Test LT (50 < 60): {a1 < a2}")
print(f"Test GT (50 > 60): {a1 > a2}")

try:
    print(a1 + 10)
except TypeError:
    print("Typprüfung funktioniert: Addition mit int nicht erlaubt.")