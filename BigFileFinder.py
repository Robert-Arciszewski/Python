#!/usr/bin/python
import sys
import subprocess
from subprocess import PIPE, run


file_size = input("Podaj minimalny rozmiar pliku [MB]: ")
command = ("find / -xdev -type f -size +" + file_size)

print(subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip())
