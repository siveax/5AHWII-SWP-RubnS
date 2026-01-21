

alter = [10, 20, 60, 30, 17, 5]
status = ["minderjährig" if a <= 18 else "volljährig" for a in alter]

print(status)

#try:
#    zahl = int(input("Gib deine Zahl ein: "))
#    ergebnis = 100/zahl
#except ValueError:
#    print("Muss eine Ganzzahl sein!")
#except ZeroDivisionError:
#    print("Division durch 0 ist nicht erlaubt!")
#else:
#    print(f"Erfolgreich gerechnet. Ergebnis: {ergebnis}")
#finally:
#    print("Error-Handling beendet.")

students = [
    {"name": "Max", "grade": 2},
    {"name": "Anna", "grade": 1}
]

names = list(map(lambda s: s["name"], students))
grades_plus = list(map(lambda s: s["grade"] + 1, students))

print(names)
print(grades_plus)


numbers = [1, 2, 4]

squares = list(map(lambda x: x*x, numbers))

print(squares)


hunde = ["Bello", "Max", "Hannes", "Kotzi", "Usbeki"]
katzen = ["Miaui", "Bellina", "Simba"]

alter = [1, 6, 4, 1, 2, 4, 7]

test = list(map(lambda x: x != "Bello", hunde))

print(test)


test1 = list(filter(lambda x: x != "Bello", hunde))

print(test1)

