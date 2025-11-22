

from datetime import date, datetime, time, timedelta
import time
import csv

rn = datetime.now()
print(rn.day)
tax_collectee = ["one", "two","three"] 
print(len(tax_collectee))


def payment_time():
    count = 0
    with open('users.csv','r', newline="") as vic:
        list = []
        ledger = csv.reader(vic)
        for x in ledger:
            count = count + 1
            list.append(x)
        if not (list): # ¯\_(ツ)_/¯
            return("Error, No name on list")
        else:
            name = list[0]
            # remove first item of list
            list.pop(0)
            # add item back to list at end 
            list.append(name)
            with open('users.csv', 'w', newline="") as overwrite:
                overwriter = csv.writer(overwrite)
                for x in list:
                    overwriter.writerow(x)
            # write to users.csv
    return name
print(payment_time())







