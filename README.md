Voici, séparé en deux dossier, le système de surveillance de parc informatique, dans le cadre du projet
d'administration des systemes.

Voici dans l'ordre demandé par le sujet ce que chacun des fichier et script font, à qui ils sont déstiné, dans
quel dossier les mettre, et potentiellement quelles modifications il faut apporter. La liste des différentes
librairies utiliser sera disponible à la fin de ce document.*



Partie I: Collecte d'information

les extracteurs d'informations sont dans le dossier coté machine, c'est à dire les autres machine que celui
qui administrera le parc. Il s'agit la de les mettre dans /usr/local/bin, et ensuite de modifier le crontab grâce à la 
commande suivante:

crontab < <(crontab -l; echo"*/5 * * * * /usr/local/bin/sonde1.py")

Ces script se lanceront toutes les 5 minutes, et vont créer un fichier info.xml contenant la totalité des informations
nécéssaires et utiles au projet.





Partie II: Stockage et Collecte Web

Pour le stockage, nous avons opté pour des fichiers XML. Malgré qu'ils soient un petit peu moins facile à
manipuler qu'une base de données, ça a l'avantage d'etre facilement lisible pour quiconque si il venait
à avoir besoin de le lire avec un editeur de texte par exemple. Le fichier de données de l'administrateur se nomme data.xml

Comme dit précédement, les sondes vont créer un fichier xml contenant les informations sur l'état de la machine et
celles-ci seront lu par l'administrateur via le fichier Menu.py.

Menu.py : Il s'agit d'une petite interface interactive en couleur qui permet d'utiliser toute les fonctions dont on peut avoir besoin comme par exemple la recupération des alertes du CERT.


La "base de données" xml sera effacée de ces données trop vieille chaque jour (données remontant à un mois en arrière)
via le script EraseOld.py. Ce script aussi sera à editer dans le crontab via la commande (dans le terminal):

crontab < <(crontab -l; echo"*/5 * * * * /home/EraseOld.py")

De plus, les données sont stockées sur le disque dur de la machine de l'administrateur.






Partie III: Affichage et Alerte

Comme dis précedement, un affichage interactif et en couleur est disponible via
Menu.py et permet d'effectuer les verifications des états des machines du parc. 
Elle permet entre autre de:
	-Regarder le dernier état d'une machine données, parmis celles présentes
	-Créer un graphe au format svg (ouverture possible via un navigateur quelconque) de la machine souhaitée contenant tous les état recensés de la machine.
	-Ajouter une machine au réseau (Options détaillées juste après)
	-Affichage des dernières alertes du CERT
	-Une sauvegarde et un chargement des données

Afin de ne pas pas faire trop de traitement de données ou de modifier le code, deux fichier, machines.txt et ipmach.txt sont
la pour recenser toute les machines présentes dans le parc. Donc en cas d'ajout d'une machine sur le reseau, il faut passer
par le remplissage de la liste des machines en écrivant son nom ainsi que son ip(privée).

Un module de détection de crise et d'envoi de mail automatique à aussi été mis en place, via le fichier AlertMachine.py.
Celui ci devra etre ajouter au crontab coté administrateur via la commande:

crontab < <(crontab -l; echo"*/5 * * * * /usr/local/bin/AlertMachine.py")

Il lira la "base de données" xml toute les 5 minutes (après chaque ajout d'une information des machines) et envoi un mail
automatiquement en cas de situation de crise. Pour la configuration de la situation de crise, il y à un fichier 
config_alert.xml qui contient celle ci. Elle sont modifiable par n'importe qui ne connaissent pas l'informatique, il ne
s'agit la pas de modification de code. Mais un petit fichier à part est associé à ce fichier afin que vraiment tout le
monde puisse le modifier sans soucis il se nomme readme_alerte. De plus, un fichier template skeleton.txt contient le contenu
des mail , il est éditable à n'importe quel moment.





Partie IV: Communication

Maintenant, pour que les informations des machines passent du coté machine au coté administrateur, nous avons utilisé scp, qui
permet la copie de fichier d'une machine à une autre.
Le protocole utilisé est SSH. 
Via le script GetData.py, on récupère le fichier info_NomMachine.xml de la machine, ou NomMachine est simplement son nom, et on ajoute cette information à data.xml. 
Et il n'y a pas de risque de doublons d'informations via cette methode, car l'information envoyée coté client écrit le fichier
info_NomMachine.xml toutes les 5 minutesutes, et sachant que cette récupération se fera toute les 5 minutesutes
(sur chaque machines du parc) toutes les informations seront récoltées une fois. Ce script sera lancé automatiquement
via le crontab, qu'il faut editer du coté admin via la commande:

crontab < <(crontab -l; echo"*/5 * * * * /usr/local/bin/GetData.py")

Aussi, tout les fichier, qu'ils soient du coté admin ou du coté machine, sont dans le dossier /home
(la ou le travail à été fait)



Les librairies qui ont été utilisées durant ce projet sont:  
	-BeautifulSoup4  
	-lxml  
	-commands  
	-subprocess  
	-psutil  
	-os  
	-array  
	-smtplib   
	-getpass   
	-sys  
	-urllib2  
	-pygal  
	-re  

Le script Dependencies.sh sert à installer les librairies qui ne sont pas installées de base.
