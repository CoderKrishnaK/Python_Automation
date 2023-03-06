# please follow below rules while designing automation script as
"""
    1. Accept input through command line or through file.
    2. Display any message in log file instead of console.
    3. for separate task define separate function.
    4. for robustness handle every expected exception.
    5. perform validations before taking any action.
    6. create user defined modules to store the functionality. 

Design automation script which accept directroy name and mail id from user and create log 
file in that directroy which contains information of running processes as its Name, PID,
Username. after creating log file send that log file to the sepcified mail.

Usage : ProcInfoLog.py Demo Marvellousinfosystem@gmail.com

Demo is name of directory.
marvellousinfosystem@gmail.com
"""

import os 
from sys import *
import psutil
import time
import MailSender as MS

def Path_Checker(Source_path,log_dir = "Marvellous"):
    if not os.path.isabs(Source_path):
        if(os.path.basename(os.getcwd()) == Source_path):
            if not os.path.exits(log_dir):
                try:
                    os.mkdir(log_dir)
                except:
                    pass
            return (os.getcwd())
    if os.path.exists(Source_path) and os.path.isdir(Source_path):
        return (Source_path)
    elif os.path.isfile(Source_path):
        print("Error : the given path is pointing to a File named as {}".format(os.path.basename(Source_path)))
        exit()
    else:
        print("Error : Invalid path\nUse (-h/-H) to get Help or (-u/-U) to know usage")
        exit()

def Process_List():
    #icnt = 0
    list_Of_Process = []
    try:
        for process in psutil.process_iter():
            #icnt+=1 
            Temp = process.as_dict(attrs = ['name','pid','username'])
            list_Of_Process.append(Temp)
   
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
    #print("P ",icnt)
    return list_Of_Process

def LogF_Creater(Path,PList):
    
    seprator = "-"*110
    space = " "*10
    Path = os.path.join(Path,"Marvelluos%s.log"%(time.ctime().replace(" ","_").replace(":","-")))
    str1 = "Following are the Processes Running in the Baground"
    
    fd = open(Path,'w')
    fd.write(seprator+"\n"+space+str1+space+"\n"+seprator+"\n")

    for P in PList:
        Tempstr = str(P)
        fd.write(Tempstr+"\n")
    
    fd.write(seprator)
    fd.close()
    return Path
        

def main():
    if(len(argv) == 2):
        
        if(argv[1] == "-h") or (argv[1] == "-H"):
            print("This Automation Script is Used to send a log file of current running processes to a EmailId")
            exit()
        elif(argv[1] == "-u") or (argv[1] == "-U"):
            print("Usage : python Application_Name Absolute_path_of_Directory Receiver_EmailID")
            exit()
        else:
            print("Error : Invalid Input\nUse (-h/-H) to get Help or (-u/-U) to know usage")
            exit()

    if(len(argv) == 3):
        try:
            path = Path_Checker(argv[1])
            Plist = Process_List()
            path = LogF_Creater(path,Plist)  
            MS.Mail_Sender(path,argv[2])

        except Exception:
            print("Error : Invalid Exception")

    else:
        print("Error : Invalid Number of Arguments\nUse (-h/-H) to get Help or (-u/-U) to know usage")
        exit()

if __name__ == "__main__":
    starttime = time.process_time()
    main()
    endtime = time.process_time()
    print("Execution Time : ",(endtime-starttime))