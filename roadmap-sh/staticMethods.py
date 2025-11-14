class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return(f"{self.name} = {self.position}")

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["MANAGER", "CASHIER", "COOK", "JANITOR"]
        return position.upper() in valid_positions


print(Employee.is_valid_position("posição"))
employee1 = Employee("Eugene", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongebob", "Cook")
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())