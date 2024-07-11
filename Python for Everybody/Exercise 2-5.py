"""Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature."""


print("Neste programa, convertiremos a temperatura de °C para °F")
C = float(input("Insira a temperatura em °C: "))
F = (C * 9/5) + 32
print(f"A temperatura em Farenheit é de: {F}°F")