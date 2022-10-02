from multiprocessing import managers


class Employee:
    def __init__(self, name, age, salary, employment_years):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_years = employment_years

    def __str__(self):
        return f"name: {self.name}, age: {self.age}, years: {self.employment_years}, salary: {self.salary}"

    def get_annual_salary(self, salary):
        return salary * 12




   
# emp_1 = Employee("Jaber", 25, 1200, 5)
# print(emp_1)






class Manager(Employee):
    def __init__(self, name, age, salary, employment_years, bonus_percentage):
        super().__init__(name, age, salary, employment_years)
        self.bonus_percentage = bonus_percentage

    def __str__(self):
        return f" name: {self.name}, age: {self.age}, years: {self.employment_years}, salary: {self.salary}"

    def get_bonus(self, salary):
        return self.bonus_percentage * salary


# manager_1 = Manager("Ahmad", 40, 3000, 15, 0.5)
# print(manager_1)

# def list_of_employees():
#     employee_1 = Employee("Ali", 30, 1300, 5)
#     employee_2 = Employee("Haneen", 25, 1500, 10)
#     employee_3 = Employee("Abdullah", 35, 2000, 15) 


# def list_of_managers():
#     manager_1 = Manager("Ahmad", 40, 3000, 15, 0.5)

def main():

    while True:
        employee_1 = Employee("Ali", 30, 1300, 5)
        employee_2 = Employee("Haneen", 25, 1500, 10)
        employee_3 = Employee("Abdullah", 35, 2000, 15)
        manager_1 = Manager("Ahmad", 40, 3000, 15, 0.5)

        print("Welcome to HR Pro")
        print("Options: 1- Show Employees, 2- Show Managers, 3- Add An Employee, 4- Add A Manager, 5-Exit")
        select = int(input("What would you like to do: "))

        if select == 1:
            print(f"employees: {employee_1} - {employee_2} - {employee_3}")

        elif select == 2:
            print(f"mangers: {manager_1}")

        elif select == 3:
            print(f"Add An Employee...")

        elif select == 4:
            print(f"Add A Manager....")
        else:
            select = 5
            return True


 






if __name__ == '__main__':
	main()
