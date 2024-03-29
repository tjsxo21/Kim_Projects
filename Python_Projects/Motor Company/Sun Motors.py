#!/usr/bin/env python
# coding: utf-8

# In[1]:


# This project built a motor company structure that takes care of outside customer services as well as internal employees within the company.
# This project demonstrates OOP concepts: class/objects/polymorphism/encapsulation/inheritance/data abstraction
from abc import ABC, abstractmethod
import pdb # debugger
import sys


def main():
    # pdb.set_trace() # trace code, type n for nextline.
    # Current Departments: finance/customer support/sales/services/hr/egr/etc
    
    def credentials_check():
        
        a = 0 
        
        while a < 3:
            
            passcode = input("Please type in the pass code ")
        
            if int(passcode) == 1432:
                print("Passcode verified")
                a = 100
                
            elif a == 2:
                print("Invalid credentials. Opting out. Goodbye.")
                sys.exit()
            
            a += 1
    
    print("\nWelcome to Sunmotors! Please choose from the following menu options.")
    z = 0
    while z < 3:
        print("For Sales - 1, Services - 2, Customer Support - 3, Employees Internal - 4, Opt Out - 5")
        menu = input("Please type in the number from the above menu options ")
        
        if int(menu) == 1:
            sunmotors_sales.sales_main()
            z = 100
        
        elif int(menu) == 2:
            sunmotors_services.services_main()
            z = 100
            
        elif int(menu) == 3:
            sunmotors_cs.cs_main()
            z = 100
            
        elif int(menu) == 4:
            # sunmotors_cs.cs_main()
            credentials_check()
            print("For Finance - 1, HR - 2, EGR - 3, Return to Main - 4")
            menu = input("Please type in the number from the above menu options ")
            
            if int(menu) == 1:
                sunmotors_finance.finance_main()
                
            elif int(menu) == 2:
                sunmotors_hr.hr_main()
                
            elif int(menu) == 3:
                sunmotors_egr.egr_main()
            # Build HR, EGR
            z = 100
            
        elif int(menu) == 5:
            print("Opting out. Goodbye.")
            sys.exit()
        
        elif z == 2:
            print("Incorrect number. Please call again.")
            sys.exit()
        
        else:
            print("Please type in the proper number")
        
        z += 1


# In[2]:


class sunmotors():
    
    sunmotors_list = []
    
    # __init__ is known as the constructor
    # Method Overloading - Sets all values to none. Passing any number of parameters doesn't cause an error.
    
    def __init__(self,model=None,year=None,msrp=None,traits=None):
        print("Sunmotors Vehicle Created")
        self.model = model
        self.year = year
        self.msrp = msrp
        self.traits = traits
        
        
class car_functions:
    
    def basic_specs(self):
        print('Vehicle Specs: ' + '\n' + str(self.model) + '\n' + str(self.year) + '\n' + str(self.msrp) + '\n' + str(self.traits))
    
    def test_drive(self):
        print("Test Driving " + self.model)
        
# Multiple inheritance & Abstract class        
class sunmotors_electric(sunmotors,car_functions,ABC):
    
    def __init__(self,model=None,year=None,msrp=None,traits=None):
        print("Sunmotors Electric Vehicle Created")
        super().__init__(model,year,msrp,traits)
    
    # Method overriding, abstract method
    @abstractmethod
    def cartype(self):
        pass
    
# Multiple inheritance & Abstract class            
class sunmotors_hydrogen(sunmotors,car_functions,ABC):
    
    def __init__(self,model,year,msrp,traits):
        print("Sunmotors Hydrogen Vehicle Created")
        super().__init__(model,year,msrp,traits)
        
    # Method overriding, abstract method
    @abstractmethod
    def cartype(self):
        pass
        
