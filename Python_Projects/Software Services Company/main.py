#import commonfunctions
from departments import engineering
from departments import finance
from departments import hr
from departments import product_mgt
from departments import clientservices

#packages
import pdb
import json

'''
To Do
OOP Concepts: Abstract Class, Encapsulation, Inheritance, Method Overloading/Overriding - Complete
'''

'''
Project Description: This project is a model of a software services company that provides 4 different services such as ML, Automation, Data Modeling and Cloud Build
Functions
- Interacts with the client to check if new or existing customer
- Retrieve relevant info from customer
- Checks if the customer data pkl file exists
- Prints out any existing product record of the customer to the developer
- Consulting department asks user to describe the nature of the problem, expected duration and the cost 
- Based on user's selection of the service category, send the description to each team and receive team's consulting report 
- Consulting report will be shown to the customer for approval or denial 
- If accepted creates a general/specific product object and create a product data pkl file that contains the customer's name
- Income generated from consulting and net profit by providing service will be added to the total revenue
- Create HR employee information and deduct any salary from the total revenue
'''

def main():
    clientservices.clientservices.clientinteraction()
    hr.instantiateObjects()
main()