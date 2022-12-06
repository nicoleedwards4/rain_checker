import requests
import smtplib

OWM_endpoint = "https://api.openweathermap.org/data/3.0/onecall"
API_KEY = ""
my_gmail = "necodetesting@gmail.com"
gmail_pw = ""

parameters = {
    "lat": 47.252940,
    "lon": -122.316230,
    "exclude": "current,minutely,daily",
    "appid": API_KEY
}

response = requests.get(OWM_endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_data = weather_data["hourly"][:12]

for hour in weather_data:
    if int(hour["weather"][0]["id"]) < 700:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_gmail, password=gmail_pw)
            connection.sendmail(
                from_addr=my_gmail,
                to_addrs="necodetesting@yahoo.com",
                msg=f"Subject:Bring an umbrella\n\nIt's going to rain today, bring an umbrella")
        break