# Multi-level inheritance        
class sunmotors_hydrogen_suvs(sunmotors_hydrogen):
    
    # Class attribute
    attr1 = "SUV"
    
    # Instance attribute
    def __init__(self,model=None,year=None,msrp=None,traits=None,inventory=None):
        print("Sunmotors Hydrogen SUV Created")
        super().__init__(model,year,msrp,traits)
        self.__inventory = inventory
        sunmotors.sunmotors_list.append(self)
        
    def cartype(self):
        print('hydrogen suv')
        
    def set_inventory(self,value):
        self.__inventory = value
        
    def get_inventory(self):
        return self.__inventory
        
        
class sunmotors_ev_suvs(sunmotors_electric):
    # __init__ is known as the constructor
    def __init__(self,model=None,year=None,msrp=None,traits=None,inventory=None):
        print("Sunmotors EV SUV Created")
        super().__init__(model,year,msrp,traits)
        # Encapsulation
        self.__inventory = inventory
        sunmotors.sunmotors_list.append(self)
        
    # Method overriding
    def cartype(self):
        print('ev suv')
    # Encapsulation set & get method    
    def set_inventory(self,value):
        self.__inventory = value
        
    def get_inventory(self):
        return self.__inventory
    
    
class sunmotors_hydrogen_sedans(sunmotors_hydrogen):
    
    def __init__(self,model=None,year=None,msrp=None,traits=None,inventory=None):
        # instance attribute
        print("Sunmotors Hydrogen Sedan Created")
        super().__init__(model,year,msrp,traits)
        self.__inventory = inventory
        sunmotors.sunmotors_list.append(self)
        
    def cartype(self):
        print('hydrogen sedan')
        
    def set_inventory(self,value):
        self.__inventory = value
        
    def get_inventory(self):
        return self.__inventory
        
        
class sunmotors_ev_sedans(sunmotors_electric):
    # __init__ is known as the constructor
    def __init__(self,model,year,msrp,traits,inventory):
        print("Sunmotors EV Sedan Created")
        super().__init__(model,year,msrp,traits)
        self.__inventory = inventory
        sunmotors.sunmotors_list.append(self)
        
    def cartype(self):
        print('ev sedan')
        
    def set_inventory(self,value):
        self.__inventory = value
        
    def get_inventory(self):
        return self.__inventory

        
def ducktyping_cartype(obj):
    obj.cartype()


# In[3]:


# Object Instantiation
hydrogen_sedan_A = sunmotors_hydrogen_sedans(model='hydrogen sedan_A',year=2022,msrp=24000,traits='hydrogen sedan',inventory=10)
hydrogen_suv_A = sunmotors_hydrogen_suvs(model='hydrogen_suv_A',year=2022,msrp=33000,traits='hydrogen suv',inventory=5)
hydrogen_suv_B = sunmotors_hydrogen_suvs(model='hydrogen_suv_B',msrp=33000,inventory=5)
ev_suv_A = sunmotors_ev_suvs(model='ev_suv_A',year=2022,msrp=70000,traits='ev suv',inventory=6)
ev_sedan_A = sunmotors_ev_sedans(model='ev_sedan_A',year=2023,msrp=60000,traits='ev sedan',inventory=7)


# In[4]:


class sunmotors_finance():
    # Buy-in
    current_revenue = 1000000
    employee_list = []
    print("Welcome to Sunmotors Finance")
    
    def finance_main():
        print("Welcome to Sunmotors Finance")
        print("For revenue report - 1, Return to Main - 2")
        menu = input("Please type in the number from the above menu options ")

        if int(menu) == 1:
            sunmotors_finance.revenue_report()
            main()

        elif int(menu) == 2:
            print("Directing you to main...")
            main()

        else:
            print("Wrong number. Directing you to main...")
            main()
    
    def __init__(self,name,dept,title,salary):
        
        self.name = name
        self.dept = dept
        self.title = title
        self.salary = salary
        print("Finance Employee Created")
        sunmotors_hr.allemployee_list.append(self)
        sunmotors_finance.employee_list.append(self)
    
    def income(income_source,revenue):
        revenue += income_source
        sunmotors_finance.current_revenue = revenue
        print("$" + str(income_source) + " added to revenue")
        print("Current renewed revenue: " + str(sunmotors_finance.current_revenue))
    
    def expense(expense_source,revenue):
        revenue -= expense_source
        sunmotors_finance.current_revenue = revenue
        print("$" + str(expense_source) + " deducted from revenue")
        print("Current renewed revenue: " + str(sunmotors_finance.current_revenue))
    
    def revenue_report():
        print("Current Revenue: " + str(sunmotors_finance.current_revenue))
        main()


