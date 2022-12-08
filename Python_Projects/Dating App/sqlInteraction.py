import abc
import pdb
import sys
import mysql
import mysql.connector as mysqlConnector

class command():
    mydb = ''
    mycursor = ''

    def connect():
        print('Connecting to SQL...')
        command.mydb = mysql.connector.connect(host = "localhost",user = "root",passwd = "Xotjsrla!123456789%",database="dating_app")
        command.mycursor = command.mydb.cursor() # cursor method: Acts as a pointer

    def insertData(profile_info):
        print('Inserting Data to SQL')
        print(command.mycursor)
        print(command.mydb)
        # command.mycursor.execute("INSERT INTO user_profile (username, gender, name, age) VALUES (%s,%s,%s,%s)", ('xyz_5', 'M', 'Sun Kim', 32))
        command.mycursor.execute("INSERT INTO user_profile (username, gender, name, age) VALUES (%s,%s,%s,%s)",(profile_info[0], profile_info[1], profile_info[2], profile_info[3]))
        # command.mydb.commit()

    def pullData():
        print('Pulling data...')
        command.mycursor.execute("SELECT * FROM user_profile")
        result = command.mycursor.fetchall()
        for x in result:
            print(x)

    def deleteData():
        print('Deleting data...')
        command.mycursor.execute("DELETE FROM user_profile")
