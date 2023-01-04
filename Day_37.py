# Raising Custom errors

# In python, we can raise custom errors by using the raise keyword.

# Defining Custom Exceptions

# In Python, we can define custom exceptions by creating a new class that is derived from the built-in Exception class.

class InvalidEnteredNumber(Exception):
    """Exception raised for errors .
    """

    def __init__(self, message="Value should be between 10 and 20"):
        self.message = message
        super().__init__(self.message)




# a = int(input("Enter any value between 5 and 9:     "))
#
# if (a < 5 or a > 9):
#     raise ValueError("Value should be between 5 and 9")

b = int(input("Enter any value between 10 and 20:     "))

if (b < 10 or b > 20):
    raise InvalidEnteredNumber
