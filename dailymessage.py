
class DailyMessage:
    def __init__(self):
        self.message = ""

    def get_message(self):
        self.message = input("Enter your daily message: ")

    def print_message(self):
        print("Your message:", self.message.upper())


class HelperSession:
    def __init__(self):
        print("Helper session has started.")

    def __del__(self):
        print("Helper session has ended.")


def create_session():
    session = HelperSession()
    return session


class PairFinder:
    def find_pair(self, numbers, target):
        for i, number in enumerate(numbers):
            for j, next_number in enumerate(numbers):
                if i < j and number + next_number == target:
                    print("Pair found!")
                    print("Numbers:", number, "and", next_number)
                    print("Indexes:", i, "and", j)
                    return

        print("No pair found that adds up to", target)


# Main program

# Step 3: Create a DailyMessage object
daily_text = DailyMessage()
daily_text.get_message()
daily_text.print_message()

print()

# Step 5: Create a HelperSession object using the function
session = create_session()

print()

# Step 6 and 7: Find a pair of numbers
numbers = [10, 20, 30, 40, 50, 60, 70]
target = int(input("Enter the target sum (e.g. 90 or 100): "))

finder = PairFinder()
finder.find_pair(numbers, target)

print()

# Delete the session object
del session


