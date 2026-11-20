# Warmup 2: Functions that Return Values
# Write two functions:

# celsius_to_fahrenheit(c) — converts Celsius to Fahrenheit using (c * 9/5) + 32
# fahrenheit_to_celsius(f) — converts Fahrenheit to Celsius using (f - 32) * 5/9
# Call each with a few test values and print the results. Use f-strings and round to one decimal place.

# Example output — your test values and wording might differ:

# 0°C = 32.0°F
# 100°C = 212.0°F
# 72°F = 22.2°C
# Save as: warmup2.py


def celsius_to_fahrenheit(c: float) -> str:
    c_to_f: float = (c * 9 / 5) + 32
    cof: str = f"{c}°C = {c_to_f:.1f}°F"
    return cof


def fahrenheit_to_celsius(f: float) -> str:
    f_to_c: float = (f - 32) * 5 / 9
    foc: str = f"{f}°F = {f_to_c:.1f}°C"
    return foc


if __name__ == "__main__":
    print(
        celsius_to_fahrenheit(100),
        "\n",
        celsius_to_fahrenheit(-100),
        "\n",
        fahrenheit_to_celsius(100),
        "\n",
        fahrenheit_to_celsius(-100),
        sep="",
    )
