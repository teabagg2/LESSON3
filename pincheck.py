class Account:
    def __init__(self, owner, pin):
        self.owner = owner
        self.__pin = pin

    def show_pin_status(self):
        print(f"PIN is set: {self.__pin is not None}")

    def check_pin(self, guess):
        return self.__pin == guess

    def set_pin(self, new_pin):
        if len(new_pin) == 4 and new_pin.isdigit():
            self.__pin = new_pin
            print("PIN updated successfully.")
        else:
            print("Error: PIN must be exactly four digits.")

    def __str__(self):
        return f"Account owner: {self.owner}, PIN is hidden for safety."


my_account = Account("Tehilla", "1234")
print(my_account)

my_account.__pin = "9999"
print(my_account.check_pin("9999"))
print(my_account.check_pin("1234"))

my_account.set_pin("9999")
print(my_account.check_pin("9999"))
print(my_account.check_pin("1234"))

my_account.set_pin("99")
my_account.set_pin("abcd")