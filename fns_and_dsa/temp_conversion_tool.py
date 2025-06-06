# temp_conversion_tool.py

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    temp_input = input("Enter the temperature (e.g., 100F or 37C): ").strip()

    try:
        if temp_input[-1].upper() == 'F':
            temp_value = float(temp_input[:-1])
            celsius = convert_to_celsius(temp_value)
            print(f"{temp_value}°F is {round(celsius, 2)}°C")
        elif temp_input[-1].upper() == 'C':
            temp_value = float(temp_input[:-1])
            fahrenheit = convert_to_fahrenheit(temp_value)
            print(f"{temp_value}°C is {round(fahrenheit, 2)}°F")
        else:
            raise ValueError("Invalid temperature unit. Please use 'C' or 'F'.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
