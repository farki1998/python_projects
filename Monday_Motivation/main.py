import smtplib
import datetime as dt
import random
now = dt.datetime.now()
weekday = now.weekday()
if weekday==0:
    with open("quotes.txt") as quote:
        all_quotes = quote.readlines()
        ran_quote = random.choice(all_quotes)
    print(ran_quote)
my_email = "fkingshuq@gmail.com"
password = "#############"
connection = smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(from_addr=my_email,to_addrs="phuonganhdang2710@gmail.com",msg=f"Subject:Monday Motivation\n\n{ran_quote}")
connection.close()
