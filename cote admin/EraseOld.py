from lxml import etree
from subprocess import call
import commands

tree = etree.parse("data.xml")

tabD=[]

for date in tree.xpath("/infos/info/date"):
    tabD.append(date.text)

tabNM=[]

for Nom_Machine in tree.xpath("/infos/info/Nom_Machine"):
	tabNM.append(Nom_Machine.text)

tabC=[]

for CPU in tree.xpath("/infos/info/CPU"):
	tabC.append(CPU.text)

tabDI=[]

for disque in tree.xpath("/infos/info/disque"):
	tabDI.append(disque.text)

tabR=[]

for RAM in tree.xpath("/infos/info/RAM"):
	tabR.append(RAM.text)

tabNP=[]

for nombre_process in tree.xpath("/infos/info/nombre_process"):
	tabNP.append(nombre_process.text)

tabNPS=[]

for nombre_process_systeme in tree.xpath("/infos/info/nombre_process_systeme"):
	tabNPS.append(nombre_process_systeme.text)

tabNPU=[]

for nombre_process_user in tree.xpath("/infos/info/nombre_process_user"):
	tabNPU.append(nombre_process_user.text)

tabU=[]

for utilisateurs in tree.xpath("/infos/info/utilisateurs"):
	tabU.append(utilisateurs.text)


date1=commands.getoutput('date +%d ')
date2=commands.getoutput('date +%m ')
date3=commands.getoutput('date +%Y ')

call(["touch","tmp.xml"])
with open("tmp.xml","w") as test:
	test.write("<?xml version='1.0' encoding='utf-8' ?>\n")
	test.write("<infos>\n")


j = len(tabD)
for i in range(0, j):
	jma=tabD[i][:-6]
	jour=jma[0]+jma[1]
	mois=jma[3]+jma[4]
	an=jma[6]+jma[7]+jma[8]+jma[9]
	# if 2016 <= 2015+1   si on est sur la meme annee, et dans le cas de la fin d'annee
	if( int(date2) <= int(mois)+1 ):
		#if 05 < 04+1    si on est le meme mois ou le mois precedent + cas de decembre
		if(mois==12):
			mois=0
			an+=1

		if( int(date3) <= int(an) ):
			#info vieille de moins de 2 mois
			info = etree.Element("info")

			date = etree.SubElement(info, "date")
			date.text=tabD[i]

			CPU = etree.SubElement(info, "CPU")
			CPU.text=tabC[i]

			Nom_Machine = etree.SubElement(info, "Nom_Machine")
			Nom_Machine.text=tabNM[i]

			disque = etree.SubElement(info, "disque")
			disque.text=tabDI[i]

			RAM = etree.SubElement(info, "RAM")
			RAM.text=tabR[i]

			nb_process = etree.SubElement(info,"nombre_process")
			nb_process.text=tabNP[i]

			nb_process_system = etree.SubElement(info,"nombre_process_systeme")
			nb_process_system.text=tabNPS[i]

			nb_process_user = etree.SubElement(info,"nombre_process_user")
			nb_process_user.text=tabNPU[i]

			utilisateurs = etree.SubElement(info, "utilisateurs")
			utilisateurs.text=tabU[i]

			var=str(etree.tostring(info,pretty_print=True))

			with open("tmp.xml","r") as test:
				pre = ''.join(test.readlines())

			with open("tmp.xml","w") as test:
				test.write(pre+var+"\n")


with open("tmp.xml","r") as test:
	pre = ''.join(test.readlines())

with open("tmp.xml","w") as test:
	test.write(pre+"</infos>")

with open("tmp.xml","r") as test:
	pre = ''.join(test.readlines())

with open("data.xml","w") as test:
	test.write(pre)

call(["rm","tmp.xml"])