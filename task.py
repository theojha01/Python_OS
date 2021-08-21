#This is a user friendly software for windows 8 or 8.1
import pyttsx3
import os
import time

pyttsx3.speak(" Hey...Welcome to my software")
x = "Welcome to my software"
y = x.center(80)
print(y)

while True :
  print("\t\t x--------------Menu for Linux command--------------x \n\n")
  print("Press 1 to Install Package \t\t\t\t\t Press 2 to Date")
  print("Press 3 to check list of folder and file \t\t\t Press 4 to Find/Search")
  print("Press 5 to Handling Services \t\t\t\t\t Press 6 to Adding user")
  print("Press 7 to Create Partition \t\t\t\t\t Press 8 to Mount Disk")
  print("Press 9 to setting up different cronjobs \t\t\t Press 10 to Mount Disk")
  print("Press 11 to fstab for mounting \t\t\t\t\t Press 12 To create physical volumes")
  print("Press 13 To create a volume group \t\t\t\t Press 14 to create logical volumes")
  print("Press 0 to Exit")
  
  pyttsx3.speak("How may I assist you")
	print("How may I assist you: ", end='')
	p=input()
  if p=1:
    packagename=input("ENTER PACKAGENAME: ")
    os.system("yum install {} -y ".format(packagename))
    
  elif p=2:
    os.system("date")
  
  elif p=3:
    os.system("ls -l")
    
  elif p=4:
    option=input("how you want to find")
    file=input("Enter Filename")
    os.system("grep {} pattern {}".format(option, file)
