class ComprehensionExamples:
    def __init__(self):
        """
        Constructor of the class.
        Step 1: Create a list of random ages.
        """
        self.ages = [12, 17, 18, 21, 25, 30, 40]

    def list_comprehension(self):
        """
        Example 1: List Comprehension
        Step 1: Select only adults (age >= 18).
        Step 2: Create a list of their ages.
        Step 3: Calculate what percentage are adults.
        """
        adults = [age for age in self.ages if age >= 18]
        percent_adults = (len(adults) / len(self.ages)) * 100

        print("List Comprehension Example:")
        print(f"Adults (>=18): {adults}")
        print(f"Adults make up {percent_adults:.2f}% of all people.\n")

    def set_comprehension(self):
        """
        Example 2: Set Comprehension
        Step 1: Get the first letter of each name.
        Step 2: Store only unique first letters (Set removes duplicates).
        Step 3: Calculate the percentage of unique first letters.
        """
        names = ["Anna", "Ben", "Bella", "Chris", "Clara", "David" "Daniel"]
        first_letters = {name[0] for name in names}
        percent_unique = (len(first_letters) / len(names)) * 100

        print("Set Comprehension Example:")
        print(f"Unique first letters: {first_letters}")
        print(f"Unique letters make up {percent_unique:.2f}% of all names.\n")

    def dict_comprehension(self):
        """
        Example 3: Dictionary Comprehension
        Step 1: Create a dictionary with products and prices.
        Step 2: Add 20% tax to each price.
        Step 3: Calculate how much percent the average price increased.
        """
        prices = {"apple": 1.0, "banana": 1.5, "cherry": 2.0}
        prices_with_tax = {item: price * 1.2 for item, price in prices.items()}

        avg_old = sum(prices.values()) / len(prices)
        avg_new = sum(prices_with_tax.values()) / len(prices_with_tax)
        percent_increase = ((avg_new - avg_old) / avg_old) * 100

        print("Dictionary Comprehension Example:")
        print(f"Old prices: {prices}")
        print(f"Prices with tax: {prices_with_tax}")
        print(f"Average price increased by {percent_increase:.2f}%.\n")


def main():
    """
    Main function.
    Step 1: Create the class object.
    Step 2: Call all comprehension examples.
    """
    example = ComprehensionExamples()
    example.list_comprehension()
    example.set_comprehension()
    example.dict_comprehension()


# Run the program
if __name__ == "__main__":
    main()