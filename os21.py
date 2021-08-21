import os

#dirname #filename
#dirname=input("Enter dir full name: ")
#os.system("mkdir {}".format(dirname))

#package install
packagename=input("ENTER PACKAGENAME: ")
os.system("yum install {} -y ".format(packagename))

#date calc 

#history

#

#ls 

#search 

#moving and removing directories

import time

#webserver
webserver=input("Enter which webserver is installed")
if webserver=="httpd":
    os.system("systemctl stop firewalld")
    print("Starting the apache services")
    os.system("systemctl start httpd")
    print("Copy your index.html files in /var/www/html/ folder ")
    time.sleep(2)
    os.system("ifconfig enp0s3")
    print("Enter the local vm ip in webbrowser for checking site")

else:
    os.system("systemctl stop firewalld")
    print("Starting the nginx services")
    os.system("systemctl start nginx")
    print("Copy your index.html files in /usr/bin/share/html/ folder ")
    time.sleep(2)
    os.system("ifconfig enp0s3")
    print("Enter the local vm ip in webbrowser for checking site")


##permanently enable the services
#systemctl enable service name


#mounting directories

#creating new users
#useraddcmd

#setting new users password

##giving different file permissions to a file 

#creating new partitions

##making command aliases
#put the alias cmmnd in /root/.bashrc dir

#creating new partitions and formatting them

#setting up different cronjobs

#setting 
##start or stop services 
#systemctl start {}

