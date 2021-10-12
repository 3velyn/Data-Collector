from email.mime.text import MIMEText
import smtplib

def send_email(email, height):
    from_email = '@gmail.com'
    from_password = ''
    to_email = email
    
    subject = 'Height data'
    message = 'Hey there, your height is <strong>%s</strong>.' % height

    msg = MIMEText(message, 'html')
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
