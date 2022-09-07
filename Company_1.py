from abc import ABC, ABCMeta, abstractmethod


class Employee(ABC):
    list_of_employees = []

    def __init__(self, name: str, surname: str, id):
        self._name = name
        self._surname = surname
        self._id = id

        Employee.list_of_employees.append(self)

    @abstractmethod
    def do_work(self):
        pass

    @abstractmethod
    def take_vacation(self):
        pass

    def __repr__(self):
        return {'name': self._name, 'surname': self._surname}


class SWEngineer(Employee):

    def __init__(self, name, surname, id, title):
        super().__init__(name, surname, id)
        self._title = title

    def do_work(self):
        print("I do work")

    def take_vacation(self):
        print("I to=ake vacation")

    @staticmethod
    def do_coding():
        print('I do coding')


class SWManager(SWEngineer):
    def __init__(self, name, surname, id, title):
        super().__init__(name, surname, id, title)

    def mentor_employee(self, employee_name):
        print(f'{self._name} is mentoring {employee_name} from now on')

    def distribute_task(self, employee_name, task_description):
        print(f"{self._name} is giving the task of {task_description} to {employee_name}")


class Accountant(Employee, ABC):
    def __init__(self, name, surname, id):
        super().__init__(name, surname, id)

    def release_salary(self):
        print(f"{self._name} is releasing salary")


class FinanceManager(Accountant, ABC):
    def __init__(self, name, surname, id):
        super().__init__(name, surname, id)

    def create_company_budget(self):
        print(f'{self._name} is creating company budget')


class SalesPerson(Employee, ABC):
    def __init__(self, name, surname, id, customer_accounts):
        super().__init__(name, surname, id)
        self._customer_accounts = customer_accounts

    def run_product_demo(self):
        print(f"{self._name} is runing product demo")


class Executive(Employee, ABC):
    all_executives = []

    def __init__(self, name, surname):
        super().__init__(name, surname)

        Executive.all_executives.append(self)

    @staticmethod
    def confirm_hiring(self, new_name, new_surname, new_id):
        new_employee = Employee(new_name, new_surname, new_id)
        return new_employee

    @staticmethod
    def confirm_firing(id):
        print(f"The employee with id:{id} is deleted")

    @staticmethod
    def confirm_company_budget():
        print('Confirming company budget')


class Manager(ABC):
    def __init__(self, reports):
        self._direct_reports = reports

    @abstractmethod
    def evaluate_employee(self, id):
        print(f"Evaluating employee with id:{id}")

    @abstractmethod
    def review_salary(self, id):
        print(f"Reviewing salary of employee with id:{id}")

    @staticmethod
    def get_direct_reports():
        print('Getting direct reports')

    @staticmethod
    def get_team():
        print('Getting teams')


class Company:
    def __init__(self, name):
        self._name = name
        self._director = Executive.all_executives
        self._employees = Employee.list_of_employees

    @staticmethod
    def getEmployee(name, surname):
        for employee in Employee.list_of_employees:
            if employee['name'] == name and employee['surname'] == surname:
                return employee
        else:
            return f"No employee with name {name} and surname {surname}"

    @staticmethod
    def getEmployees():
        return Employee.list_of_employees
