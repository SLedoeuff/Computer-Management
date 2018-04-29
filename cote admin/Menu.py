# -*- coding: utf-8 -*-


from lxml import etree
import pygal
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

call(["clear"])

print("\033[31m * Bienvenue ! * \033[0m \n")

def Menu():
	print("\033[32m Que souhaitez-vous faire ? \033[0m")
	print("\033[32m (saisissez le chiffre associé à la fonction et appuyez sur entrée) \033[0m")
	print("\033[34m1\033[0m - Afficher les infos d'une machine")
	print("\033[34m2\033[0m - Créer un graphe d'une machine")
	print("\033[34m3\033[0m - Ajouter une machine au reseau (A faire après que celle ci soit installée !)")
	print("\033[34m4\033[0m - Afficher les derniere alertes du CERT<non actif>")
	print("\033[34m5\033[0m - Sauvegarder les données")
	print("\033[34m6\033[0m - Charger les données sauvegarder")
	print("\033[34m0\033[0m - Quitter")
	z = raw_input('> ')
	print("\n")
	if(z == "1"):
		info_machine()
	elif(z == "2"):
		graph()
	elif(z == "3"):
		AjoutMachine()
	elif(z == "4"):
		cert()
	elif(z == "5"):
		Sauvegarde()
	elif(z == "6"):
		ChargerSauvegarde()
	elif(z == "0"):
		print("Au revoir !")
		exit()
	else:
		print("Cette catégorie n'éxiste pas !")

	Menu()

def cert():
	call(["python","call_parser.py"])

def info_machine():

	call(["clear"])
	print("Voici la liste des machines du parc :")

	fichier = open("machines.txt","r")
	lignes = fichier.readlines()
	fichier.close()

	dico=dict()
	type(dico)
	for ligne in lignes:
		dico[ligne[:-1]]="x"


	for Mach in dico:
		j = len(tabD)
		for i in range(0, j):
			if tabNM[i] == Mach:
				dico[Mach]=tabD[i]

	test=1

	while test == 1 :
		for Mach in dico:
			print(Mach)

		print("\n")
		x = raw_input('\033[32m* Quelle machine voulez vous visioner ? (Saisissez le nom de la machine)\033[0m\n')
		for Mach in dico:
			if Mach == x :
				test=0

		if test == 1 :
			print("Rentrer un nom de machine valide !")


	print("\033[0m\033[35mEtat de la machine : " + x + ", date: "+dico[x])

	j = len(tabD)
	for i in range(0, j):
		if tabNM[i] == x :
			if dico[x] == tabD[i] :
				print("CPU:"+tabC[i])
				print("RAM:"+tabR[i])
				print("Disque:"+tabDI[i])
				print("Processur executés:"+tabNP[i])
				print("Dont, en processus systeme:"+tabNPS[i])
				print("Et, en processus utilisateur:"+tabNPU[i])
				print("Utilisateurs:"+tabU[i])
				print("\033[0m\n")

	Menu()

def graph():

	call(["clear"])
	fichier = open("machines.txt","r")
	lignes = fichier.readlines()
	fichier.close()
	machin=[]
	print("Liste des machines du parc : \n")
	for ligne in lignes:
		machin.append(ligne[:-1])
		print(ligne[:-1])

		test=1


	while test == 1 :
		x = raw_input('\033[32m* De quelle machine voulez vous faire le graph ?\033[0m\n')
		print("\n")

		for thing in machin:
			if(x == thing):
				test=0

		if(test==1):
			print('Machine inexistante !')

	tabCM=[]
	tabRM=[]
	tabDM=[]

	j = len(tabD)
	for i in range(0, j):
		if tabNM[i] == x :
			tabCM.append(float(tabC[i]))
			tabRM.append(float(tabR[i]))
			tabDM.append(float(tabDI[i]))

	line_chart = pygal.Bar()
	line_chart.title = 'Informations about machine '
	line_chart.add('CPU',	tabCM)
	line_chart.add('RAM',	tabRM)
	line_chart.add('Disk',	tabDM)

	line_chart.render_to_file('StatMachine_'+x+'.svg')
	print("\033[35mGraphe créer ! Consulter StatMachine"+x+".svg\033[0m\n")
	Menu()

def AjoutMachine():

	x = raw_input('\033[32m* Quelle est le nom de la machine que vous souhaitez ajouter ?\033[0m\n')
	y = raw_input("\033[32m* Quelle est l'ip de la machine que vous souhaitez ajouter ?\033[0m\n")

	with open("machines.txt","r") as test:
		pre = ''.join(test.readlines())

	with open("machines.txt","w") as test:
		test.write(pre+x+"\n")

	with open("ipmach.txt","r") as test:
		pre = ''.join(test.readlines())

	with open("ipmach.txt","w") as test:
		test.write(pre+y+"\n")

	print("\033[35mMachine ajoutée ! :D\033[0m\n")

def Sauvegarde():
	call(["tar","cvf","backup.tar","data.xml"])
	call(["clear"])
	print("Sauvegarde effectuée !\n")

def ChargerSauvegarde():
	existTar=commands.getoutput('find -type f -name "backup.tar"')
	if(str(existTar)==""):
		print("Aucune archive !\n")
	else:
		call(["tar","xvf","backup.tar"])
		call(["clear"])
		print("Sauvegarde chargée !\n")

Menu()
