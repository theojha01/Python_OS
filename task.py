import pyttsx3
import os
import time
import getpass

#pyttsx3.speak(" Hey...Welcome to my software")
os.system("espeak-ng Hey...Welcome to my software")
x = "Welcome to my software"
y = x.center(80)
print(y)

while True :
  os.system("clear")
  print("\t\t x--------------Menu for Linux command--------------x \n\n")
  print("Press 1 to Install Package \t\t\t\t\t Press 2 to Date")
  print("Press 3 to check list of folder and file \t\t\t Press 4 to Find/Search")
  print("Press 5 to Handling Services \t\t\t\t\t Press 6 to Adding user")
  print("Press 7 to Create Partition \t\t\t\t\t Press 8 To create a webserver")
  print("Press 9 to setting up different cronjobs \t\t\t Press 10 to Mount Disk")
  print("Press 11 to fstab for mounting \t\t\t\t\t Press 12 To create physical volumes")
  print("Press 13 To create a volume group \t\t\t\t Press 14 to check logical volumes")
  print("Press 0 to Exit")
  
  #pyttsx3.speak("How may I assist you")
  os.system("espeak-ng 'How may I assist you'")
  #print("How may I assist you: ", end='')
  p=int(input("HOW MAY I ASSIST YOU "))
  if p==1:
    packagename=input("ENTER PACKAGENAME: ")
    os.system("yum install {} -y ".format(packagename))
    os.system("espeak-ng 'packages installed'")
    time.sleep(2)
    
  elif p==2:
    os.system("espeak-ng 'Date is'")
    os.system("date")
    time.sleep(2)
  
  elif p==3:
    os.system("espeak-ng 'Current Directory list is'")
    os.system("ls -l")
    
  elif p==4:
    option=input("how you want to find")
    file=input("Enter Filename")
    os.system("grep {} {}".format(option, file))
  
  elif p==5:
    service=input("Enter Service Name")
    os.system("systemctl start {}".format(service))
    os.system("espeak-ng 'service is started'")
    time.sleep(2)

  elif p==6:
    name=input("Enter new user name: ")
    passwd = getpass.getpass(prompt="Enter password: ")
    os.system("sudo useradd {}".format(name))
    os.system("sudo passwd {}".format(name))
    time.sleep(2)
  
  elif p==7:
    disk=input("enter your disk name")
    os.system("sudo fdisk /dev/{}".format(disk))
    
  elif p==8:
    webserver=input("Enter which webserver is installed")
    if webserver=="httpd":
        os.system("systemctl stop firewalld")
        print("Starting the apache services")
        os.system("systemctl start httpd")
        print("Copy your index.html files in /var/www/html/ folder ")
        time.sleep(2)
        os.system("ifconfig enp0s3")
        print("Enter the local vm ip in webbrowser for checking site")
        os.system("espeak-ng 'Enter the local vm ip in webbrowser for checking site'")
    else:
        os.system("systemctl stop firewalld")
        print("Starting the nginx services")
        os.system("systemctl start nginx")
        print("Copy your index.html files in /usr/bin/share/html/ folder ")
        time.sleep(2)
        os.system("ifconfig enp0s3")
        print("Enter the local vm ip in webbrowser for checking site")
        os.system("espeak-ng 'Enter the local vm ip in webbrowser for checking site'")
	      
  elif p==9:
    os.system("crontab –e")

  elif p==10:
    initdisk=input("Enter the destination where to mount")
    finaldisk=input("Enter the disk path")
    os.system("mount -t ntfs {}  {}".format(initdisk, finaldisk))
	      
  elif p==11:
    os.system("vim /etc/fstab")
	      
  elif p==12:
    initdisk=input("Enter the destination where to mount")
    finaldisk=input("Enter the disk path")
    os.system("pvcreate {}  {}".format(initdisk, finaldisk))
	      
  elif p==13:
    grname=input("Enter your group name")
    initdisk=input("Enter the destination where to mount")
    finaldisk=input("Enter the disk path")
    os.system("vgcreate {}  {} {}".format(grname,initdisk, finaldisk))
	      
  elif p==14:
    os.system("lvdisplay")
  elif p==0:
    break
