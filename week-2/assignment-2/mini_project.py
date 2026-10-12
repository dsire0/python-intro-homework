# Asks the user to enter a temperature in Fahrenheit
# Converts it to Celsius using the formula: celsius = (fahrenheit - 32) * 5 / 9
# Prints the result rounded to one decimal place. The example below shows the format — your input and result will differ:

# Requirements:
# Handle the conversion yourself (no built-in converter functions)
# Use an f-string for the output
# Round to exactly one decimal place

# Handle the conversion yourself (no built-in converter functions)
def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    Convert the input temperature from fahrenheit to celsius
    """
    celsius: float = (fahrenheit - 32) * 5 / 9
    return celsius


input_temp: float = float(input("Enter a temperature in Fahrenheit: "))

output_temp: float = fahrenheit_to_celsius(input_temp)

# Use an f-string for the output
# Round to exactly one decimal place
print(f"{input_temp:.1f}°F is {output_temp:.1f}°C.")

