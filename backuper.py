import shutil
import os
import datetime

date = datetime.datetime.now()
date_short = date.strftime("%d%m%y")

source_path = input("Wprowadź ścieżkę do źródła np.: /home/user/Pulpit\n")
destination_path = input("Wprowadź ścieżkę przeznaczenia np.: /media/disk/\n")
destination_filename = "backup"+date_short

dest = destination_path + destination_filename

check_file = os.path.isfile(source_path)
check_dir = os.path.isdir(source_path)

if check_file == True:
    print("Został wskazany plik a powinien być wskazany katalog.")
    exit(0)
elif check_dir == True:

    if os.path.exists(dest):
        for i in range(check_dir):
            print("Katalog o tej nazwie już istnieje.")
            destination_filename = "backup"+date_short+"_"+str(i)
            dest = destination_path + destination_filename
            if os.path.exists(dest):
                print("Ten plik już istnieje tutaj: "+dest)
            else:
                shutil.copytree(source_path, dest)
            print("Kopiowanie rozpoczęte...")
            print("Kopiowanie zakończone. \n Plik backupu jest tutaj: "+dest)

    else:
        print("Kopiowanie rozpoczęte...")
        shutil.copytree(source_path,dest)
        print("Kopiowanie zakończone. \n Plik backupu jest tutaj: "+dest)
else:
    print("Nie został wskazany plik ani katalog")
    exit(0)