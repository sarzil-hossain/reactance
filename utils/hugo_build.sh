#!/bin/sh
[ $(pwd | rev | cut -d '/' -f 1 | rev) != "reactance" ] && echo Please run from reactance directory && exit 1

for d in .hugo_sites_build/*; do
	uname=$(echo $d | rev | cut -d / -f 1 | rev)
	cd $d && hugo && cd ../..
	mv $d/public .built_sites/$uname
done;
