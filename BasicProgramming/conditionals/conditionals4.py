def generate_fibonacci(num):
    if num <= 1:
        return num
    else:
        return generate_fibonacci(num - 1) + generate_fibonacci(num - 2)


def print_fibonacci_series():
    number_input = int(input("Enter the number up to which you want to generate the fibonacci series "))
    fib_list = [generate_fibonacci(i) for i in range(number_input)]
    print(fib_list)


print_fibonacci_series()
