"""Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature."""

def temp():
    try:
        C = float(input("Insira a temperatura em °C: "))
    except:
        print("Somente são aceitos números.")
        return temp()
    else:
        return C

C = temp()
print("Neste programa, convertiremos a temperatura de °C para °F")
F = (C * 9/5) + 32
print(f"A temperatura em Farenheit é de: {F}°F")