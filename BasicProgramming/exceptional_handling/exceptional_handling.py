def divide_numbers():
    try:
        # Get user input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform division
        result = num1 / num2

    except ZeroDivisionError:
        # Handle division by zero
        print("Error: Cannot divide by zero.")
    except ValueError:
        # Handle invalid input
        print("Error: Invalid input. Please enter numeric values.")
    else:
        # If no exception occurs
        print(f"The result is: {result}")
    finally:
        # Code that runs no matter what
        print("Division operation completed.")


# Example usage
divide_numbers()
