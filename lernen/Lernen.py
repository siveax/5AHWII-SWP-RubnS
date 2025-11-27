import random
import array as arr

statistics = {}

for i in range(1, 46):
    statistics[i] = 0

print(statistics)

def draw_lotto_numbers():

    numbers = arr.array("i", range(1, 46))

    print(f"Gesamte Liste: {numbers}")

    for i in range(6):
        pos = random.randint(0, 44 - i)
        temp = numbers[pos]
        numbers[pos] = numbers[44-i]
        numbers[44-i] = temp

    print(f"Neue Liste: {numbers}")

    drawn: list[int] = list(numbers[-6:])

    print(f"Gezogene Zahlen: {drawn}")

    return drawn

def update_statistics(drawn):
    for num in drawn:
        statistics[num] += 1


def run_statistics(num_draws):

    for _ in range(num_draws):
        update_statistics(draw_lotto_numbers())

    print("")
    print(f"Statistiken nach {num_draws} Ziehungen:")
    print("Zahl | Anzahl | Prozentual")
    for num in range(1, 46):
        count = statistics[num]
        perc = (count / (num_draws * 6)) * 100
        print(f"{num:4d} | {count:6d} |  {perc:9.2f}% ")

def main():
    run_statistics(100000)

if __name__ == "__main__":
    main()
