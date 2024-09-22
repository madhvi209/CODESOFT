import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def exponentiate(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error! Cannot take the square root of a negative number."
    return math.sqrt(x)

def calculate(equation):
    try:
        # Replace '^' with '**' for exponentiation
        equation = equation.replace('^', '**')
        result = eval(equation)
        return result
    except Exception as e:
        return f"Error! {str(e)}"

def main():
    print("Welcome to the Advanced Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiate (x^y)")
    print("6. Square Root (sqrt(x))")
    print("7. Evaluate an expression (e.g., 2 + 3 * (5 - 1))")

    while True:
        choice = input("Enter choice (1/2/3/4/5/6/7) or 'q' to quit: ")

        if choice == 'q':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5', '6']:
            if choice in ['1', '2', '3', '4', '5']:
                num1 = float(input("Enter first number: "))
                if choice in ['1', '2', '3', '4']:
                    num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
                elif choice == '5':
                    print(f"{num1} ^ {num2} = {exponentiate(num1, num2)}")
            elif choice == '6':
                num1 = float(input("Enter the number for square root: "))
                print(f"sqrt({num1}) = {square_root(num1)}")

        elif choice == '7':
            equation = input("Enter an expression (e.g., 2 + 3 * (5 - 1)): ")
            print(f"Result: {calculate(equation)}")
        else:
            print("Invalid input! Please enter a valid choice.")

if __name__ == "__main__":
    main()
