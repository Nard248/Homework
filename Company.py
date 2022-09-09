from abc import ABC, abstractmethod


class Company:
    id = 0
    list_of_companies: list[object] = []
    id_list: list[int] = []

    def __init__(self, name: str, director: 'Executive' = None, budget=0):
        list_of_employees = []
        self.name = name
        self._director = director
        self.budget = budget
        Company.id += 1
        self._id = Company.id
        Company.id_list.append(Company.id)
        employee: Employee
        for employee in Employee.employee_list:
            if employee.company_id == self._id:
                list_of_employees.append(self)
        self._employees = list_of_employees
        Company.list_of_companies.append(self)

    def getEmployee(self, name, surname):
        employee: Employee
        for employee in self._employees:
            if employee.name == name and employee.surname == surname:
                return employee

    def getEmployees(self):
        return self._employees

    def hire_employee(self, name, surname, passport_id, age, _type, exp_salary, manager=None):
        executive = self._director
        if executive is not None and executive.confirm_hiring(age, exp_salary):
            return Employee(name, surname, self._id, age, passport_id, manager, exp_salary)
        else:
            return f"No director or executive did not accept"


class Employee(ABC):
    employee_id = 0
    employee_list = []

    def __init__(self, name: str, surname: str, company_id: int, age, pass_id, mentor=None, salary=0, team=[]):
        Employee.employee_id += 1
        self._id = Employee.employee_id
        self.name = name
        self.surname = surname
        self.company_id = company_id
        self.age = age
        self.pass_id = pass_id
        self.mentor = mentor
        self._salary = salary
        self.team = team
        Employee.employee_list.append(self)


    @abstractmethod
    def do_work(self):
        pass

    @abstractmethod
    def take_vacation(self, days):
        pass


class Manager(ABC):
    def __init__(self, direct_reports):
        self.direct_reports = direct_reports

    @abstractmethod
    def evaluate_employee(self, grade: int, employee: Employee):
        pass

    @abstractmethod
    def review_salary(self, employee: Employee):
        pass

    def get_direct_reports(self):
        return self.direct_reports

    # def get_team(self):
    #     team_members = []
    #     employee: Employee
    #     for employee in Employee.employee_list:
    #         if employee.mentor == self:
    #             team_members.append(employee)
    #     return team_members
    def get_team(self):
        return self.team


class SWEngineer(Employee):

    def __init__(self, name: str, surname: str, company_id: int, age, pass_id, title, mentor=None, salary=0, team=[]):
        assert company_id in Company.id_list, 'No such company defined'
        super().__init__(name, surname, company_id, age, pass_id, mentor, team)
        self._title = title
        self._id = Employee.employee_id + 1
        self._salary = salary
        Employee.employee_id += 1

    def take_vacation(self, days):
        return f"{self.name} is taking vacation form {days} days"

    def do_work(self):
        return f"{self.name} is working"

    def do_coding(self):
        return f"{self.name} is coding"


class SWManager(SWEngineer, Manager):
    def __init__(self, name: str, surname: str, company_id: int, age, pass_id, title='Manager', mentor=None, salary=0, team=[], direct_reports=[]):
        SWEngineer.__init__(self, name, surname, company_id, age, pass_id, title, mentor, salary, team)
        Manager.__init__(self, direct_reports)
        self._id = Employee.employee_id + 1
        Employee.employee_id += 1

    def mentor_employee(self, employee: SWEngineer):
        if employee.mentor is None:
            employee.mentor = self
            self.direct_reports.append(employee)
            self.team.append(employee)
            return f"Employee {employee.name} is being mentored by {self.name} from now on"
        else:
            return f"The employee {employee.name} already has a mentor` {employee.mentor}"

    def distribute_tasks(self, task_list, employee: SWEngineer):
        if self == employee.mentor:
            employee.tasks = task_list
            return f"Successfully distributed tasks for {employee.name}"
        else:
            return f"{self.name} is not mentor of {employee.name} to give tasks"

    def review_salary(self, employee: SWEngineer):
        return f"Salary of {employee.name} is {employee._salary}"

    def evaluate_employee(self, grade, employee: SWEngineer):
        employee.evaluation = grade
        return f"Evaluation the {employee.name} with grade of {grade}"


