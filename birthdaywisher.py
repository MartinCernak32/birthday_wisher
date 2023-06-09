import smtplib
import datetime as dt
import random
import pandas

now = dt.datetime.now()
month = now.month
day = now.day
file_paths = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
letter = random.choice(file_paths)

with open(letter, 'r') as file:
    message = file.read()
    

birthdays_data_frame = pandas.read_csv("birthdays.csv")
birthdays_dict = birthdays_data_frame.to_dict(orient="records")

for person in birthdays_dict:
    persons_name = person['name']
    persons_birthmonth = person['month']
    persons_birthday = person['day']
    message = message.replace('[NAME]', persons_name)
    if persons_birthmonth == month and persons_birthday == day:
        message_to_send = message

my_email = "martin.cernak32@gmail.com"
password = "yrkvjdfmjbykfbdr"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#     from_addr=my_email,
#     to_addrs="crki73@gmail.com", 
#     msg=f"Subject:HAPPY BIRTHDAY\n\n{message}",
#             )

print(message_to_send) 
