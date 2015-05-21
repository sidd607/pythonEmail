import smtplib
import getpass
from smtplib import SMTPHeloError
from smtplib import SMTPAuthenticationError
from smtplib import SMTPException
from smtpData import getHost

class pyMail:
	server = []
	port = 25
	host = ""
	uname = ""
	password = ""
		
	def __init__(self, uname, password):
		self.uname = uname
		self.password = password

	def createObj(self):
		self.server = getHost(self.uname)
		if(self.server == 1):
			exit(1)
		smtpObj = smtplib.SMTP(self.server[0], self.server[1])
		return smtpObj

	def login(self):
		smtpObj = self.createObj()
		try:
			smtpObj.ehlo()
			smtpObj.starttls()
			smtpObj.ehlo()
			smtpObj.login(self.uname, self.password)
			smtpObj.quit()
			print "Login Successful"
		except SMTPHeloError:
			print "Server not Responding"
			return 1
		except SMTPAuthenticationError:
			print "Username / Password incorrect"
			return 1
		except SMTPException:
			print "Unknown Error occured" 
			return 1
			
		return 0
		

#Test

uname = raw_input("Email id: ")
password = getpass.getpass("Password: ")

pymail = pyMail(uname,password)
pymail.login()
