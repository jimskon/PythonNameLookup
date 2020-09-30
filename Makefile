#MakeFile to build and deploy the Sample US CENSUS Name Data using ajax
# For CSC3004 Software Development
user = skon


all: PutCGI PutHTML

PutCGI:
	chmod 757 namelookup.py
	cp namelookup.py /usr/lib/cgi-bin/$(user)_namelookup.py

	echo "Current contents of your cgi-bin directory: "
	ls -l /usr/lib/cgi-bin/

PutHTML:
	cp namelookup.html /var/www/html/class/softdev/$(user)/pNames/
	cp namelookup.css /var/www/html/class/softdev/$(user)/pNames/
	cp namelookup.js /var/www/html/class/softdev/$(user)/pNames/

	echo "Current contents of your HTML directory: "
	ls -l /var/www/html/class/softdev/$(user)/pNames/
