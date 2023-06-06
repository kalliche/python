import os
import random
import smtpd

def automatic_email():
    user = input('Ingrese su nombre >>: ')
    email = input('Ingrese su correo >>: ')
    message = (f'Dear {user} welcome to Thecleverprogramer')
    s = smtpd.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login()
    s.login('Your Gmail Account', 'Your App Password')
    s.sendmail('&&&&&&&&', email, message)
    print('Email Sent!')

automatic_email()