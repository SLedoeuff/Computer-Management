# -*- coding: utf-8 -*-

import psutil
import os
import array
from lxml import etree
import commands
from subprocess import call

cpu_use=psutil.cpu_percent()
diskuse=psutil.disk_usage('/').percent
ram_used=psutil.virtual_memory().percent

base="/"

values = str(cpu_use)
valuess= str(diskuse)
valuesss= str(ram_used)

info = etree.Element("info")

date = etree.SubElement(info, "date")
date.text=base

CPU = etree.SubElement(info, "CPU")
CPU.text=values

Nom_Machine = etree.SubElement(info, "Nom_Machine")
Nom_Machine.text=base

disque = etree.SubElement(info, "disque")
disque.text=valuess

RAM = etree.SubElement(info, "RAM")
RAM.text=valuesss

nb_process = etree.SubElement(info,"nombre_process")
nb_process.text=base

nb_process_system = etree.SubElement(info,"nombre_process_systeme")
nb_process_system.text=base

nb_process_user = etree.SubElement(info,"nombre_process_user")
nb_process_user.text=base

utilisateurs = etree.SubElement(info, "utilisateurs")
utilisateurs.text=base

xmlTemp=str(etree.tostring(info,pretty_print=True))

host=commands.getoutput('hostname')
fname="info_"+host+".xml"
with open(fname,"w") as test:
	test.write(xmlTemp)


call(["python","sonde2.py"])

call(["sh","verifPUs.sh"])