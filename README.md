# PythonNameLookup
A web program with Python to lookup name statistics

Must do the following:

 - sudo pip install sortedcontainers  # Install sorted containers for all users
 - sudo mkdir /var/www/html/PythonNameLookup
 - sudo chown ubuntu /var/www/html/PythonNameLookup/
 - sudo apt install libcgicc-dev
 - sudo chmod 777 /usr/lib/cgi-bin/
 - sudo a2enmod cgi. # enable cgi
 - sudo systemctl restart apache2

Then use use "make" to set it up.
