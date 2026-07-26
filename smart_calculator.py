import math

def smart_calculator():
    # Print the welcome message
    print("Welcome to Smart Calculator")
    print("Available list of operators: +, -, *, /, // (integer division), % (modulus), ** (power)")
    print(" sqrt → Square Root (only first number used)")
    print(" abs → Absolute Value (only first number used)")
    print(" inv → Additive Inverse (only first number used)")
    print(" currency → Convert currencies")
    print(" history → Show all past results")
    print("Type 'stop' anytime to exit.\n")

    history = []
    # Static exchange rates for currency conversion, updated as of late July 2026.
    # These are fixed values for demo purposes, not a live feed, so they will
    # drift out of date over time. For production use, this should call a
    # live exchange-rate API instead.
    rates = {
        "USD": {"USD": 1, "EUR": 0.8790, "GBP": 0.7477, "QAR": 3.6455},
        "EUR": {"USD": 1.1377, "EUR": 1, "GBP": 0.8506, "QAR": 4.1480},
        "GBP": {"USD": 1.3374, "EUR": 1.1755, "GBP": 1, "QAR": 4.8760},
        "QAR": {"USD": 0.2743, "EUR": 0.2411, "GBP": 0.2051, "QAR": 1}
    }

    # Main loop to keep the calculator running
    while True:
        # Get the operator choice from the user
        operator_choice = input(
            "Choose an operator (+, -, *, /, //, %, **, sqrt, abs, inv, currency, history): "
        ).strip()

        # Check if the user wants to stop
        if operator_choice.lower() == "stop":
            print("Calculator shutting off. Goodbye!")
            break

        # If choice is history, display the list of previous results
        if operator_choice == "history":
            if history:
                print("Calculation History:")
                for index, result in enumerate(history, 1):
                    print(f"{index}: {result}")
            else:
                print("No calculations yet.")
            continue

        # Logic for single-number operations (sqrt, abs, inv)
        if operator_choice in ["sqrt", "abs", "inv"]:
            try:
                num = float(input("Enter a number: "))
                if operator_choice == "sqrt":
                    result = math.sqrt(num)
                elif operator_choice == "abs":
                    result = abs(num)
                else:  # inv
                    result = -num
                print(f"Result: {result}\n")
                history.append(result)
            except ValueError:
                print("Invalid input. Please enter numbers only.\n")
            continue

        # Logic for currency conversion
        if operator_choice == "currency":
            try:
                amount = float(input("Enter amount: "))
                from_currency = input("From currency (USD, EUR, GBP, QAR): ").strip().upper()
                to_currency = input("To currency (USD, EUR, GBP, QAR): ").strip().upper()

                # Check if currencies exist in the rates dictionary
                if from_currency not in rates or to_currency not in rates[from_currency]:
                    print("Invalid currency choice!\n")
                    continue

                result = amount * rates[from_currency][to_currency]
                print(f"Converted Amount: {result:.2f} {to_currency}\n")
                history.append(result)
            except ValueError:
                print("Invalid input. Please enter numbers only.\n")
            continue

        # Validate if the choice is a standard math operator
        if operator_choice not in ["+", "-", "*", "/", "//", "%", "**"]:
            print("Invalid operator. Try again!\n")
            continue

        # Logic for multi-number calculations
        try:
            numbers = input("Enter numbers separated by spaces: ").split()
            numbers = [float(num) for num in numbers]

            # Ensure the user provided at least two numbers for these operators
            if len(numbers) < 2:
                print("Please enter at least two numbers!\n")
                continue

            result = numbers[0]
            # Loop through numbers and apply the chosen operator sequentially
            for num in numbers[1:]:
                if operator_choice == "+":
                    result += num
                elif operator_choice == "-":
                    result -= num
                elif operator_choice == "*":
                    result *= num
                elif operator_choice == "/":
                    if num == 0:
                        print("Error: Division by zero!\n")
                        break  # Exit the for loop on division by zero
                    result /= num
                elif operator_choice == "//":
                    if num == 0:
                        print("Error: Division by zero!\n")
                        break
                    result //= num
                elif operator_choice == "%":
                    if num == 0:
                        print("Error: Division by zero!\n")
                        break
                    result %= num
                elif operator_choice == "**":
                    result **= num
            else:
                # This block runs only if the for loop completed without a 'break'
                print(f"Result: {result}\n")
                history.append(result)

        except ValueError:
            print("Invalid input. Please enter numbers only.\n")


# Run the calculator
smart_calculator()
