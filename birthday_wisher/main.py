from datetime import datetime
import pandas
import random
import smtplib
EMAIL = "farhan.kingshuq124@gmail.com"
PASSWORD = "#########"
today = datetime.now()
today_tuple = (today.month,today.day)
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month,data_row.day):data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]",birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=EMAIL,password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,to_addrs=birthday_person["email"],msg=f"Subject:Happy Birthday\n\n{content}")
        connection.close()
