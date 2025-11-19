import random
import array as arr

class Lotto:

    def __init__(self):
        """
        Initialize the Lotto class.
        Create a dictionary to count how often each number is drawn.
        """
        self.statistics = {}
        for number in range(1, 46):
            self.statistics[number] = 0

    def draw_lotto_numbers(self, show_output=False):
        """
        Draw 6 random lotto numbers from 1 to 45 without repetition.
        Returns a list of 6 drawn numbers.
        """
        numbers = arr.array("i", range(1, 46))  # create array 1–45

        # draw 6 numbers by swapping random positions to the end
        for i in range(6):
            pos = random.randint(0, 44 - i)
            temp = numbers[pos]
            numbers[pos] = numbers[44 - i]
            numbers[44 - i] = temp

        # take the last 6 numbers as drawn
        drawn = numbers[-6:]

        if show_output:
            print(f"Drawn numbers: {drawn}")

        return drawn

    def update_statistics(self, drawn):
        """
        Update the statistics dictionary by increasing the count for each drawn number.
        """
        for num in drawn:
            self.statistics[num] += 1

    def run_statistics(self, num_draws):
        """
        Perform several draws and print how often each number appeared and its percentage.
        """
        for _ in range(num_draws):
            drawn = self.draw_lotto_numbers()
            self.update_statistics(drawn)

        print()
        print(f"Statistics after {num_draws} draws:")
        # Print header
        print("Number | Count | Percentage")
        print("-" * 29)
        for num in range(1, 46):
            count = self.statistics[num]
            percentage = (count / (num_draws * 6)) * 100
            print(f"{num:6d} | {count:5d} | {percentage:9.2f}%")
        print()

def main():
    # create a Lotto game
    game = Lotto()

    # show one single draw first
    game.draw_lotto_numbers(show_output=True)

    # ask how many draws for statistics
    num_draws = int(input("Enter how many draws you want to simulate: "))

    # run the statistics
    game.run_statistics(num_draws)

if __name__ == "__main__":
    main()
