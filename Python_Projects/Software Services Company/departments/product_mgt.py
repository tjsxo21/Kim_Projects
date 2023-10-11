# Application: Abstract class/methods, inheritance

from abc import ABC, abstractmethod
import pdb
import commonfunctions

class product_functions:

    def basic_specs(self):
        print('Product Specs: ' + '\n' + str(self.customer) + '\n' + str(self.category) + '\n' + str(self.name) + '\n' + str(
            self.year) + '\n' + str(self.teamspecs) + '\n' + str(self.totalcost) + '\n' + str(self.listprice) + '\n' + str(self.desc))

    def productspecs(list):
        for object in list:
            print(product_functions.basic_specs(object))

    def saveproductdata():
        print("Saving product data to a file...")
        filename = "product data.pkl"
        currentproductlist = commonfunctions.load_object(filename)

        if currentproductlist is not None:
            print("Current Product List Exists")
            product.allproduct_list = product.allproduct_list + currentproductlist
        else:
            print("Current Customer List Doesn't Exist")

        # Saves all product list to a .pkl file
        commonfunctions.save_object(product.allproduct_list, "product data.pkl")

# Abstract class/methods
class product(ABC):
    allproduct_list = []

    @abstractmethod
    def __init__(self, customer, category, name, year, teamspecs, totalcost, listprice, desc=None):
        # Appending objects to the list
        self.allproduct_list.append(self)
        self.customer = customer
        self.category = category
        self.name = name
        self.year = year
        self.teamspecs = teamspecs
        self.totalcost = totalcost
        self.listprice = listprice
        self.desc = desc
        print("Product Created")

    @abstractmethod
    def basic_specs(self):
        pass

    @abstractmethod
    def productspecs(self):
        pass

# Inheritance
class product_ml(product):
    ml_product_list = []

    def __init__(self, customer, category, name, year, teamspecs, totalcost, listprice, desc=None):
        super().__init__(customer, category, name, year, teamspecs, totalcost, listprice, desc)
        self.ml_product_list.append(self)
        print("ML Product Created")
        product_functions.saveproductdata()

    def basic_specs(self):
        print('Product Specs: ' + '\n' + str(self.customer) + '\n' + str(self.category) + '\n' + str(self.name) + '\n' + str(
            self.year) + '\n' + str(self.teamspecs) + '\n' + str(self.totalcost) + '\n' + str(self.listprice) + '\n' + str(self.desc) + '\n' + str(self.ml_traits))

    def productspecs(list):
        for object in list:
            print(product_ml.basic_specs(object))

class product_automation(product):
    automation_product_list = []

    def __init__(self, customer, category, name, year, teamspecs, totalcost, listprice, desc=None):
        super().__init__(customer, category, name, year, teamspecs, totalcost, listprice, desc)
        self.automation_product_list.append(self)
        print("Automation Product Created")
        product_functions.saveproductdata()

    def basic_specs(self):
        print('Product Specs: ' + '\n' + str(self.category) + '\n' + str(self.name) + '\n' + str(
            self.year) + '\n' + str(self.teamspecs) + '\n' + str(self.totalcost) + '\n' + str(self.listprice) + '\n' + str(self.desc) + '\n' + str(self.automation_traits))

    def productspecs(list):
        for object in list:
            print(product_automation.basic_specs(object))

class product_datamodeling(product):
    datamodeling_product_list = []

    def __init__(self, customer, category, name, year, teamspecs, totalcost, listprice, desc=None):
        super().__init__(customer, category, name, year, teamspecs, totalcost, listprice, desc)
        self.datamodeling_product_list.append(self)
        print("Data Modeling Product Created")
        product_functions.saveproductdata()

    def basic_specs(self):
        print('Product Specs: ' + '\n' + str(self.category) + '\n' + str(self.name) + '\n' + str(
            self.year) + '\n' + str(self.teamspecs) + '\n' + str(self.totalcost) + '\n' + str(self.listprice) + '\n' + str(self.desc) + '\n' + str(self.datamodeling_traits))

    def productspecs(list):
        for object in list:
            print(product_datamodeling.basic_specs(object))

class product_cloudbuild(product):
    cloudbuild_product_list = []

    def __init__(self, customer, category, name, year, teamspecs, totalcost, listprice, desc=None):
        super().__init__(customer, category, name, year, teamspecs, totalcost, listprice, desc)
        self.cloudbuild_product_list.append(self)
        print("Cloud Build Product Created")
        product_functions.saveproductdata()

    def basic_specs(self):
        print('Product Specs: ' + '\n' + str(self.category) + '\n' + str(self.name) + '\n' + str(
            self.year) + '\n' + str(self.teamspecs) + '\n' + str(self.totalcost) + '\n' + str(self.listprice) + '\n' + str(self.desc) + '\n' + str(self.cloudbuild_traits))

    def productspecs(list):
        for object in list:
            print(product_cloudbuild.basic_specs(object))