from smtplib import SMTPException
import getpass
import smtplib
print "Login: "
sender = raw_input("Enter Google email id: ");
password = getpass.getpass("Password: ")
receivers = raw_input("Reciever(s): ").split()
sub = raw_input("Subject: ")
txt = raw_input("Message: ")
message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: This is test 
This is a test mail 
"""
try:
   smtpObj = smtplib.SMTP('smtp.gmail.com',587)
   smtpObj.ehlo()
   smtpObj.starttls()
   smtpObj.ehlo()
   smtpObj.login(sender,password)
   smtpObj.sendmail(sender, receivers, message)
   smtpObj.quit()         
   print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"
