# -*- coding: utf-8 -*-

from lxml import etree
from subprocess import call
import os
import smtplib
import getpass
import sys

tree = etree.parse("data.xml")

tabD=[]
#affichage des dates
for date in tree.xpath("/infos/info/date"):
    tabD.append(date.text)

tabNM=[]
#affichage de la machine concernée
for Nom_Machine in tree.xpath("/infos/info/Nom_Machine"):
	tabNM.append(Nom_Machine.text)

tabC=[]
#affichage du CPU
for CPU in tree.xpath("/infos/info/CPU"):
	tabC.append(CPU.text)

tabDI=[]
#affichage utilisation disque
for disque in tree.xpath("/infos/info/disque"):
	tabDI.append(disque.text)

tabR=[]
#affichage de la RAM
for RAM in tree.xpath("/infos/info/RAM"):
	tabR.append(RAM.text)

tabNP=[]
#affichage du nombre de process
for nombre_process in tree.xpath("/infos/info/nombre_process"):
	tabNP.append(nombre_process.text)

tabNPS=[]
#affichage du nombre de process system
for nombre_process_systeme in tree.xpath("/infos/info/nombre_process_systeme"):
	tabNPS.append(nombre_process_systeme.text)

tabNPU=[]
#affichage du nombre de process system
for nombre_process_user in tree.xpath("/infos/info/nombre_process_user"):
	tabNPU.append(nombre_process_user.text)

tabU=[]
#affichage du nombre d'utilisateurs
for utilisateurs in tree.xpath("/infos/info/utilisateurs"):
	tabU.append(utilisateurs.text)


tree = etree.parse("config_alerte.xml")
for alert in tree.xpath("/config/CPU"):
	alertCPU=alert.text

for alert in tree.xpath("/config/RAM"):
	alertRAM=alert.text

for alert in tree.xpath("/config/Dsk"):
	alertDSK=alert.text

for alert in tree.xpath("/config/Process"):
	alertPRS=alert.text

for alert in tree.xpath("/config/User"):
	alertUSR=alert.text


def mail(type,machine):
	mail = 'gmail'
	user = 'put mail here'
	passwd = 'put password here'
	nomac = machine

	to = 'put email here'
	subject = 'SYSTEM ALERT !!! '+type
	# body = 'AN ALERT HAS BEEN SEND FROM THE MACHINE : ' + nomac
	with open('skeleton.txt', 'r') as myfile:
	    body=myfile.read().replace('\n', '') + nomac
	try:
	    mail = smtplib.SMTP('smtp.gmail.com',587)
	    #mail = smtplib.SMTP('smtpz.univ-avignon.fr',465)
	    mail.ehlo()
	    mail.starttls()
	    mail.login(user,passwd)
	    msg = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
	    mail.sendmail(user,to,msg)
	    sys.stdout.flush()
	    mail.quit()
	except KeyboardInterrupt:
	    print '[-] Canceled'
	    sys.exit()
	except smtplib.SMTPAuthenticationError:
	    print '\n[!] The username or password you entered is incorrect.'
	    sys.exit()




alrtC=[]
alrtR=[]
alrtDI=[]
alrtNP=[]
alrtU=[]


j = len(tabD)
for i in range(0, j):
	if(float(tabC[i]) > float(alertCPU)):
		alrtC.append(tabD[i])

	if(float(tabR[i]) > float(alertRAM)):
		alrtR.append(tabD[i])

	if(float(tabDI[i]) > float(alertDSK)):
		alrtDI.append(tabD[i])

	if(float(tabNP[i]) > float(alertPRS)):
		alrtNP.append(tabD[i])

	if(float(tabU[i]) > float(alertUSR)):
		alrtU.append(tabD[i])


j = len(alrtC)
if(int(j) >= int(1)):
	for i in range(0, j):
		mail("CPU ALERT",alrtC[i])

j = len(alrtR)
if(int(j) >= int(1)):
	for i in range(0, j):
		mail("RAM ALERT",alrtR[i])

j = len(alrtDI)
if(int(j) >= int(1)):
	for i in range(0, j):
		mail("Disk ALERT",alrtDI[i])

j = len(alrtNP)
if(int(j) >= int(1)):
	for i in range(0, j):
		mail("Process ALERT",alrtNP[i])

j = len(alrtU)
if(int(j) >= int(1)):
	for i in range(0, j):
		mail("User ALERT",alrtU[i])
