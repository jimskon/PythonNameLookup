# PythonNameLookup
Set up Apache 2 for CGI
https://code-maven.com/set-up-cgi-with-apache

Must install libraries for www-data!
-sudo mkdir /var/www/.local
-sudo mkdir /var/www/.cache
-sudo chown www-data.www-data /var/www/.local
-sudo chown www-data.www-data /var/www/.cache
-sudo -H -u www-data pip3 install sortedcontainers