# In[5]:


class sunmotors_cs():
    
    employee_list = []
    
    def __init__(self,name,dept,title,salary):
        
        # sunmotors_hr.__init__(self)
        self.name = name
        self.dept = dept
        self.title = title
        self.salary = salary
        print("CS Employee Created")
        sunmotors_hr.allemployee_list.append(self)
        sunmotors_cs.employee_list.append(self)
    
    def cs_main():
        print("Welcome to Sunmotors Customer Support")
        print("For General Questions - 1, Technical Questions - 2, All Other Questions - 3")
        menu = input("Please type in the number from the above menu options ")

        if int(menu) == 1:
            print("For General Questions, Please Dial 1800-123-1111")

        elif int(menu) == 2:
            print("For Technical Questions, Please Dial 1800-123-1112")

        elif int(menu) == 3:
            print("For All Other Questions, Please Dial 1800-123-1113")

        else:
            print("Wrong number. Directing you to main...")
            main()
        
        main() # Going back to main


# In[6]:


class sunmotors_sales():
    # pdb.set_trace()
    employee_list = []
    
    def __init__(self,name,dept,title,salary):
        
        self.name = name
        self.dept = dept
        self.title = title
        self.salary = salary
        print("Sales Employee Created")
        sunmotors_hr.allemployee_list.append(self)
        sunmotors_sales.employee_list.append(self)
    
    def sales_main():
        print("Welcome to Sunmotors Sales")
    
        x = 0

        while x < 3:

            customer_model = input("Which model are you looking for? ")

            for object in sunmotors.sunmotors_list:
                # print(object.model)
                if object.model == customer_model:

                    # inventory check
                    if object.inventory > 0:
                        print("It's in the inventory")
                        quantity = input("How many do you want? ")
                        print(object.model + " " + quantity + " order placed")
                        object.inventory = object.inventory - int(quantity)
                        #print(object.model + " " + str(object.inventory) + " left")
                        cost = object.msrp * int(quantity)
                        print("Thanks for the purchase. Total Cost is $" + str(cost)+".")
                        sunmotors_finance.income(cost, sunmotors_finance.current_revenue)
                    else:
                        print("It's not in the inventory at the moment. Please contact customer service.")
                    x = 100
                    break
            x += 1
            if x < 3:
                print("Please retype the proper model name")
            elif x == 3:
                print("Incorrect model name. Directing you back to main...")
                main()
        
        main() # Going back to main


# In[7]:


