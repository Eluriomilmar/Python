#Weight converter

unit = input("Insert a unit(Kg/lbs): ")
while unit.upper() != "KG" and unit.upper() != "LBS":
    print("Insert a valid unit")
    unit = input("Insert a unit(Kg/lbs): ")
value = float(input(f"Insert amount of {unit}: "))
while isinstance(value, float) == False:
    print(f"Insert a valid amount of {unit}")
    value = float(input(f"Insert amount of {unit}: "))
if unit.upper == "KG":
    print(f"{value}Kg is approximately {round(value*2.205, 3)}lbs")
else:
    print(f"{value}lbs is approximately {round(value * 0.454, 3)}Kg")