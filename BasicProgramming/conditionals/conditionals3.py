def triangle_type(side1, side2, side3):
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        if side1 == side2 == side3:
            return "Equilateral"
        elif side1 == side2 or side1 == side3 or side2 == side3:
            return "Isosceles"
        else:
            return "Scalene"
    else:
        return "Not a triangle"


def main():
    print("Triangle Type Checker")

    # Get the lengths of the triangle sides from the user
    try:
        side1 = float(input("Enter the length of the first side: "))
        side2 = float(input("Enter the length of the second side: "))
        side3 = float(input("Enter the length of the third side: "))
        result = triangle_type(side1, side2, side3)
        print(f"The triangle is: {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values for the sides.")


if __name__ == "__main__":
    main()
