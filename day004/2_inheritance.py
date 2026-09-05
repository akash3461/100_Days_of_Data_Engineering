"""A few examples of inheritance and method overriding."""

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        return f"{self.name} is doing general employee work."

    def annual_salary(self):
        return self.salary * 12

    def __str__(self):
        return f"Employee(name={self.name}, salary={self.salary})"


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def work(self):
        return f"{self.name} is writing {self.programming_language} code."


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def work(self):
        return f"{self.name} is managing a team of {self.team_size} people."

    def annual_salary(self):
        base = super().annual_salary()
        return base + 50000


class SeniorDeveloper(Developer):
    def __init__(self, name, salary, programming_language, years_experience):
        super().__init__(name, salary, programming_language)
        self.years_experience = years_experience

    def work(self):
        base_work = super().work()
        return f"{base_work} ({self.years_experience} years experience)"


dev = Developer("Rohan", 60000, "Python")
mgr = Manager("Meera", 80000, 5)
senior = SeniorDeveloper("Farhan", 90000, "Java", 8)

for person in [dev, mgr, senior]:
    print(person.work())
    print(f"  Annual salary: {person.annual_salary()}")
    print()

print(dev)

print("\nIs senior a Developer?", isinstance(senior, Developer))
print("Is senior an Employee?", isinstance(senior, Employee))
print("Is mgr a Developer?", isinstance(mgr, Developer))
