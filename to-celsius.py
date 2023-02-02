# Temperature conversion from Fahrenheit to Celsius

fahrenheit = float(input("What temperature (in fahrenheit) would you like converted to Celsius? "))
celsius = (fahrenheit - 32) * 5 / 9 

print(fahrenheit, "F is", round(celsius, 2), "C")