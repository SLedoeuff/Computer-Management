from lxml import etree
from subprocess import call


fichier = open("machines.txt","r")
lignes = fichier.readlines()
fichier.close()
machine=[]
for ligne in lignes:
	machine.append(ligne[:-1])


fichier = open("ipmach.txt","r")
lignes = fichier.readlines()
fichier.close()
ipmachin=[]
for ligne in lignes:
	ipmachin.append(ligne[:-1])

j = len(machine)
for i in range(0, j):
	ip=ipmachin[i]
	user=machine[i]
	path="/home"
	fname="info_"+user+".xml"
	term=user+"@"+ip+":"+path+fname

	call(["scp", term, path])

	with open(fname,"r") as test:
		add = ''.join(test.readlines())

	with open("data.xml","r") as test:
		test_str = ''.join(test.readlines()[:-1])

	with open("data.xml","w") as test:
		test.write(test_str+add)
		test.write("</infos>")

	call(["rm",fname])