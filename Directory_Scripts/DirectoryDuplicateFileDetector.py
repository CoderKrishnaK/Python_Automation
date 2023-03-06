from sys import *
import os
import hashlib

def hashfile(path, blocksize = 1024):
  fd = open(path,'rb')
  hasher = hashlib.md5()
  buf = fd.read(blocksize)

  while len(buf) > 0:
    hasher.update(buf)
    buf = fd.read(blocksize)
  
  fd.close()
  return hasher.hexdigest()

def FindDuplicate(path):
  flag = os.path.isabs(path)
  if flag == False:
    path = os.path.abspath(path)

  exists = os.path.isdir(path)
  
  dups = {}
  if exists:
    for dirName, subdirs, fileList in os.walk(path):
      for filen in fileList:
        path = os.path.join(dirName, filen)
        file_hash = hashfile(path)
        if file_hash in dups:
          dups[file_hash].append(path)
        else:
          dups[file_hash] = [path]
    
    return dups
  else:
    print("Invalid path")

def PrintDuplicate(dict1):
  results = list(filter(lambda x: len(x)>1, dict1.values()))
  
  if len(results) > 0:
    print("Duplicates Found:")
    print("The following files are identical.")

    iCnt = 0
    for result in results:
      for subresult in result:
        iCnt += 1
        if iCnt>= 2:
          print("\t\t%s"%subresult)
  else:
      print("No duplicates files found")

def main():
  print("-------------- Marvellous Infosystem ------------------")
  print("Application Name: "+argv[0])
  if (len(argv)!= 2):
    print("Error : Invalid Number of Arguments")
    exit()
  
  if (argv[1] == "-h") or (argv[1] == "-H"):
    print("This Scripts is used to traverse specific directory and display sizes of files")

  if (argv[1] == "-u") or (argv[1] == "-U"):
    print("Usage : ApplicationName Absolutepath_of_Directory")
    exit()
  
  try:
    arr = {}
    arr = FindDuplicate(argv[1])
    PrintDuplicate(arr)
  except ValueError:
    print("Error : Invalid Datatype of Input")

if __name__ == "__main__":
  main()