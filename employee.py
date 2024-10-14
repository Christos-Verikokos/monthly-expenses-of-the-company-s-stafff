from abc import ABC

class Employees:
    def __init__(self, employees):
        self.employees = employees
        self.number = 1

    def total_expenses(self):
        expenses = 0
        for employee in self.employees:
            expenses += employee.total_salary()
        return expenses

    def average_expenses(self):
        avg_exp = 0
        for employee in self.employees:
            avg_exp += employee.total_salary()
        return avg_exp / len(self.employees)


class Employee(ABC):
    # Abstract class that contain common features about other classes.
    def __init__(self,first_name, last_name, position, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.salary = salary

    # Method to give the employee a raise
    def give_raise(self, amount):
        self.salary += amount
        print(f"{self.first_name} {self.last_name} has been given a raise of {amount}. New salary is {self.salary}")

class SalariedWorker(Employee):
    # A class about salaried worker
    def __init__(self, first_name, last_name, position, salary, level):
        super().__init__( first_name, last_name, position, salary)
        self.level = level
        self.level_increment = {'Director': 500,
                                'Lead': 350,
                                'Senior': 200,
                                'Mid': 100,
                                'Junior':0,
                                }

    def total_salary(self):
        return self.salary + self.level_increment[self.level]

    def display_info(self):
        total_salary = self.salary + self.level_increment[self.level]
        return (self.first_name.title(), self.last_name.title(), self.position, f"Salaried worker-{self.level}",
                self.salary, f"+{self.level_increment[self.level]} {self.level} ","", self.total_salary())

class FreelancerEmployee(Employee):
    # A class about freelancer
    def  __init__(self,first_name, last_name, position, salary, salary_per_overtime, overtime):
        super().__init__(first_name, last_name, position, salary)
        self.salary_per_overtime = salary_per_overtime
        self.overtime = overtime

    def overtime_increment(self):
         if not self.overtime:
            overtime = 0
         return self.salary_per_overtime * self.overtime

    def total_salary(self):
        return self.overtime_increment() + self.salary

    def display_info(self):
        return (self.first_name.title(), self.last_name.title(), self.position, "Freelancer",
                self.salary, "", f"+{self.overtime_increment()} = {self.salary_per_overtime} * {self.overtime}",
                self.total_salary())

class StudentEmployee(Employee):
    # A class about students that they do training
    def __init__(self, first_name, last_name, position, salary, age):
        super().__init__(first_name, last_name, position, salary)
        self.age = age

    def total_salary(self):
        if self.age >= 25:
            self.salary = 700
            return 700
        else:
            self.salary = 600
            return 600

    def display_info(self):
        return (self.first_name.title(), self.last_name.title(), self.position, "Training work",
                self.total_salary(), "", "",self.total_salary())

