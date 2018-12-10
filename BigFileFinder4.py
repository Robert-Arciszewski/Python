#!/usr/bin/python
import sys
import subprocess
from subprocess import PIPE, run
file_size = input("Podaj minimalny rozmiar pliku [MB]: ")
max_results = input("Podaj ilość wyników: ")
show_size = (" -exec du -sh {} ';'")
head_result = ("| head -n"+max_results+" ")
sort = ("| sort -rh ")

m = "M"
#command = ("find / -xdev -type f -size +" + file_size + show_size + head_result)


             #find / -xdev -type f -size +100M -exec du -sh {} ';'| head -n20
             #find / -xdev -type f -size +100M -exec du -sh {} ';'| head -n10

            #find / -xdev -type f -size +100M -exec du -sh {} ';'| head -n10


command = ("find / -xdev -type f -size +"+file_size+m+show_size + sort+head_result)

#print (command)
#print ("find / -xdev -type f -size +" + file_size + show_size + head_result)
print(subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip())
