def read_numbers_from_file(file_path):
    """Read numbers from a file and return a list of integers."""
    numbers = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    number = int(line.strip())
                    numbers.append(number)
                except ValueError:
                    print(f"Invalid number found: {line.strip()} - Skipping.")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    return numbers


def calculate_sum(numbers):
    """Calculate the sum of a list of numbers."""
    return sum(numbers)


def write_result_to_file(file_path, result):
    """Write the result to a file."""
    try:
        with open(file_path, 'w') as file:
            file.write(f"The sum of the numbers is: {result}\n")
    except IOError as e:
        print(f"Error writing to file '{file_path}': {e}")


def main(input_file, output_file):
    numbers = read_numbers_from_file(input_file)
    if numbers:
        result = calculate_sum(numbers)
        write_result_to_file(output_file, result)
        print(f"Result written to '{output_file}'")
    else:
        print("No valid numbers to process.")


# Example usage
input_file = 'input.txt'
output_file = 'output.txt'
main(input_file, output_file)
