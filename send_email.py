from email.mime.text import MIMEText
import smtplib

def send_email(email, height, average_height, ppl_count):
    from_email = '@gmail.com'
    from_password = ''
    to_email = email
    
    subject = 'Height data'
    message = 'Hey there, your height is <strong>%s</strong>. Average height of all is <strong>%s</strong> and that is calculated out <strong>%s</strong> of people.' % (height, average_height, ppl_count)

    msg = MIMEText(message, 'html')
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