class Accountant(Employee):
    def __init__(self, name: str, surname: str, company_id: int, age, pass_id, title='Accountant', mentor=None, salary=0, team=[]):
        super(Accountant, self).__init__(name, surname, company_id, age, pass_id, title, mentor, salary, team)
        self.mentor = mentor
        self._id = Employee.employee_id + 1
        Employee.employee_id += 1

    def take_vacation(self, days):
        return f"{self.name} is taking Vacation for {days} days"

    def do_work(self):
        return f"{self.name} is doing work"

    def release_salary(self, employee: Employee):
        return f"{self.name} released salary for {employee.name} in amount of {employee._salary}"


class FinanceManager(Accountant, Manager):

    def __init__(self, name: str, surname: str, company_id: int, age, pass_id, title='Accountant', mentor=None, salary=0, team=[], direct_reports=[]):
        Accountant.__init__(self, name, surname, company_id, age, pass_id, title, mentor, salary, team)
        Manager.__init__(self, direct_reports)
        self._id = Employee.employee_id + 1
        Employee.employee_id += 1

    def create_company_budget(self, budget):
        company: Company
        company_id: int = self.company_id - 1
        company = Company.list_of_companies[company_id]
        company.budget = budget
        return f"Successfully created budget for company {company.name}, with " \
               f"amount of {budget} "

    def mentor_employee(self, employee: Accountant):
        if employee.mentor is None:
            employee.mentor = self
            self.direct_reports.append(employee)
            self.team.append(employee)
            return f"Employee {employee.name} is being mentored by {self.name} from now on"
        else:
            return f"The employee {employee.name} already has a mentor` {employee.mentor}"

    def distribute_tasks(self, task_list, employee: Accountant):
        if self == employee.mentor:
            employee.tasks = task_list
            return f"Successfully distributed tasks for {employee.name}"
        else:
            return f"{self.name} is not mentor of {employee.name} to give tasks"

    def review_salary(self, employee: Accountant):
        return f"Salary of {employee.name} is {employee._salary}"

    def evaluate_employee(self, grade: int, employee: Accountant):
        employee.evaluation = grade
        return f"Evaluation the {employee.name} with grade of {grade}"


class SalesPerson(Employee):
    def __init__(self, name, surname, company_id, customer_accounts):
        super(SalesPerson, self).__init__(name, surname, company_id)
        self._customer_accounts = customer_accounts
        self._id = Employee.employee_id + 1
        Employee.employee_id += 1

    def take_vacation(self, days):
        return f"{self.name} is taking Vacation for {days} days"

    def do_work(self):
        return f"{self.name} is doing work"

    def run_product_demo(self):
        return f'{self.name} is releasing product demo'


class Executive(Employee, Manager):
    executives_list = []

    def __init__(self, name: str, surname: str, company_id: int, age, pass_id, mentor=None, salary=0, team=[], direct_reports=[]):
        Employee.__init__(self, name, surname, company_id, age, pass_id, mentor, salary, team)
        Manager.__init__(self, direct_reports)
        self._id = Employee.employee_id + 1
        Employee.employee_id += 1
        Executive.executives_list.append(self.name)

    def take_vacation(self, days):
        return f"{self.name} is taking Vacation for {days} days"

    def do_work(self):
        return f"{self.name} is doing work"

    @staticmethod
    def confirm_hiring(age, exp_salary):
        if age <= 30 and exp_salary < 15000:
            return True
        return False

    @staticmethod
    def confirm_firing(employee: Employee):
        employee.fired_status = False
        return f'{employee.name} is fired'

    def confirm_company_budget(self):
        company: Company
        company = Company.list_of_companies[self.company_id - 1]
        if company.budget > 10000 or company.budget is None:
            company.budget_confirm = False
            return f"Budget of size {company.budget} cannot be accepted, according to company's executive"
        else:
            company.budget_confirm = True
            return f"{company.name}'s budget is successfully confirmed"

    def review_salary(self, employee: Employee):
        return f"Salary of {employee.name} is {employee._salary}"

    def evaluate_employee(self, grade, employee: Employee):
        employee.evaluation = grade
        return f"Evaluation the {employee.name} with grade of {grade}"


if __name__ == '__main__':
    onex = Company('Onex')
    globbing = Company('Globbing')

    empl1 = SWEngineer('Name', 'Surname', 1, 'Junior')
    manager_1 = SWManager('Manager', 'Surenyan', 1)
    manager_1.mentor_employee(empl1)
    print(manager_1.direct_reports)
