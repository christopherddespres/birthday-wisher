import datetime as dt
import smtplib
import pandas
import random

gmail_smtp = "smtp.gmail.com"
gmail_email = "programtestingCD@gmail.com"
gmail_password = "vcmz komb kbpo vjuv"


def send_email(recipient_name, recipient_email, letter_content):
    with smtplib.SMTP(gmail_smtp) as connection:
        connection.starttls()
        connection.login(user=gmail_email, password=gmail_password)
        connection.sendmail(from_addr=gmail_email, to_addrs=recipient_email,
                            msg=f"Subject:Happy Birthday {recipient_name}!!\n\n"
                                f"{letter_content}")


def create_letter(swap_name):
    random_letter = f"letter_templates/letter_{random.randint(1,3)}.txt"
    custom_letter = open(random_letter, "r")
    text = custom_letter.read()

    return text.replace("[NAME]", swap_name)


now = dt.datetime.now()
month = now.month
day = now.day

data = pandas.read_csv("birthdays.csv")

for index, row in data.iterrows():
    if row["month"] == month and row["day"] == day:
        name = row['name']
        email = row['email']
        letter = create_letter(name)
        print(f"Sending letter to {row['name']} at {row['email']}")
        send_email(name, email, letter)

# Extra Hard Starting Project
# 1. Update the birthdays.csv - DONE
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.
