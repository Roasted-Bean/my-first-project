def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            return "Error: division by zero"
        return a / b
    else:
        return "Error: unknown operator"

def main():
    print("Simple Calculator (type 'quit' to exit)")
    print("Operators: + - * /")

    while True:
        user_input = input("\nEnter expression (e.g. 5 + 3): ").strip()
        if user_input.lower() == 'quit':
            break

        parts = user_input.split()
        if len(parts) != 3:
            print("Invalid input. Use format: number operator number")
            continue

        try:
            a = float(parts[0])
            operator = parts[1]
            b = float(parts[2])
        except ValueError:
            print("Invalid numbers. Try again.")
            continue

        result = calculate(a, b, operator)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
