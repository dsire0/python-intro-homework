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


def celsius_to_fahrenheit(c: float) -> float:
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32) * 5 / 9


if __name__ == "__main__":
    for c in (0, 100, -100):
        print(f"{c:.1f}°C = {celsius_to_fahrenheit(c):.1f}°F")

    for f in (72, 100, -100):
        print(f"{f:.1f}°F = {fahrenheit_to_celsius(f):.1f}°C")
