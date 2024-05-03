python3 -m venv .venv
pip3 install hugo

for d in ./*/; do
	cd $d && hugo
	# remove images directories
	rm -r $d/public/images
done;
