def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    
    Args:
    - celsius (float): Temperature in Celsius
    
    Returns:
    - float: Temperature in Fahrenheit
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Example usage:
celsius_temperature = 25
fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)
print(f"{celsius_temperature} degrees Celsius is equal to {fahrenheit_temperature} degrees Fahrenheit.")
