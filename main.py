import smtplib
import pandas
import datetime as dt
import random
#you should enter gmail for sender email for diffrent email pls enter diffrent smtp
SENDER_EMAIL = ""
SENDER_PASSWORD=""
recipient_email = ""
recipient_name =""
#----------------------------READING LETTER FILES----------------------------#
letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
random_letter = random.choice(letters)
with open(f"letter_templates/{random_letter}", "r") as file:
    letter = file.read()
    
#-------------------------------READING CSV FILE-------------------------------#
file = pandas.read_csv("./birthdays.csv")
birthdays = file.to_dict(orient="records")

#----------------------------------------TIME-----------------------------------------#
now = dt.datetime.now()
current_month= now.month
current_day = now.day

#-------------------------------TODAY IS BIRTHDAY-----------------------------#
def birthday():
    '''Finds if today is birthday'''
    global  recipient_email
    global recipient_name
    for i in range(len(birthdays)):
        if current_month == birthdays[i]['month'] and current_day == birthdays[i]['day']:
            recipient_email = birthdays[i]['email']
            recipient_name = birthdays[i]['name']
            return  letter.replace("[NAME]", f"{recipient_name]}")
            
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)
    if birthday():
        connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=recipient_email, msg= f"Subject:Happy Birthday!\n\n{birthday()}"




