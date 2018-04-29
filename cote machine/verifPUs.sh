#!/bin/bash

nbprocess=$(ps -A | wc -l)
nbprocess=$(($nbprocess - 1))

psys=$(ps -A | awk '{print ($2)}')
nbpsys=0
for elem in $psys
do
	if test $elem = '?'
	then
		nbpsys=$(($nbpsys + 1))
	fi
done


nbpuser=$(ps -u | wc -l)
nbpuser=$(($nbpuser -1))

userco=$(users | wc -w)

host=$(hostname)
prefn="info_"
suffn=".xml"
fname=$prefn$host$suffn

sed -i -e "s/<nombre_process>\/<\/nombre_process>/<nombre_process>$nbprocess<\/nombre_process>/g" $fname
sed -i -e "s/<nombre_process_systeme>\/<\/nombre_process_systeme>/<nombre_process_systeme>$nbpsys<\/nombre_process_systeme>/g" $fname
sed -i -e "s/<nombre_process_user>\/<\/nombre_process_user>/<nombre_process_user>$nbpuser<\/nombre_process_user>/g" $fname
sed -i -e "s/<utilisateurs>\/<\/utilisateurs>/<utilisateurs>$userco<\/utilisateurs>/g" $fname