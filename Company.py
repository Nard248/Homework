from abc import ABC, abstractmethod


class Company:
    id = 0
    list_of_companies: list[object] = []

    def __init__(self, name: str, director=None, budget=0):
        list_of_employees = []
        self.name = name
        self._director = director
        self.budget = budget
        Company.id += 1
        self._id = Company.id
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


class Employee(ABC):
    employee_id = 0
    employee_list = []

    def __init__(self, name: str, surname: str, company_id: int, mentor=None, salary=0):
        Employee.employee_id += 1
        self._id = Employee.employee_id
        self.name = name
        self.surname = surname
        self.company_id = company_id
        self.mentor = mentor
        self._salary = salary
        Employee.employee_list.append(self)

    @abstractmethod
    def do_work(self):
        pass

    @abstractmethod
    def take_vacation(self, days):
        pass


class Manager(ABC):
    def __init__(self):
        self.direct_reports = None

    @abstractmethod
    def evaluate_employee(self, grade: int, employee: Employee):
        pass

    @abstractmethod
    def review_salary(self, employee: Employee):
        pass

    def get_direct_reports(self):
        return self.direct_reports

    def get_team(self):
        team_members = []
        employee: Employee
        for employee in Employee.employee_list:
            if employee.mentor == self:
                team_members.append(employee)
        return team_members


class SWEngineer(Employee):

    def __init__(self, name: str, surname: str, company_id: int, title: str, salary=1000):
        assert company_id < Company.id, 'No such company defined'
        super().__init__(name, surname, company_id)
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
    def __init__(self, name, surname, company_id, title='Manager', direct_reports=None):
        super().__init__(name, surname, company_id, title)
        self.direct_reports = direct_reports
        self._id = Employee.employee_id + 1
        Employee.employee_id += 1

    def mentor_employee(self, employee: SWEngineer):
        if employee.mentor is None:
            employee.mentor = self
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
    def __init__(self, name, surname, company_id, mentor=None):
        super(Accountant, self).__init__(name, surname, company_id)
        self.mentor = mentor
        self._id = Employee.employee_id + 1
        Employee.employee_id += 1

    def take_vacation(self, days):
        return f"{self.name} is taking Vacation for {days} days"

    def do_work(self):
        return f"{self.name} is doing work"

    def release_salary(self, employee: Employee):
        return f"{self.name} released salary for {employee.name} in amount of {employee._salary}"


# TODO implement Manager abstract class abstract methods in this implementation
class FinanceManager(Accountant, Manager):

    def __init__(self, name, surname, company_id):
        super(FinanceManager, self).__init__(name, surname, company_id)
        self._id = Employee.employee_id + 1
        Employee.employee_id += 1

    def create_company_budget(self, budget):
        company: Company
        company = Company.list_of_companies[self.company_id - 1]
        company.budget = budget
        return f"Successfully created budget for company {company.name}, with " \
               f"amount of {budget} "

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
        pass


class Executive(Employee):
    executives_list = []

    def __init__(self, name, surname, company_id):
        super(Executive, self).__init__(name, surname, company_id)
        self._id = Employee.employee_id + 1
        Employee.employee_id += 1
        Executive.executives_list.append(self.name)

    def take_vacation(self, days):
        return f"{self.name} is taking Vacation for {days} days"

    def do_work(self):
        return f"{self.name} is doing work"

    @staticmethod
    def confirm_hiring(employee: Employee):
        apply_status = True
        employee.apply_status = apply_status
        return f'{employee.name} is successfully applied'

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


onex = Company('Onex')
print(onex)
globbing = Company('Globbing')
print(globbing)

empl1 = SWEngineer('Name', 'Surname', 1, 'Junior')
print(type(Employee.employee_list[0]) == SWEngineer)
manager_1 = SWManager('Manager', 'Surenyan', 1)
manager_1.mentor_employee(empl1)
print(manager_1.get_team())
