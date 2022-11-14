#MakeFile to build and deploy the Sample US CENSUS Name Data using ajax
# For CSC3004 Software Development
user = skon


all: PutCGI PutHTML

PutCGI:
	chmod 757 namelookup.py
	cp namelookup.py /usr/lib/cgi-bin/namelookup.py

	echo "Current contents of your cgi-bin directory: "
	find /usr/lib/cgi-bin/ -type f -mmin -5 -ls

PutHTML:
	cp namelookup.html /var/www/html/PythonNameLookup/
	cp namelookup.css /var/www/html/PythonNameLookup/
	cp namelookup.js /var/www/html/PythonNameLookup/
	cp -r namedata /var/www/html/PythonNameLookup/

	echo "Current contents of your HTML directory: "
	ls -l /var/www/html/PythonNameLookup/
