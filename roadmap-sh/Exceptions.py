# exception = An event that interrupts the flow of a program
#           1.try, 2.except, 3.finally


try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("Dividing by 0 is not possible")
except ValueError:
    print("Enter only numbers, please.")
except Exception:
    print("Something went really wrong!")
finally:
    print("Cleanup and stuff")