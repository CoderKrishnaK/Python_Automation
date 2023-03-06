
import platform,cpuinfo,psutil,threading,time

def size(byte):
  #this the function to convert bytes into more suitable reading format.

  #Suffixes for the size
  for x in ["B","KB","MB","GB","TB"]:
    if byte<1024:
      return f"{byte:.2f}{x}"
    byte=byte/1024

def Display():
    print("--------------------------------------------------------------")
    
    print("---------- Platform Information ----------")
    Processsor_Details = cpuinfo.get_cpu_info()
    print("System Name : ",platform.system())
    print("System Version: ",platform.release())
    print("--------------------------------------------------------------")
    
    print("---------- Microprocessor Information ----------")
    print("Processsor Name : ",Processsor_Details['brand_raw'])
    print("Processsor details : ",platform.processor())
    print("Processsor Architecture : ",Processsor_Details['arch'])
    print("Processor is : {}bits".format(Processsor_Details['bits']))
    print("Physical core count : ",psutil.cpu_count(logical = False))
    
    print("--------------------------------------------------------------")
    
    print("---------- System Primery and Secondary Storage Device Information ----------")
    mem = psutil.virtual_memory()
    print("Total Usable Ram : ",size(mem.total))

    par = psutil.disk_partitions()
    # getting all of the disk partitions
    for x in par:
        print("Drive: ", x.device)
        print("File system type: ", x.fstype)

        dsk = psutil.disk_usage(x.mountpoint)
        print("Total Harddiskspace : ", size(dsk.total))
    
    print("--------------------------------------------------------------")

def main():
    t1 = threading.Thread(target = Display)
    t1.start()
    t1.join()

if __name__ == "__main__":
    start_time = time.process_time()
    main()
    end_time = time.process_time()
    print("Excecution time time : ",end_time-start_time)
