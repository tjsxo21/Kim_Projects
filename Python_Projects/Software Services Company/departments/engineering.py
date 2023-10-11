from abc import ABC, abstractmethod
from departments import product_mgt
from departments import finance

teaminput_items_global = ["","","","","","",""]

class engineering_team(ABC):

    @abstractmethod
    def consultingservice():
        pass

    @abstractmethod
    def developmentwork():
        pass

    def askteaminput():
        print("Asking Team Input")

        i = 0
        category = ""
        name = ""
        year = ""
        teamspecs = ""
        totalcost = ""
        listprice = ""
        desc = ""

        teaminput_items = [category, name, year, teamspecs, totalcost, listprice, desc]
        teaminput_itemname = ["category", "name", "year", "teamspecs", "totalcost", "listprice", "desc"]

        for item in teaminput_items:
            item = input("Please type in " + teaminput_itemname[i] + " ")
            teaminput_items[i] = item
            i += 1

        return teaminput_items

class ml_team(engineering_team):

    def consultingservice(description):
        print("Machine Learning Consulting Service")
        print("Problem Description: " + description)
        print("Generating Quote...")
        finance.finance.expense(100)
        teaminput_items_global = engineering_team.askteaminput()
        return teaminput_items_global

    def developmentwork():
        print("Developing")

class automation_team(engineering_team):

    def consultingservice(description):
        print("Automation Consulting Service")
        print("Problem Description: " + description)
        print("Generating Quote...")
        finance.finance.expense(100)
        teaminput_items_global = engineering_team.askteaminput()
        return teaminput_items_global

class datamodeling_team(engineering_team):

    def consultingservice(description):
        print("Data Modeling Consulting Service")
        print("Problem Description: " + description)
        print("Generating Quote...")
        finance.finance.expense(100)
        teaminput_items_global = engineering_team.askteaminput()
        return teaminput_items_global

class cloudbuild_team(engineering_team):

    def consultingservice(description):
        print("Cloud Build Consulting Service")
        print("Problem Description: " + description)
        print("Generating Quote...")
        finance.finance.expense(100)
        teaminput_items_global = engineering_team.askteaminput()
        return teaminput_items_global