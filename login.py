import pymail
import sys
import getpass

def getDetails():
	uname = raw_input("Login id: ")
	password = getpass.getpass("Password: ")
	return uname, password

def getPass():
	password = getpass.getpass("Password: ")
	return password


if(len(sys.argv)==1):
	getDetails()
else:
	print "Hello"
