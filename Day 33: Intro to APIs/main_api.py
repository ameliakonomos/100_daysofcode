import requests
from datetime import datetime
import smtplib
import time

my_email = "alkonomos@gmail.com"
my_password = "mypass"

my_lat = 34.066631
my_long = -118.439568

#check if ISS is overhead
def is_iss_overhead():
    #make a request to ISS API
    data_response = requests.get(url="http://api.open-notify.org/iss-now.json")

    #check for api error
    data_response.raise_for_status()

    #get the actual data
    my_data = data_response.json()
    data_longitude= float(my_data["iss_position"]["longitude"])
    data_latitude = float(my_data["iss_position"]["latitude"])

    # if ISS is close to current position and it is night time, trigger true
    if my_lat - 5 <= data_latitude <= my_lat + 5 and my_long - 5 <= data_longitude <= my_long + 5:
        return True

def is_night():

    #API parameters
    parameters= {
        "lat": my_lat,
        "lng": my_long,
        "formatted": 0,
    }

    #sunrise sunset API
    sun_data = requests.get(url=" https://api.sunrise-sunset.org/json", params=parameters)
    sun_data.raise_for_status()
    sun_data = sun_data.json()
    sunrise = sun_data["results"]["sunrise"]
    sunset = sun_data["results"]["sunset"]
    #get current UNIX time
    current_time = datetime.now()

    # isolate hour times using split
    sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
    sunset_hour = int(sunset.split("T")[1].split(":")[0])
    current_hour = current_time.hour

    if current_hour >= sunset_hour or current_hour <= sunrise_hour:
        #night time
        return True

while True:
    time.sleep(60)
    #send email to say look up
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg="Look up!!"
        )










