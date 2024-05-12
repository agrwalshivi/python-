# Define custom exception class
class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def validate_age(age):
    if age < 0:
        raise CustomError("Age cannot be negative.")
    elif age < 18:
        raise CustomError("You must be 18 or older.")

def main():
    try:
        age = int(input("Enter your age: "))
        validate_age(age)
        print("Age is valid.")
    except ValueError:
        print("Please enter a valid integer for age.")
    except CustomError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