class sunmotors_services():
    # pdb.set_trace()
    employee_list = []
    
    def __init__(self,name,dept,title,salary):
        
        self.name = name
        self.dept = dept
        self.title = title
        self.salary = salary
        print("Services Employee Created")
        sunmotors_hr.allemployee_list.append(self)
        sunmotors_services.employee_list.append(self)
    
    def services_main():
        
        print("Welcome to Sunmotors Services")
        print("For Maintenance - 1, Replacement Parts - 2, Accessories - 3")
        menu = input("Please type in the number from the above menu options ")

        if int(menu) == 1:
            sunmotors_services.services_maintenance()

        elif int(menu) == 2:
            sunmotors_services.services_replacement()

        elif int(menu) == 3:
            sunmotors_services.services_accessories()

        else:
            print("Wrong number directing you to main...")
            main()
        
        main() # Going back to main

    def services_maintenance():
        
        def multipoint_inspection():
            print("Multipoint inspection in progress")
            print("The cost is $250")
            sunmotors_finance.income(250, sunmotors_finance.current_revenue)
        
        def oilchange():
            print("Oil Change in progress")
            print("The cost is $50")
            sunmotors_finance.income(50, sunmotors_finance.current_revenue)
            
        print("Maintenance Department")
        print("For Multipoint Inspection - 1, Oil Change - 2")
        menu = input("Please type in the number from the above menu options ")
        
        if int(menu) == 1:
            multipoint_inspection()
                
        elif int(menu) == 2:
            oilchange()
            
        else:
            print("Directing you back to main...")
            main()
    
    def services_replacement():
       
        def tire_replacement():
            print("Tire replacement")
            print("The cost is $200")
            sunmotors_finance.income(200, sunmotors_finance.current_revenue)
        
        def engine_replacement():
            print("Engine replacement")
            print("The cost is $4000")
            sunmotors_finance.income(4000, sunmotors_finance.current_revenue)
        
        print("Replacement Department")
        print("For Tire replacement - 1, Engine Replacement - 2")
        menu = input("Please type in the number from the above menu options ")
        
        if int(menu) == 1:
            tire_replacement()
            
              
        elif int(menu) == 2:
            engine_replacement()
            
        else:
            print("Directing you back to main...")
            main()
        
    def services_accessories():
        
        def enhanced_stereo():
            print("Enhanced Stereo")
            print("The cost is $300")
            sunmotors_finance.income(300, sunmotors_finance.current_revenue)
        
        def seatcovers():
            print("Seat Covers")
            print("The cost is $200")
            sunmotors_finance.income(200, sunmotors_finance.current_revenue)
        
        print("Accessories Department")
        print("For Enhanced Stereo - 1, Seat Covers - 2")
        menu = input("Please type in the number from the above menu options ")
        
        if int(menu) == 1:
            enhanced_stereo()
              
        elif int(menu) == 2:
            seatcovers()
            
        else:
            print("Directing you back to main...")
            main()
        
        main() # Going back to main


# In[8]:


class sunmotors_hr():
    # pdb.set_trace()
    allemployee_list = []
    employee_list = []
    
    def __init__(self,name,dept,title,salary):
        
        self.name = name
        self.dept = dept
        self.title = title
        self.salary = salary
        sunmotors_hr.allemployee_list.append(self)
        sunmotors_hr.employee_list.append(self)
        print("HR Employee Created")
        
    def hr_main():
        
        print("Welcome to Sunmotors HR")
        print("For Employee Info - 1, Training - 2, Compensation & Benefits - 3")
        menu = input("Please type in the number from the above menu options ")

        if int(menu) == 1:
            sunmotors_hr.employee_info()

        elif int(menu) == 2:
            sunmotors_hr.training()

        elif int(menu) == 3:
            sunmotors_hr.compensation()

        else:
            print("Directing you back to main...")
            main()
            
    def employee_info():
        
        employees_list = []
        print("All - 0, Finance - 1, CS - 2, Sales - 3, Services - 4, HR - 5, EGR - 6")
        dept = input("Which department employee info?")
        
        if dept == "0":
            
            employees_list = sunmotors_hr.allemployee_list
        
        elif dept == "1":
            
            employees_list = sunmotors_finance.employee_list
            
        elif dept == "2":
            
            employees_list = sunmotors_cs.employee_list
            
        elif dept == "3":
            
            employees_list = sunmotors_sales.employee_list
            
        elif dept == "4":
            
            employees_list = sunmotors_services.employee_list
            
        elif dept == "5":
            
            employees_list = sunmotors_hr.employee_list
            
        elif dept == "6":
            
            employees_list = sunmotors_egr.employee_list
            
        for item in employees_list:
            print(item.name + ' / ' + item.dept + ' / ' + item.title)
        
    def training():
        
        def corporate_ethics():
            print("Corporate ethics training in progress")
        
        def skill_dev():
            print("Skill dev training in progress")
            
        def compliance():
            print("Compliance training in progress")
        
        print("For corporate ethics - 1, skill dev - 2, compliance - 3")
        menu = input("Which type of training?")
        
        if int(menu) == 1:
            corporate_ethics()
            
        elif int(menu) == 2:
            skill_dev()
        
        elif int(menu) == 3:
            compliance()
        
        else:
            print("Directing you back to main")
            main()
            
    def compensation():
        totalyearly_salary = 0
        for item in sunmotors_hr.allemployee_list:
            totalyearly_salary += item.salary
        sunmotors_finance.expense(totalyearly_salary,sunmotors_finance.current_revenue)
    
        main() # Going back to main


