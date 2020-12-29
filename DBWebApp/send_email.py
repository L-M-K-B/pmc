from email.mime.text import MIMEText
import smtplib


def send_email(email, height, average):
    from_email = ""
    from_pw = ""

    subject = "Height data"
    message = f"Hi,<br> your height is <strong>{height} cm</strong>. <br> The average of all data is <strong>{average} cm </strong>"

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_pw)
    gmail.send_message(msg)
