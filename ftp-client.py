from ftplib import FTP

ftp = FTP('')
cont = True;
while cont:
	command = input("Input a command: ")
	split = command.split()
	for s in split:
		print(s)
	if split[0] == "CONNECT":
		ftp.connect(split[1],int(split[2]))
		ftp.login(user='Owner', passwd = '1234')
		ftp.cwd('')
	if split[0] == "STORE":
 		ftp.storbinary('STOR '+ split[1], open(split[1], 'rb'))
	if split[0] == "RETRIEVE":
 		localfile = open(split[1], 'wb')
 		ftp.retrbinary('RETR ' + split[1], localfile.write, 1024)
 		localfile.close()
	if split[0] == "LIST":
		ftp.retrlines('LIST')
	if split[0] == "QUIT":
		ftp.quit()
		cont = False