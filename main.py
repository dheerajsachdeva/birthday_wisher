##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
MY_EMAIL = "dheerajarya@gmail.com"
PASSWORD = "PUT_YOUR_PASSWORD_HERE_BY_CREATING_APP_PASSWORD"

import smtplib
import pandas
import datetime as dt
import random

today = (dt.datetime.now().month, dt.datetime.now().day)


data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    person_name = birthdays_dict[today]
    file_path = f"./letter_templates/letter_{random.randint(1,3)}.txt"
    with open (file_path) as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]", person_name["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=person_name["email"],
                            msg=f"Subject: Happy Birthday \n\n {contents}")




