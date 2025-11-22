import csv
from csv import writer
import pandas as pd

def total_users():
    with open('users.csv','r', newline='') as file:
        reader = csv.reader(file)
        count = sum(1 for col in reader)
        return count

def add_user(user):
    print("Add User Ran")
    with open('users.csv', '+a', newline="") as write:
        appender = writer(write)
        appender.writerow([user])
        
    
def search_user(user):
    # use for loop to go through entire CSV file, comparing the numeric entry with name
    found = []
    with open('users.csv','r', newline="") as test:
        # should typecast user to all upper/lower case letters
        read_file = csv.reader(test)
        count = 0
        for x in read_file:
            count = count + 1
            if user in x: 
                return count, True
        return count, False
    #return the entry with number 



def remove_user(user):
    print("Remove User Ran")
    new_list = []
    with open('users.csv','r', newline="") as test:
        # search for user 
        v1, v2 = search_user(user)
        user = "['" + user + "']"
        # Above returns T/F and row where user is 
        if v2 == True: 
            observer = csv.reader(test)
            for row in observer:
                if str(row) != user:
                    # print(str(row))
                    # print(user)
                    new_list.append(row)
                    with open('users.csv','w', newline="") as story_teller:
                        writer = csv.writer(story_teller)
                        writer.writerows(new_list)
            #take new_list and rewrite csv file
        else:
            print("not possible")
        # handle case handling if false 
        # delete row if true 
        
        #BONUS; have program check if user is deleted by running search User again 
        

