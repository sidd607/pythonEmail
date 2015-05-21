from os.path import expanduser

def buildList():
	home = expanduser("~")
	home += "/.pymail/smtp.data"
	smtpData = {}
	database = open(home,"rw+")
	line = ""
	data = []
	line = database.readline()
	while line != "":
#		print line
		data.append(line.split())
		temp = []
		temp.append(line.split()[1])
		temp.append(line.split()[2])
		smtpData[line.split()[0]] = temp
		line = database.readline()
	return smtpData
#	print data
#	print smtpData
def getHost(uname):
	smtpData = buildList()
	try:
		uname = uname.split("@")[1]
#		print uname
	except Exception:
		print "Enter a valid email id"
		return 1
	if(uname in smtpData):
		return smtpData[uname]
	else:
		print "smtp server data for " + uname + " doesnt exist"  
		return 1
buildList()
#print getHost("sidd@gmail.com")
#print getHost("sidd@iiitb.org")

