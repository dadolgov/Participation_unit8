
""" Temperature converter.
Converts Celsius into Fahrehnheit using several functions
celsius_input: saves user temperature input and converts it to float
fahrenheit_conversion: converts Celsius temperature into Fahrenheit
print_results: prints out initial and converted temperatures in a single sentence
temp_conversion: orcestrator function, uses all the functions above

Author: Dmitrii Dolgov
3/8/2026
"""

def celsius_input() -> float:
    """takes temperature in Ceslius and saves it as a float type

    Returns:
        float: temperature in Celsius
    """
    temp_celsius: float = float(input("Enter temperature in Celsius: "))
    return temp_celsius

def fahrenheit_conversion(temp_celsius: float) -> float:
    """takes temperature in Celsius and converts it to Fahrenheit

    Args:
        temp_celsius (float): temperature in Celsius

    Returns:
        float: temperature in Fahrenheit
    """
    temp_fahrenheit: float = (temp_celsius * 9/5) + 32
    return temp_fahrenheit

def print_results (temp_c: float, temp_f: float) -> None:
    """Prints initial temperature and conversion results in a single sentence

    Args:
        temp_c (float): Celsius temperature
        temp_f (float): Fahrenheit temperature
    """
    print(f"{temp_c} degrees Celsius is equal to {temp_f} degrees Fahrenheit.")

def temp_conversion() -> None:
    """Converts Celsius to Fahrenheit degrees and prints out the result.
    """
    celsius: float = celsius_input()
    fahrenheit: float = fahrenheit_conversion(celsius)
    print_results(celsius, fahrenheit)

# program starts here
if __name__=="__main__":
    temp_conversion()