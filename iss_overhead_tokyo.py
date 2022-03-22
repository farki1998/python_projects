import requests
from datetime import datetime
import smtplib
import time
EMAIL = "farhan.kingshuq124@gmail.com"
PASSWORD = "##########"
MY_LAT = 35.6804
MY_LONG = 139.7690
def iss_over():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT-5<=iss_latitude<=MY_LAT+5 and MY_LONG-5<=iss_longitude<=MY_LONG+5:
        return True
def night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now>=sunset and time_now<=sunrise:
        return True
while True:
    time.sleep(60)
    if iss_over() and night():
        connection = smtplib.SMTP("smtp.gmail.com",587)
        connection.starttls()
        connection.login(user=EMAIL,password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,to_addrs=EMAIL,msg="Subject:LOOK UP!!\n\nThe International Space Station is over your head.")
        connection.close()
