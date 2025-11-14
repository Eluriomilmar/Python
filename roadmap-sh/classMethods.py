class Student:

    count = 0
    tot_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.tot_gpa += gpa


    #Instance method
    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"

    @classmethod
    def get_avg_gpa(cls):
        if cls.count == 0:
            return f"0"
        else:
            return f"Avg GPA: {cls.tot_gpa / cls.count:.2f}"

print(Student.get_count())

student1 = Student("Spongebob", 3.2)
student2 = Student("Naami", 4)
student3 = Student("Patrick", 2)

print(Student.get_count())
print(Student.get_avg_gpa())