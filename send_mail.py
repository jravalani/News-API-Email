import smtplib, ssl
import os
import config


def send_mail(message):
    host = "smtp.gmail.com"
    port = 465
    username = "jay.ravalani746@gmail.com"
    password = config.password
    receiver = "jay.ravalani746@gmail.com"

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending mail: {e}")
