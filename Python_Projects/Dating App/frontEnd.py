# dating_app project
# To Do List
# Object Instantiation (Review)
# Get info from SQL and build functions to match

import sys
import pdb
import mysql
import mysql.connector as mysqlConnector
import userInteraction
from dbMgmt import sqlInteraction
# Alt: sys.path.append("C:/Users/tjsxo/OneDrive/Documents/Main_Work/Programming/Python Projects/DatingApp/dbMgmt")
def main():
    print('Main')
    sqlInteraction.command.connect()
    userInteraction.userinfo.userinput()
    sqlInteraction.command.pullData()
main()