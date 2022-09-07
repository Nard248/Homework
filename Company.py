from abc import ABC, abstractmethod


# TODO implement two instance methods for companies, and define director and employees list
class Company:
    id = 0
    list_of_companies = []

    def __init__(self, name: str, director=None):
        self._name = name
        if director in Executive.executives_list:
            self._director = director
        else:
            self._director = 'No Director'
        Company.id += 1
        self._id = Company.id
        list_of_employees = []
        for employee in Employee.employee_list:
            if employee._company_id == self._id:
                list_of_employees.append(self)
        self._employees = list_of_employees
        Company.list_of_companies.append(self)

    def getEmployee(self, name, surname):
        for employee in self._employees:
            if employee._name == name and employee._surname == surname:
                return employee

    def getEmployees(self):
        return self._employees


class Employee(ABC):
    employee_id = 0
    employee_list = []

    def __init__(self, name: str, surname: str, company_id: int):
        self._name = name
        self._surname = surname
        self._company_id = company_id
        Employee.employee_list.append(self)

    @abstractmethod
    def do_work(self):
        pass

    @abstractmethod
    def take_vacation(self):
        pass


# TODO implement Manager abstract class, ask Zaruhi about it
class Manager(ABC):
    def __init__(self, direct_reports=[]):
        self._direct_reports = direct_reports

    @abstractmethod
    def evaluate_employee(self):
        pass

    @abstractmethod
    def review_salary(self):
        pass

    def get_direct_reports(self):
        return self._direct_reports

    def get_team(self):
        team_members = []
        for reporter in self._direct_reports:
            team_members.append(reporter._name)
        return team_members


class SWEngineer(Employee):

    def __init__(self, name, surname, company_id, title):
        super().__init__(name, surname, company_id)
        self._title = title
        self._id = Employee.employee_id + 1
        Employee.employee_id += 1

    def take_vacation(self):
        pass

    def do_work(self):
        pass

    def do_coding(self):
        pass


# TODO implement Manager abstract class abstract methods in this implementation
class SWManager(SWEngineer):

    def __init__(self, name, surname, company_id, title='Manager'):
        super().__init__(name, surname, company_id, title)
        self._id = Employee.employee_id + 1
        Employee.employee_id += 1

    # def mentor_employee(self, name, surname):
    #     for employee in Employee.employee_list:
    #         if employee.__name__

    def distribute_tasks(self):
        pass


class Accountant(Employee):
    def __init__(self, name, surname, company_id):
        super(Accountant, self).__init__(name, surname, company_id)
        self._id = Employee.employee_id + 1
        Employee.employee_id += 1

    def take_vacation(self):
        pass

    def do_work(self):
        pass

    def release_salary(self):
        pass


# TODO implement Manager abstract class abstract methods in this implementation
class FinanceManager(Accountant):
    def __init__(self, name, surname, company_id):
        super(FinanceManager, self).__init__(name, surname, company_id)
        self._id = Employee.employee_id + 1
        Employee.employee_id += 1

    def create_company_budget(self):
        pass


class SalesPerson(Employee):
    def __init__(self, name, surname, company_id, customer_accounts):
        super(SalesPerson, self).__init__(name, surname, company_id)
        self._customer_accounts = customer_accounts
        self._id = Employee.employee_id + 1
        Employee.employee_id += 1

    def take_vacation(self):
        pass

    def do_work(self):
        pass

    def run_product_demo(self):
        pass


# TODO implement Manager abstract class abstract methods in this implementation
class Executive(Employee):
    executives_list = []

    def __init__(self, name, surname, company_id):
        super(Executive, self).__init__(name, surname, company_id)
        self._id = Employee.employee_id + 1
        Employee.employee_id += 1
        Executive.executives_list.append(self._name)

    def take_vacation(self):
        pass

    def do_work(self):
        pass

    @staticmethod
    def confirm_hiring(employee_object):
        apply_status = True
        employee_object.apply_status = apply_status
        return f'{employee_object._name} is successfully applied'

    @staticmethod
    def confirm_firing(employee_object):
        employee_object.apply_status = False
        return f'{employee_object._name} is fired'

    def confirm_company_budget(self):
        for company in Company.list_of_companies:
            if company._id == self._company_id:
                company.confirmation_of_budget = True
                return f"{company._name}'s budget is successfully confirmed"


onex = Company('Onex')
print(onex)
globbing = Company('Globbing')
print(globbing)

empl1 = SWEngineer('Name', 'Surname', 1, 'Junior')
print(type(Employee.employee_list[0]) == SWEngineer)
