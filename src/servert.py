from colorama import Fore
import time
starttime = int(time.time())

def log(message,error=False,detailedtime=True):
    #bellow you will find a very advanced print() function
    if detailedtime==True:
      l=time.struct_time(time.localtime(int(time.time())))
      timee=Fore.YELLOW+f"[{l.tm_year}-{l.tm_mon}-{l.tm_mday} {l.tm_hour}:{l.tm_min}:{l.tm_sec}]"+Fore.WHITE
    else:
      l=time.struct_time(time.localtime(int(time.time())))
      timee=Fore.YELLOW+f"[{l.tm_hour}:{l.tm_min}:{l.tm_sec}]"+Fore.WHITE
    if error==False:
      print(timee+" "+str(message)+Fore.WHITE)
    else:
      print(timee+" "+Fore.RED+str(message)+Fore.WHITE)
    return 'lmao imagine lmao lmao lmao lmao lmao lmao lmao lmao'
