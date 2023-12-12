class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname


class SalaryEmployee(Employee):
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname)
        self.salary = salary

    def emp_paycheck(self):
        return self.salary / 52


class HourlyEmployee(Employee):
    def __init__(self, fname, lname, weekly_hours, hourly_rate):
        super().__init__(fname, lname)
        self.weekly_hours = weekly_hours
        self.hourly_rate = hourly_rate

    def emp_paycheck(self):
        return self.weekly_hours * self.hourly_rate


class CommisionEmployee(SalaryEmployee):
    def __init__(self, fname, lname, salary, no_sales, com_rate):
        super().__init__(fname, lname, salary)
        self.no_sales = no_sales
        self.com_rate = com_rate

    def emp_paycheck(self):
        regular_salary = super().emp_paycheck()
        total_salary = self.no_sales * self.com_rate
        return regular_salary + total_salary
