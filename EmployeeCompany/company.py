from employee import Employee, SalaryEmployee, HourlyEmployee, CommisionEmployee


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employee(self):
        print("Current Employees")
        for i in self.employees:
            print(i.fname, i.lname)
        print("____________________")

    def paycheck(self):
        print("Employee Paycheck")
        for i in self.employees:
            print(i.fname, i.lname)
            print(f"Amount  ${i.emp_paycheck():,.2f}")
            print("___________________")


def main():
    my_company = Company()
    employee1 = SalaryEmployee("Harry", "Potter", 50000)
    my_company.add_employee(employee1)
    employee2 = HourlyEmployee("Ron", "Weasley", 16, 50)
    my_company.add_employee(employee2)
    employee3 = CommisionEmployee("Hermione", "Granger", 70000, 5, 100)
    my_company.add_employee(employee3)

    my_company.display_employee()
    my_company.paycheck()


main()
