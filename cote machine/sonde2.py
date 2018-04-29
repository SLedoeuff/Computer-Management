import os
import commands
from subprocess import call

date1=commands.getoutput('date +%d\ ')
date2=commands.getoutput('date +%m\ ')
date3=commands.getoutput('date +%Y\ %H:%M')
host=commands.getoutput('hostname')

file="info_"+host+".xml"

var="s/<date>\/<\/date>/<date>"+date1[:-1]+"\/"+date2[:-1]+"\/"+date3+"<\/date>/g"
call(["sed", "-i","-e",var,file])

var2="s/<Nom_Machine>\/<\/Nom_Machine>/<Nom_Machine>"+host+"<\/Nom_Machine>/g"
call(["sed", "-i","-e",var2,file])
