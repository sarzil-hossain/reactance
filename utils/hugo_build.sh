#!/bin/sh

for d in .hugo_sites_build/*; do
	uname=$(echo $d | rev | cut -d / -f 1 | rev)
	cd $d && hugo && cd ../..
	mv $d/public .built_sites/$uname
done;
