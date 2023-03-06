Automation_Script (Duplicate_File_Removal_Automation) :- 
This Script is Divide into 3 modules
1) Assignment13_1.py (main module)
2) MailSender.py
3) Credentials.json

Modules used:-
1) import os module
2) import time
3) import hashlib
4) import schedule
5) import datetime
6) import smtplib
7) from os.path import basename
8) from email.mime.multipart import MIMEMultipart
9) from email.mime.text import MIMEText
10) from email.mime.application import MIMEApplication
11) from email.utils import formatdate

Main Module Contains Functions as:-
1) Path_Checker(directory_path):
	Takes argument as directory path and check whether that path entered is correct or not

2) Count_Files(directory_path):
	Takes argument as directory path and travels in it and counts files only

3) CheckSum(File,blockszie = 1024):
	Takes argument as file at a time and gives checksum of that file to read that file we use blocksize parameter
	and returns CheckSum of file (we use md5 checksum formating)

4)Directory_Content(Source_path):
	Takes argument as directory path and travels using os.walk method and send each file to CheckSum Function to get CheckSum of file

5) File_Creator(file_name):
	This function creates a log file in current directory so we can write in that file

6) Duplicate_Removal(Dict,file):
	This function accept Dictionary containing files and checksum stored in it
	And check if CheckSum of file is equal to another file in Dictionary and then if checkSum are equal we remove it

7) Task_Minute():
	This function actually acts as trigger function which call all above functions at a particular interval of time since we used a schedular

8) main()
	It accept command line arguments from user and 
	Argv[0]:- Application Name 
	Argv[1]:- Directory path
	Argv[2]:- Time interval (in Minutes or Hours)
	Argv[3]:- Receiver_Mail

->Credentials.json file 
Contains Email-ID of Sender
Contains App Password for Sending Mail through script

To Run the Script:-
You to run command as:-
python Assignment13_1.py "Directory_path"      50        Receiver_Mail
	Argv[0]		    Argv[1]	            Argv[2]            Argv[3]

Assignment13_1.py is File Name
Directory_path should be proper absolute path 
50 is time in minute so that this script will run every (50 minutes interval)
You can give dynamic inputs for time and mail 
if you want to change Mail of sender you need edit credentials in json file.