# In[9]:


class sunmotors_egr():
    
    employee_list = []
    
    def __init__(self,name,dept,title,salary):
        
        self.name = name
        self.dept = dept
        self.title = title
        self.salary = salary
        print("Engineering Employee Created")
        sunmotors_hr.allemployee_list.append(self)
        sunmotors_egr.employee_list.append(self)
            
    def ev_rnd():
        print("Electric Vehicle R&D in progress (Cost: $70000/yr)")
        sunmotors_finance.expense(70000,sunmotors_finance.current_revenue)
        
    def hydrogen_rnd():
        print("Hydrogen Vehicle R&D in progress (Cost: $60000/yr)")
        sunmotors_finance.expense(60000,sunmotors_finance.current_revenue)
    
    def autonomous_rnd():
        print("Autonomous Driving R&D in progress (Cost: $80000/yr)")
        sunmotors_finance.expense(80000,sunmotors_finance.current_revenue)
    
    def egr_main():
    
        print("Welcome to Sunmotors EGR")
        print("For EV R&D - 1, Hydrogen EV R&D - 2, Autonomous R&D - 3")
        menu = input("Please type in the number from the above menu options ")

        if int(menu) == 1:
            sunmotors_egr.ev_rnd()

        elif int(menu) == 2:
            sunmotors_egr.hydrogen_rnd()

        elif int(menu) == 3:
            sunmotors_egr.autonomous_rnd()

        else:
            print("Directing you back to main...")
            main()
        
        main() # Going back to main


# In[10]:


Finance_Employee1 = sunmotors_finance(name='Amy Cron',dept='Finance',title='Senior Financial Analyst',salary=100000)
Finance_Employee2 = sunmotors_finance(name='John Doe',dept='Finance',title='Junior Financial Analyst',salary=60000)
CS_Employee1 = sunmotors_cs(name='Brian Kim',dept='CS',title='Customer Services Manager',salary=90000)
CS_Employee2 = sunmotors_cs(name='Holly Doe',dept='CS',title='Customer Representative',salary=45000)
Sales_Employee1 = sunmotors_sales(name='Tom Doe',dept='Sales',title='Sales Manager',salary=90000)
Sales_Employee2 = sunmotors_sales(name='James Doe',dept='Sales',title='Sales Associate',salary=70000)
Services_Employee1 = sunmotors_services(name='Dave Doe',dept='Services',title='Services Manager',salary=120000)
Services_Employee2 = sunmotors_services(name='Don Doe',dept='Services',title='Mechanic',salary=100000)
HR_Employee1 = sunmotors_hr(name='Maggy Has',dept='HR',title='HR Manager',salary=100000)
HR_Employee2 = sunmotors_hr(name='Harry Kim',dept='HR',title='HR Associate',salary=70000)
EGR_Employee1 = sunmotors_egr(name='Gary Bald',dept='EGR',title='EGR Manager',salary=130000)
EGR_Employee2 = sunmotors_egr(name='David Boo',dept='EGR',title='Data Scientist',salary=100000)


# In[11]:


ev_suv_A.basic_specs()


# In[12]:


hydrogen_suv_A.test_drive()


# In[13]:


hydrogen_sedan_A.basic_specs()


# In[14]:


hydrogen_suv_B.basic_specs()


# In[15]:


ev_suv_A.cartype()
ducktyping_cartype(ev_suv_A)
ducktyping_cartype(hydrogen_sedan_A)


# In[16]:


ev_suv_A.set_inventory(30)
hydrogen_suv_A.set_inventory(40)
# ev_suv_A.__inventory (Cause error)
# ev_suv_A.__inventory = 40 (This won't work since it's a private var)
print(ev_suv_A.get_inventory())
print(hydrogen_suv_A.get_inventory())

