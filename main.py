import os
import requests
import smtplib

API_KEY = os.environ["API_kEY"]

parameters = {
    "lat": 5.545282,
    "lon": 5.821964,
    "appid": API_KEY,
    "cnt": 4,
}

my_email = os.environ["MY_EMAIL"]
my_password = os.environ["MY_PASSWORD"]

response = requests.get(
    "https://api.openweathermap.org/data/2.5/forecast",
    params=parameters,
)
response.raise_for_status()

data = response.json()

for forecast in data["list"]:
    weather_id = forecast["weather"][0]["id"]

    if weather_id > 700:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, APP_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="jonesagbramu@gmail.com",
                msg="Subject:Weather Alert\n\nGo out today with an umbrella "
            )
            break
