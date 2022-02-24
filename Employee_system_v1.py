def input_invalid_int():
    print("\nEnter choice (from 1 to 5): ")
    print("1) Add a new employee")
    print("2) List all employees")
    print("3) Delete by age range")
    print("4) Update salary given a name")
    print("5) End the program")
    choice = input()
    if choice.isdecimal():
        return int(choice)
    return -1


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.name} has age {self.age} and salary {self.salary}"


class EmployeesManager:
    def __init__(self):
        self.employee_lst = []

    def add_employee(self, employee_obj):
        self.employee_lst.append(employee_obj)

    def list_employees(self):
        for employee in self.employee_lst:
            print("Employee:", employee)

    def delete_employee(self, start_age, end_age):
        for pos in range(len(self.employee_lst)-1, -1, -1):
            if start_age <= self.employee_lst[pos].age <= end_age:
                print(f"Deleting Employee: {self.employee_lst[pos].name}")
                del self.employee_lst[pos]

    def update_salary(self, find_name, salary):
        for idx, employee in enumerate(self.employee_lst):
            if employee.name == find_name:
                self.employee_lst[idx].salary = salary
                print("Updated Successfully")
                return
        print("There is no such employee in the system")


class FrontEndManager:
    def __init__(self):
        self.employee_manager = EmployeesManager()

    def print_menu(self):
        while True:
            choice = input_invalid_int()
            if 1 <= choice <= 5:

                employee = Employee(None, None, None)
                if choice == 1:
                    print("Enter employee data:")
                    employee.name = input("Enter the name: ")
                    employee.age = int(input("Enter tha age:"))
                    employee.salary = float(input("Enter the salary:"))
                    self.employee_manager.add_employee(employee)

                elif choice == 2:
                    print("\n*** Employee List ***")
                    if len(self.employee_manager.employee_lst) == 0:
                        print("There is no employees at the moment !!!")
                    else:
                        self.employee_manager.list_employees()
                        print()

                elif choice == 3:
                    start_age = int(input("Enter start age: "))
                    end_age = int(input("Enter end age: "))
                    self.employee_manager.delete_employee(start_age, end_age)

                elif choice == 4:
                    name = input("Enter name: ")
                    new_salary = input("Enter new salary: ")
                    self.employee_manager.update_salary(name, new_salary)
                elif choice == 5:
                    print("Program Ended !!!")
                    break
            else:
                print("Invalid range. Try again")
                print()
                continue

    def run(self):
        self.print_menu()


if __name__ == '__main__':
    print("Program Started !!!")
    app = FrontEndManager()
    app.run()

# no employee at the moment
# check if you find the employee before updating salary

"""
    def delete_employee(self, start_age, end_age):
        for pos in range(len(self.employee_lst)-1, -1, -1):
            if start_age <= self.employee_lst[pos].age <= end_age:
                print("Deleting Employee:", self.employee_lst[pos].name)
                del self.employee_lst[pos]
"""
