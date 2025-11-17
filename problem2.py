"""
Problem 2: Temperature Converter
Convert between Celsius and Fahrenheit temperatures.
"""

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius*9/5 + 32
    return fahrenheit


    """
    Convert Celsius to Fahrenheit.
    Formula: F = (C × 9/5) + 32

    Args:
        celsius (float): Temperature in Celsius

    Returns:
        float: Temperature in Fahrenheit
    """
    # TODO: Implement this function
    pass


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
    """
    Convert Fahrenheit to Celsius.
    Formula: C = (F - 32) × 5/9

    Args:
        fahrenheit (float): Temperature in Fahrenheit

    Returns:
        float: Temperature in Celsius
    """
    # TODO: Implement this function
    pass


def temperature_converter():
    temp = float(input("Enter temperature value: "))
    unit = input("Enter current unit (C/F): ").strip().upper()
    if unit == 'C':
        converted = celsius_to_fahrenheit(temp)
        print(f"{temp}°C is {converted:.2f}°F")
    elif unit == 'F':
        converted = fahrenheit_to_celsius(temp)
        print(f"{temp}°F is {converted:.2f}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    """
    Interactive temperature converter.
    Ask user for:
    1. Temperature value
    2. Current unit (C or F)
    3. Convert and display result
    """
    print("Temperature Converter")
    print("-" * 30)

    # TODO: Implement the interactive converter
    # Remember to:
    # - Get temperature value from user
    # - Get unit (C or F) from user
    # - Validate input
    # - Perform conversion
    # - Display result rounded to 2 decimal places
    pass


# Test cases (DO NOT MODIFY)
if __name__ == "__main__":
    # Test conversions
    print("Running tests...")

    # Test Celsius to Fahrenheit
    assert celsius_to_fahrenheit(0) == 32, "0°C should be 32°F"
    assert celsius_to_fahrenheit(100) == 212, "100°C should be 212°F"

    # Test Fahrenheit to Celsius
    assert fahrenheit_to_celsius(32) == 0, "32°F should be 0°C"
    assert fahrenheit_to_celsius(212) == 100, "212°F should be 100°C"

    print("All tests passed!")
    print()

    # Run interactive converter
    temperature_converter()