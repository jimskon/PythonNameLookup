#MakeFile to build and deploy the Sample US CENSUS Name Data using ajax
# For CSC3004 Software Development

# Put your user name below:
USER= skon

all: PutCGI PutHTML

PutCGI:
	chmod 757 namelookup.py
	cp namelookup.py /usr/lib/cgi-bin/$(USER)_namelookup.py

	echo "Current contents of your cgi-bin directory: "
	ls -l /usr/lib/cgi-bin/

PutHTML:
	cp namelookup.html /var/www/html/class/softdev/$(USER)/python/
	cp namelookup.css /var/www/html/class/softdev/$(USER)/python/
	cp namelookup.js /var/www/html/class/softdev/$(USER)/python/

	echo "Current contents of your HTML directory: "
	ls -l /var/www/html/class/softdev/$(USER)/python/
