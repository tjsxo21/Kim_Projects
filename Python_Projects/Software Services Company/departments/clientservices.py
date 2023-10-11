import commonfunctions
from departments import engineering
from departments import product_mgt
from departments import finance

import sys
import pdb
import tkinter as tk
from tkinter import messagebox, simpledialog

root = tk.Tk()
root.withdraw()

teaminput_items_global = []

class clientservices():

    def clientinteraction():
        name = clientservices.customerrecord()
        clientinfo.printclientproductinfo(name)
        clientservices.consulting(name)

    def customerrecord():
        print("Customer Record")
        filename = "customer data.pkl"
        # Loading customer list data
        currentcustomerlist = commonfunctions.load_object(filename)

        new_customer = messagebox.askquestion("Customer Record", "Are you a new customer?")
        if new_customer == "yes":
            print("New Customer")
            name = simpledialog.askstring("Customer Info","Please type in your full name")
            phone = simpledialog.askstring("Customer Info","Please type in your phone")
            email = simpledialog.askstring("Customer Info","Please type in your email")
            job = simpledialog.askstring("Customer Info","Please type in your job")
            company = simpledialog.askstring("Customer Info","Please type in your company")
            # Create client object
            clientinfo(name,phone,email,job,company)
        else:
            print("Existing Customer. Finding Record...")
            name = simpledialog.askstring("Customer Info", "Please type in your full name")

        if currentcustomerlist is not None:
            print("Current Customer List Exists")
            clientinfo.allclient_list = clientinfo.allclient_list + currentcustomerlist
        else:
            print("Current Customer List Doesn't Exist")

        # Saves all client list to a .pkl file
        commonfunctions.save_object(clientinfo.allclient_list, "customer data.pkl")
        return name

    def consulting(customer):
        messagebox.showinfo("Info", "Please choose from the following software services category")
        menu = simpledialog.askstring("Menu Selection", "1 - Machine Learning, 2 - Automation, 3 - Data Modeling, 4 - Cloud Build")
        description = simpledialog.askstring("Request Description","Please describe the problem, expected duration and cost estimate in detail ")

        if int(menu) == 1:
            print("Transferring to Machine Learning Team")
            teaminput_items_global = engineering.ml_team.consultingservice(description)
            clientservices.finalizepurchase(teaminput_items_global)
            # Instantiating Objects
            product_mgt.product_ml(customer,teaminput_items_global[0],teaminput_items_global[1],teaminput_items_global[2],teaminput_items_global[3],
                                   teaminput_items_global[4],teaminput_items_global[5],teaminput_items_global[6])

        elif int(menu) == 2:
            print("Transferring to Automation Team")
            teaminput_items_global = engineering.automation_team.consultingservice(description)
            clientservices.finalizepurchase(teaminput_items_global)
            # Instantiating Objects
            product_mgt.product_automation(customer,teaminput_items_global[0],teaminput_items_global[1],teaminput_items_global[2], teaminput_items_global[3],
                                           teaminput_items_global[4], teaminput_items_global[5],teaminput_items_global[6])

        elif int(menu) == 3:
            print("Transferring to Data Modeling Team")
            teaminput_items_global = engineering.datamodeling_team.consultingservice(description)
            clientservices.finalizepurchase(teaminput_items_global)
            # Instantiating Objects
            product_mgt.product_datamodeling(customer,teaminput_items_global[0],teaminput_items_global[1],teaminput_items_global[2],teaminput_items_global[3],
                                             teaminput_items_global[4],teaminput_items_global[5],teaminput_items_global[6])

        elif int(menu) == 4:
            print("Transferring to Cloud Build Team")
            teaminput_items_global = engineering.cloudbuild_team.consultingservice(description)
            clientservices.finalizepurchase(teaminput_items_global)
            # Instantiating Objects
            product_mgt.product_datamodeling(customer,teaminput_items_global[0],teaminput_items_global[1],teaminput_items_global[2],teaminput_items_global[3],
                                             teaminput_items_global[4], teaminput_items_global[5],teaminput_items_global[6])

        elif int(menu) != (1 and 2 and 3 and 4):
            print("Please type in the proper number")
            clientservices.consulting()

    def finalizepurchase(list):
        response = messagebox.askquestion('Quote','Category: '+list[0]+'\nName: '+list[1]+'\nYear: '+list[2]+'\nTeamspecs: '+list[3]+'\nQuote: $'+list[5]+'\n\nWould you like to accept the quote?')

        if response == "yes":
            print("User Accepted the Quote")
            netprofit = int(list[5]) - int(list[4])
            finance.finance.income(netprofit)
        else:
            print("User Rejected the Quote")

        root.destroy()
        root.mainloop()

class clientinfo():
    allclient_list = []

    def __init__(self,name,phone,email,job,company):
        # Appending objects to the list
        self.allclient_list.append(self)
        self.name = name
        self.phone = phone
        self.email = email
        self.job = job
        self.company = company
        print("Client Created")

    # Prints out all products the customer ordered
    def printclientproductinfo(name):
        filename = "product data.pkl"
        currentproductlist = commonfunctions.load_object(filename)

        if currentproductlist is not None:
            print("Current Product List Exists")
            for product in currentproductlist:
                if name == product.customer:
                    print(product.customer)
                    product_mgt.product_functions.basic_specs(product)
        else:
            print("Current Customer List Doesn't Exist")