from smtplib import SMTPException
import getpass
import smtplib
print "Login: "

def getHost(domain):
	dMap={}
	dMap["gmail.com"] = ['smtp.gmail.com','587']
	dMap["yahoo.com" ] = ['','']
	if domain in dMap:
		return dMap[domain]
	else:
		return 0

def func():
    sender = raw_input("Enter Google email id: ");
    host = ""
    port = 0
    try:
        server = sender.split("@")[1]
	if getHost(server) != 0:
		host = getHost(server)[0]
		post = getHost(server)[1]	
	else:
		print "host: " + server + " Not yet defined"
		return 0
    except Exception:
        print "Enter a valid email Address"
        func()
	return 0
    print server
    password = getpass.getpass("Password: ")
    receivers = raw_input("Reciever(s): ").split()
    sub = raw_input("Subject: ")
    txt = raw_input("Message: ")
    message = "From: From <from@fromdomain.com>\n"+"To: To Person <to@todomain.com>\n"+"Subject: "+sub+"\n"+txt
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


func()
