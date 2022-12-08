from dbMgmt import sqlInteraction

class userinfo():
    print("User info")

    def __init__(self,username,gender,name,age):
        self.username = username
        self.gender = gender
        self.name = name
        self.age = age
        print('User Account Created')
    
    # Takes in user input and save as profile info
    def userinput():
        profile_info = ['','','','']
        profile_text = ['username', 'gender', 'name', 'age']
        # profile_text = ['username', 'gender', 'name', 'age', 'height', 'ethnicity', 'school', 'workplace', 'job title', 'religion', 'political tendency', 'dating goals', 'sexual preferences']

        # Asking user input
        i = 0
        while i < len(profile_info):
            profile_info[i] = input("Please type in " + profile_text[i] + ": ")
            i+=1

        user1 = userinfo(username=profile_info[0],gender=profile_info[1],name=profile_info[2],age=profile_info[3])
        sqlInteraction.command.insertData(profile_info)

    def getuserinfo():
        print('Get user info')
