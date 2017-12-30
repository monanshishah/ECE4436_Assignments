import smtplib
import uuid
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
import os

#Monanshi Shah - 250855901
#Ryan Hellowell - 250841733


# Ask user to input email for authentication
username = input('Enter your username: ')
# Ask user to input password for authentication
password = input('Enter your password: ')
# Ask for the recipient email
recipient = input("Enter the recipient: ")


# Attach the image to the email
def attachImage(img_dict):
    with open(img_dict['path'], 'rb') as file:
        picture = MIMEImage(file.read(), name = os.path.basename(img_dict['path']))
        picture.add_header('Content-ID', '<{}>'.format(img_dict['cid']))
    return picture


# Generate the email with the picture
def generateEmail(gmail_user, to_list, img1):
    msg = MIMEMultipart('related')
    msg['Subject'] = Header(u'ECE4436 - Lab 3: Monanshi Shah, Ryan Hellowell', 'utf-8')
    msg['From'] = username
    msg['To'] = recipient
    msg_alternative = MIMEMultipart('alternative')
    msg_text = MIMEText(u'Sorry the image is not loading', 'plain', 'utf-8')
    msg_alternative.attach(msg_text)
    msg.attach(msg_alternative)
    msg_html = u'I love computer networks!'
    msg_html = MIMEText(msg_html, 'html', 'utf-8')
    msg_alternative.attach(msg_html)
    msg.attach(attachImage(img1))
    return msg

# Set up sending all the necessary commands to send the message
def sendMail(msg, username, password, to_list):
    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(username, password)
    mailServer.sendmail(username, to_list, msg.as_string())
    mailServer.quit()

# Do the final preparations and send the email to the recipient
img1 = dict(title = 'Image 1', path = '171.jpg', cid = str(uuid.uuid4()))
email_msg = generateEmail(username, [recipient], img1)
sendMail(email_msg, username, password, [recipient])
