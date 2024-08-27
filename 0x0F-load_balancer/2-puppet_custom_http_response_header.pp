#!/usr/bin/env bash
#cofiguration with puppet

exec { "http header":
	command => 'sudo apt-get update -y;
	sudo apt-get install nginx -y;
	sed -i "/server_name/ _/a add_header X-served-By $HOSTNAME;" /etc/nginx/sites-available/default
	sudo service nginx restart',
	provider => shell,

