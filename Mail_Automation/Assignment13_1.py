"""
Please Follow Below rules while designing automation as:

  Accept input through command line or through file
  Display any message in LogFile instead of console.
  For robustness handle every expected exception
  Perform Validations before taking actions
  Create user defined Modules to store the functionality

  Design Automation script which performs following task.

  Step 1: Accept Directory name from user and delete all duplicate files from the specified directory by considering the checksum of files
  Step 2: Create one directory named as marvellous and inside that directory create log file which maintains all names of duplicate files which are deleted
  Step 3: Name of that log file should contains the date and time at which that file gets created.
  Step 4: Accept Duration in minutes from user and perform task of duplicate file removal after the specific time interval.
  Step 5: Accept Mail ID from user and send attachment of the log file
  Step 6: Mail should contains statistics about the operation of duplicate file removal

  Mail Body Should contains below things:
    1. Starting time Scanning
    2. Total Number of files Scanned
    3. Total Number of Duplicate files found

  Consider below command line option for the given script
  -DuplicateFileRemoval.py E:\Data\Demo 50 marvellousinfosystem@gmail.com

  1:   DuplicateFileRemoval.py --- Name of python automation script 
  2:   E:\Data\Demo            --- Absolute path of directory which contains duplicate files (argv[1])
  3:   -50                     --- Time interval of script in minutes (argv[2])
  4:   marvellousinfosystem@gmail.com --- Maild ID of receiver  (argv[3])

  Note:-
    For every separate task write separate function.
    Write all user defined functions in one user defined module
    Use proper validation techniques
    Provide help and Usage option for Script
    Create one Readme file which contains description of our script details of command line  options.
"""

from sys import *
import os
import time
import hashlib
import schedule
import datetime
import MailSender as MS

def Count_Files(Source_path):
  iCnt = 0
  for dirName,subdirs,fileList in os.walk(Source_path):
    iCnt += len(fileList)
  return iCnt

def Path_Checker(Source_path):
  iCnt = 0
  if os.path.exists(Source_path):
    if (os.path.isdir(Source_path)): 
      if (os.path.abspath(Source_path)):
        return Source_path
  else:
    print("Error : Invalid Path")
    exit()

def CheckSum(File,blocksize = 1024):
  if os.path.exists(File):
    fd = open(File,"rb")
    hasher = hashlib.md5()
    buf = fd.read(blocksize)

    while len(buf)> 0:
      hasher.update(buf)
      buf = fd.read(blocksize)
    fd.close()

    return hasher.hexdigest()

def Directory_Content(Source_path):
  Arr = {}
  for dirName,subdirs, fileList in os.walk(Source_path):
      for file in fileList:
        temp = CheckSum(os.path.join(dirName,file))
        if not temp in Arr:
          Arr[temp] = [os.path.join(dirName,file)]
        else:
          Arr[temp].append(os.path.join(dirName,file))
  return Arr
  
def File_Creator(file_name):
  path = os.getcwd()
  path = os.path.join(path,str(file_name)+("_%s"%time.ctime()+".txt").replace(" ","_").replace(":","-"))
  fd = open(path,"w")
  fd.close()

  return path

def Duplicate_Removal(Dict,file):
  Count = 0
  fd = open(file,"w")
  separator = "-" * 80
  fd.write("Deleted file History"+"\n")
  iRet = Count_Files(argv[1])
 

  for key in Dict:
    path_list = Dict[key]
    iCnt = 0
    if (len(path_list) >1):
      for path in path_list:
        iCnt = iCnt + 1
        if(iCnt > 1):
          Count = Count + 1
          fd.write(path+"\n")
          os.remove(path)
  fd.write("Total Duplicate Files:-"+str(Count))
  fd.write("\n"+"Total Files in Directory:-"+str(iRet))
  
  fd.close()

def Task_Minute():
  try:
    Arr = {}
    path = Path_Checker(argv[1])
    Arr = Directory_Content(path)
    log_path = File_Creator("Marvellous_log")
    Duplicate_Removal(Arr,log_path)
    
    MS.Mail_Sender(log_path,argv[3])
    
  except  Exception as E:
    print(E)

def main():
  if(len(argv) == 1):
    print("Error : Invalid Number of arguments")
    print("Use -h to get info on application")
    print("Use -u to get usage of application")
    exit()

  if(len(argv) == 2):
    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to Delete Duplicate files from the Directory and write Record of it into log file and send that log file using mail")
        exit()
    elif(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : python Application_Name Directory_Path time(at which minute you want to send) Receiver_mail")
        exit()
  
  if(len(argv) == 4):
    schedule.every(int(argv[2])).minutes.do(Task_Minute)
    while(True):
      schedule.run_pending()
      time.sleep(1)
    
if __name__ == "__main__":
  starttime = time.time()
  main()
  endtime = time.time()
  