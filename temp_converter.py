
""" Temperature converter.

"""

def celsius_input() -> float:
    temp_celsius: float = float(input("Enter temperature in Celsius: "))
    return temp_celsius

def fahrenheit_conversion(temp_celsius: float) -> float:
    temp_fahrenheit: float = (temp_celsius * 9/5) + 32
    return temp_fahrenheit

def print_results (temp_c: float, temp_f: float) -> None:
    print(f"{temp_c} degrees Celsius is equal to {temp_f} degrees Fahrenheit.")

def temp_conversion():
    celsius: float = celsius_input()
    fahrenheit: float = fahrenheit_conversion(celsius)
    print_results(celsius, fahrenheit)

if __name__=="__main__":
    temp_conversion()