#MakeFile to build and deploy Python Shakespeare lookup
user = skon


all: PutCGI PutHTML

PutCGI:
	chmod 757 shakewebpy.py
	cp shakewebpy.py /usr/lib/cgi-bin/$(user)_shakewebpy.py

	echo "Current contents of your cgi-bin directory: "
	find /usr/lib/cgi-bin/ -type f -mmin -5 -ls	

PutHTML:
	cp shakewebpy.html /var/www/html/class/softdev/$(user)/shakewebpy/
	cp shakewebpy.css /var/www/html/class/softdev/$(user)/shakewebpy/
	cp shakewebpy.js /var/www/html/class/softdev/$(user)/shakewebpy/

	echo "Current contents of your HTML directory: "
	ls -l /var/www/html/class/softdev/$(user)/shakewebpy/
