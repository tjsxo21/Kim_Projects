from abc import ABC, abstractmethod
from departments import finance

class employee(ABC):
    employee_list = []

    @abstractmethod
    def get_args(self):
        pass

    @abstractmethod
    def employee_info():
        pass

    def allemployeeinfo():
        for i in employee.employee_list:
            print(i)

class clientservices_employee(employee):
    clientservices_employee_list = []

    def __init__(self, *args):
        # Encapsulation - Private Attribute
        self.__args = args
        self.employee_list.append(args)
        self.clientservices_employee_list.append(self)
        print('Client Services Employee Created')
        finance.finance.expense(int(args[2]))

    def get_args(self):
        return self.__args

    def employee_info():
        for i in clientservices_employee.clientservices_employee_list:
            print(clientservices_employee.get_args(i))

class finance_employee(employee):
    finance_employee_list = []

    def __init__(self, *args):
        # Encapsulation - Private Attribute (__args)
        self.__args = args
        self.employee_list.append(args)
        self.finance_employee_list.append(self)
        print('Finance Employee Created')
        finance.finance.expense(int(args[2]))

    # Returns all args passed in for an object
    def get_args(self):
        return self.__args

    def employee_info():
        for i in finance_employee.finance_employee_list:
            print(finance_employee.get_args(i))

class engineering_employee(employee):
    engineering_employee_list = []

    def __init__(self, *args):
        # Encapsulation - Private Attribute
        self.__args = args
        self.employee_list.append(args)
        self.engineering_employee_list.append(self)
        print('Engineering Employee Created')
        finance.finance.expense(int(args[2]))

    def get_args(self):
        return self.__args

    def employee_info():
        for i in engineering_employee.engineering_employee_list:
            print(engineering_employee.get_args(i))

class hr_employee(employee):
    hr_employee_list = []

    def __init__(self, *args):
        # Encapsulation - Private Attribute
        self.__args = args
        self.employee_list.append(args)
        self.hr_employee_list.append(self)
        print('HR Employee Created')
        finance.finance.expense(int(args[2]))

    def get_args(self):
        return self.__args

    def employee_info():
        for i in hr_employee.hr_employee_list:
            print(hr_employee.get_args(i))

# Instantiating Employee Objects
def instantiateObjects():
    Employee1 = clientservices_employee('Bob', 'Client Services', 65000)
    Employee2 = engineering_employee('Sun', 'Engineering', 100000)
    Employee3 = finance_employee('Tom', 'Finance', 90000, '28', 'VT Grad')
    Employee4 = hr_employee('Gary', 'HR', '100000')

instantiateObjects()
