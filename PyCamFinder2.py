#!/usr/bin/python3
import sys
from json import loads
import requests
from requests.auth import HTTPDigestAuth
from requests.auth import HTTPBasicAuth
import subprocess
from subprocess import PIPE, run
import pings
import socket
import os
from datetime import datetime
from contextlib import suppress
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import hashlib
from pprint import pprint
import re

def main():
    print ("\n\n")
    print("_______________ PyCamScanner v1.0.20181210 _______________")
    #print(str("____________________ ")+str(datetime.now().strftime('%m-%d-%y'))+" _______________")
    menu()


def menu():
    choice = input("""
                    1: Dahua 
                    2: Uniview
                    3: Hikvision

                    0: Wyjście

                    Wybieram: """)

    if choice == '1':
        print("___________________________________________________________")
        print("\n Menu ->  Dahua")
        choice = input("""
                    0: Kompletny raport - podgląd
                    1: Kompletny raport - zapis do pliku
                    2: Chmura
                    3: Adresy IP
                    4: Kodowanie H.264/H.265
                    5: Ustawione godziny
                    6: Wersja oprogramowania
                    7: Nazwy kanałów
                    8: Typ urządzenia

                    9: Powrót do menu
                    0: Wyjście

                    Wybieram: """)
        if choice == '0':
            dahua_new()
        if choice == '1':
            dahua_new_files()
        elif choice == '2':
            dahua_nvr_new_cloud()
        elif choice == '3':
            dahua_nvr_new_ip()
        elif choice == '4':
            dahua_nvr_new_encode()
        elif choice == '5':
            dahua_nvr_new_time()
        elif choice == '6':
            dahua_nvr_new_software()
        elif choice == '7':
            dahua_nvr_new_channelname()
        elif choice == '8':
            dahua_nvr_new_devicetype()
        elif choice == '9':
            menu()
        elif choice == '0':
            sys.exit()
        else:
            print("Podana została nieobsługiwana wartość")
            menu()


    if choice == '2':

        print("___________________________________________________________")

        print("\n Menu ->  Uniview")

        choice = input("""
                    0: Kompletny raport - podgląd
                    1: Kompletny raport - file
                    2: Ustawienie chmury v1
                    3: Ustawienie chmury v2
    
                    9: Powrót do menu
                    0: Wyjście
    
                    Wybieram: """)

        if choice == '0':
            uniview_new()
        if choice == '1':
            set_unv_cloud()
        elif choice == '2':
            set_unv_cloud()
        elif choice == '3':
            set_unv_cloud2()
        elif choice == '9':
            menu()
        elif choice == '0':
            sys.exit()
        else:
            print("Podana została nieobsługiwana wartość")
            menu()

        #save_to_file()
    elif choice == '3':
        set_unv_cloud()
    elif choice == '4':
        menu()
    elif choice == '5':
        menu()
    elif choice == '6':
        menu()
    elif choice == '6':
        menu()
    elif choice == '7':
        menu()
    elif choice == '8':
        menu()
    elif choice == '9':
        menu()
    elif choice == '0':
        sys.exit()
    else:
        print("Podana została nieobsługiwana wartość")
        menu()

def dahua_new():
    while True:
        try:
            a = int(input("Podsieć: 192.168."))
            x = int(input("Zakres hostów od: 192.168." + str(a) + "."))
            y = int(input("Zakres hostów do: 192.168." + str(a) + ".")) + 1
        except ValueError:
            print('Wprowadzona została niepoprawna wartość.')
            continue
        login_text = ("Podaj login: ")
        passw_text = ("Podaj hasło: ")
        login = input(login_text)
        passw = input(passw_text)
        http = "http://"
        ip_uniview = "192.168." + str(a) + "."
        uniview_url = "/cgi-bin/magicBox.cgi?action=getSystemInfo"
        cloud_rest = "/cgi-bin/configManager.cgi?action=getConfig&name=T2UServer"
        confignetwork_rest = "/cgi-bin/configManager.cgi?action=getConfig&name=Network"
        configencode_rest = "/cgi-bin/configManager.cgi?action=getConfig&name=Encode"
        currenttime_rest = "/cgi-bin/global.cgi?action=getCurrentTime"
        softwareversion_rest = "/cgi-bin/magicBox.cgi?action=getSoftwareVersion"
        channeltitle_rest = "/cgi-bin/configManager.cgi?action=getConfig&name=ChannelTitle"
        devicetype_rest = "/cgi-bin/magicBox.cgi?action=getDeviceType"
        p = pings.Ping()
        for i in range(x, y):
            ip_rest = str(i)
            ping_ip = str(ip_uniview + ip_rest)
            response = p.ping(ping_ip)
            httpdigest = ',auth=HTTPDigestAuth('+login+','+passw+')'
            httpauth = ',auth=('+login+','+passw+')'
            print(ping_ip)
            if (response.is_reached()):
                systeminfo = requests.get(http + ip_uniview + str(ip_rest) + uniview_url, auth=HTTPDigestAuth(login, passw), verify=False)
                cloud = requests.get(http + ip_uniview + str(ip_rest) + cloud_rest, auth=HTTPDigestAuth(login, passw), verify=False)
                confignetwork = requests.get(http + ip_uniview + str(ip_rest) + confignetwork_rest, auth=HTTPDigestAuth(login, passw), verify=False)
                configencode = requests.get(http + ip_uniview + str(ip_rest) + configencode_rest, auth=HTTPDigestAuth(login, passw))
                currenttime = requests.get(http + ip_uniview + str(ip_rest) + currenttime_rest,auth=HTTPDigestAuth(login, passw))
                softwareversion = requests.get(http + ip_uniview + str(ip_rest) +softwareversion_rest,auth=HTTPDigestAuth(login, passw))
                channeltitle = requests.get(http + ip_uniview + str(ip_rest) + channeltitle_rest,auth=HTTPDigestAuth(login, passw))
                devicetype = requests.get(http + ip_uniview + str(ip_rest) + devicetype_rest,auth=HTTPDigestAuth(login, passw))
                if systeminfo.status_code == 401:
                    systeminfo = requests.get(http + ip_uniview + str(ip_rest) + uniview_url,auth=(login, passw), verify=False)
                    cloud = requests.get(http + ip_uniview + str(ip_rest) + cloud_rest, auth=(login, passw), verify=False)
                    confignetwork = requests.get(http + ip_uniview + str(ip_rest) + confignetwork_rest, auth=(login, passw), verify=False)
                    configencode = requests.get(http + ip_uniview + str(ip_rest) + configencode_rest, auth=(login, passw))
                    currenttime = requests.get(http + ip_uniview + str(ip_rest) + currenttime_rest,auth=(login, passw))
                    softwareversion = requests.get(http + ip_uniview + str(ip_rest) +softwareversion_rest,auth=(login, passw))
                    channeltitle = requests.get(http + ip_uniview + str(ip_rest) + channeltitle_rest,auth=(login, passw))
                    devicetype = requests.get(http + ip_uniview + str(ip_rest) + devicetype_rest,auth=(login, passw))
                else:
                    print("Nie mogę się zalogować do urządzenia")
                print("Informacje dla: "+ ping_ip +"\n")
                print("Informacje systemowe: \n"+ systeminfo.text)
                print("Model urządzenia: \n"+ devicetype.text)
                print("Czas: \n" + currenttime.text)
                print("Wersja oprogramowania: \n" + softwareversion.text)
                print("Chmura: \n"+ cloud.text)
                print("Konfiguracja sieci: \n" + confignetwork.text)
                print("Kodowanie: \n" + configencode.text)
                print("Kanały: \n" + channeltitle.text)
                print(devicetype.url)
                print(devicetype.status_code)
            else:
                print("OFFLINE\n")

        break


def dahua_new_files():
    while True:
        try:
            a = int(input("Podsieć: 192.168."))
            x = int(input("Zakres hostów od: 192.168." + str(a) + "."))
            y = int(input("Zakres hostów do: 192.168." + str(a) + ".")) + 1
        except ValueError:
            print('Wprowadzona została niepoprawna wartość.')
            continue
        login_text = ("Podaj login: ")
        passw_text = ("Podaj hasło: ")
        login = input(login_text)
        passw = input(passw_text)
        #alt_login = "admin"
        #alt_passwd = "admin123"
        http = "http://"
        ip_uniview = "192.168." + str(a) + "."
        uniview_url = "/cgi-bin/magicBox.cgi?action=getSystemInfo"
        cloud_rest = "/cgi-bin/configManager.cgi?action=getConfig&name=T2UServer"
        confignetwork_rest = "/cgi-bin/configManager.cgi?action=getConfig&name=Network"
        configencode_rest = "/cgi-bin/configManager.cgi?action=getConfig&name=Encode"
        currenttime_rest = "/cgi-bin/global.cgi?action=getCurrentTime"
        softwareversion_rest = "/cgi-bin/magicBox.cgi?action=getSoftwareVersion"
        channeltitle_rest = "/cgi-bin/configManager.cgi?action=getConfig&name=ChannelTitle"
        devicetype_rest = "/cgi-bin/magicBox.cgi?action=getDeviceType"
        p = pings.Ping()
        for i in range(x, y):
            ip_rest = str(i)
            ping_ip = str(ip_uniview + ip_rest)
            response = p.ping(ping_ip)
            print(ping_ip)
            #response = p.ping("192.168.135.50"))
            #print (response)
            if (response.is_reached()): #jeśli połączenie nawiązane
                systeminfo = requests.get(http + ip_uniview + str(ip_rest) + uniview_url, auth=HTTPDigestAuth(login, passw))
                cloud = requests.get(http + ip_uniview + str(ip_rest) + cloud_rest, auth=HTTPDigestAuth(login, passw))
                confignetwork = requests.get(http + ip_uniview + str(ip_rest) + confignetwork_rest, auth=HTTPDigestAuth(login, passw))
                configencode = requests.get(http + ip_uniview + str(ip_rest) + configencode_rest, auth=HTTPDigestAuth(login, passw))
                currenttime = requests.get(http + ip_uniview + str(ip_rest) + currenttime_rest,auth=HTTPDigestAuth(login, passw))
                softwareversion = requests.get(http + ip_uniview + str(ip_rest) + softwareversion_rest,auth=HTTPDigestAuth(login, passw))
                channeltitle = requests.get(http + ip_uniview + str(ip_rest) + channeltitle_rest,auth=HTTPDigestAuth(login, passw))
                devicetype = requests.get(http + ip_uniview + str(ip_rest) + devicetype_rest,auth=HTTPDigestAuth(login, passw))
                if systeminfo.status_code == 200: #jeśli mamy połączenie do rejestratora
                    #print (systeminfo.headers)
                    #print (systeminfo.cookies)
                    #print(systeminfo.elapsed)
                    #print(systeminfo.encoding)
                    #print(systeminfo.history)
                    print(systeminfo.content)
                    print(systeminfo.apparent_encoding)
                    print(systeminfo.links)
                    print(systeminfo.iter_content(1,True))
                    print(systeminfo.__attrs__)
                    print(systeminfo.reason)
                    print(systeminfo.raw)
                    print(systeminfo.links)
                    print(systeminfo.apparent_encoding)
                    filepath = "Raport/NVR_" + ping_ip + ".txt"
                    os.makedirs(os.path.dirname(filepath), exist_ok=True)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        print("Rejestrator: " + ping_ip + "\n", file=f)
                        print("Data wygenerowania raportu: "+ datetime.today().strftime("%Y-%m-%d %H:%M:%S"), file=f)
                        print('Linki: \n' + str(systeminfo.url) + '\n' + str(cloud.url) + '\n' + str(confignetwork.url) + '\n' + str(configencode.url) + '\n' + str(currenttime.url) + '\n' + str(softwareversion.url) + '\n' + str(channeltitle.url) + '\n' + str(devicetype.url) + '\n', file=f)
                        print("Informacje systemowe: \n" + systeminfo.text, file=f)
                        print("Model urządzenia: \n" + devicetype.text, file=f)
                        print("Czas: \n" + currenttime.text, file=f)
                        print("Wersja oprogramowania: \n" + softwareversion.text, file=f)
                        print("Chmura: \n" + cloud.text, file=f)
                        print("Konfiguracja sieci: \n" + confignetwork.text, file=f)
                        print("Kodowanie: \n" + configencode.text, file=f)
                        print("Kanały: \n" + channeltitle.text, file=f)
                        print("Dane rejestratora zapisane")
                        #print(confignetwork.url)_
                        #print(confignetwork.status_code)
                elif systeminfo.status_code == 401: #jeśli nie połączymy się do rejestratora, próbujemy do IPC z auth=login,passw
                    systeminfo = requests.get(http + ip_uniview + str(ip_rest) + uniview_url,auth=(login, passw))
                    cloud = requests.get(http + ip_uniview + str(ip_rest) + cloud_rest,auth=(login, passw))
                    confignetwork = requests.get(http + ip_uniview + str(ip_rest) + confignetwork_rest,auth=(login, passw))
                    configencode = requests.get(http + ip_uniview + str(ip_rest) + configencode_rest,auth=(login, passw))
                    currenttime = requests.get(http + ip_uniview + str(ip_rest) + currenttime_rest,auth=(login, passw))
                    softwareversion = requests.get(http + ip_uniview + str(ip_rest) + softwareversion_rest,auth=(login, passw))
                    channeltitle = requests.get(http + ip_uniview + str(ip_rest) + channeltitle_rest,auth=(login, passw))
                    devicetype = requests.get(http + ip_uniview + str(ip_rest) + devicetype_rest,auth=(login, passw))
                    if systeminfo.status_code == 200: #jeśli połączymy się do IPC
                        filepath = "Raport/IPC_" + ping_ip + ".txt"
                        os.makedirs(os.path.dirname(filepath), exist_ok=True)
                        with open(filepath, 'w', encoding='utf-8') as f:
                            print("Kamera: " + ping_ip + "\n", file=f)
                            print("Data wygenerowania raportu: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"),file=f)
                            print('Linki: \n' + str(systeminfo.url) + '\n' + str(cloud.url) + '\n' + str(confignetwork.url) + '\n' + str(configencode.url) + '\n' + str(currenttime.url) + '\n' + str(softwareversion.url) + '\n' + str(channeltitle.url) + '\n' + str(devicetype.url) + '\n', file=f)
                            print("Informacje systemowe: \n" + systeminfo.text, file=f)
                            print("Model urządzenia: \n" + devicetype.text, file=f)
                            print("Czas: \n" + currenttime.text, file=f)
                            print("Wersja oprogramowania: \n" + softwareversion.text, file=f)
                            print("Chmura: \n" + cloud.text, file=f)
                            print("Konfiguracja sieci: \n" + confignetwork.text, file=f)
                            print("Kodowanie: \n" + configencode.text, file=f)
                            print("Kanały: \n" + channeltitle.text, file=f)
                            print("Dane kamery zapisane")
                    elif systeminfo.status_code == 401: #jeśli nie połączymy się do urzadzenia
                        filepathauth = "Raport/BLOKADA_" + ping_ip + ".txt"
                        os.makedirs(os.path.dirname(filepathauth), exist_ok=True)
                        with open(filepathauth, 'w', encoding='utf-8') as l:
                            print("Zły login '"+login+"' lub hasło '" +passw+"' lub urządzenie zablokowane.", file=l)
                            print("Zły login lub hasło lub urządzenie zablokowane")
                    else:
                        #filepathproblem = "Raport/NIEZNANY_" + ping_ip + ".txt"
                        #os.makedirs(os.path.dirname(filepathproblem), exist_ok=True)
                        #with open(filepathproblem, 'w', encoding='utf-8') as p:
                        #print("Nieznany problem.", file=p)
                        print("Nieznany problem")
                        print(systeminfo.url)
                        #print(systeminfo.status_code)


            else:
                filepathoffline = "Raport/OFFLINE_"+ping_ip+".txt"
                os.makedirs(os.path.dirname(filepathoffline), exist_ok=True)
                with open(filepathoffline, 'w', encoding='utf-8') as o:
                    print("OFFLINE\n", file=o)
                    print("OFFLINE")
        break


def dahua_nvr_new_cloud():
    while True:
        try:
            a = int(input("Podsieć: 192.168."))
            x = int(input("Zakres hostów od: 192.168." + str(a) + "."))
            y = int(input("Zakres hostów do: 192.168." + str(a) + ".")) + 1
        except ValueError:
            print('Wprowadzona została niepoprawna wartość.')
            continue
        login_text = ("Podaj login: ")
        passw_text = ("Podaj hasło: ")
        login = input(login_text)
        passw = input(passw_text)
        http = "http://"
        ip_uniview = "192.168." + str(a) + "."
        cloud_rest = "/cgi-bin/configManager.cgi?action=getConfig&name=T2UServer"
        p = pings.Ping()
        for i in range(x, y):
            ip_rest = str(i)
            ping_ip = str(ip_uniview + ip_rest)
            response = p.ping(ping_ip)
            print("\n"+ping_ip+"\n")
            if (response.is_reached()):
                cloud = requests.get(http + ip_uniview + str(ip_rest) + cloud_rest, auth=HTTPDigestAuth(login, passw))
                if cloud.text != "":
                    print(cloud.text+"\n")
                    #print(cloud.json())
                    #print(cloud.headers)
                else:
                    #ipc
                    cloud = requests.get(http + ip_uniview + str(ip_rest) + cloud_rest, auth=(login, passw))
                    print(cloud.text+"\n")
            else:
                print("OFFLINE\n\n")

        break


def dahua_nvr_new_ip():
    while True:
        try:
            a = int(input("Podsieć: 192.168."))
            x = int(input("Zakres hostów od: 192.168." + str(a) + "."))
            y = int(input("Zakres hostów do: 192.168." + str(a) + ".")) + 1
        except ValueError:
            print('Wprowadzona została niepoprawna wartość.')
            continue
        login_text = ("Podaj login: ")
        passw_text = ("Podaj hasło: ")
        login = input(login_text)
        passw = input(passw_text)
        http = "http://"
        ip_uniview = "192.168." + str(a) + "."
        confignetwork_rest = "/cgi-bin/configManager.cgi?action=getConfig&name=Network"
        p = pings.Ping()
        for i in range(x, y):
            ip_rest = str(i)
            ping_ip = str(ip_uniview + ip_rest)
            response = p.ping(ping_ip)
            print(ping_ip)
            if (response.is_reached()):
                confignetwork = requests.get(http + ip_uniview + str(ip_rest) + confignetwork_rest, auth=HTTPDigestAuth(login, passw))
                if confignetwork.text != "":
                    print(confignetwork.text)
                else:
                    confignetwork = requests.get(http + ip_uniview + str(ip_rest) + confignetwork_rest, auth=(login, passw))
                    print(confignetwork.text)
            else:
                print("OFFLINE\n")
        break


def dahua_nvr_new_encode():
    while True:
        try:
            a = int(input("Podsieć: 192.168."))
            x = int(input("Zakres hostów od: 192.168." + str(a) + "."))
            y = int(input("Zakres hostów do: 192.168." + str(a) + ".")) + 1
        except ValueError:
            print('Wprowadzona została niepoprawna wartość.')
            continue
        login_text = ("Podaj login: ")
        passw_text = ("Podaj hasło: ")
        login = input(login_text)
        passw = input(passw_text)
        http = "http://"
        ip_uniview = "192.168." + str(a) + "."
        configencode_rest = "/cgi-bin/configManager.cgi?action=getConfig&name=Encode"
        p = pings.Ping()
        for i in range(x, y):
            ip_rest = str(i)
            ping_ip = str(ip_uniview + ip_rest)
            response = p.ping(ping_ip)
            print(ping_ip)
            if (response.is_reached()):
                configencode = requests.get(http + ip_uniview + str(ip_rest) + configencode_rest,auth=HTTPDigestAuth(login, passw))
                if configencode.text != "":
                    print(configencode.text)
                else:
                    configencode = requests.get(http + ip_uniview + str(ip_rest) + configencode_rest, auth=(login, passw))
                    print(configencode.text)
                    #print(configencode.status_code)
                    if (configencode.status_code == 401):
                        print("Zły login lub hasło lub konto zablokowane. "+ str(configencode.status_code))
                    else:
                        print(configencode.text)
                        #print(configencode.status_code)
            else:
                print("OFFLINE\n")
        break



def dahua_nvr_new_time():
    while True:
        try:
            a = int(input("Podsieć: 192.168."))
            x = int(input("Zakres hostów od: 192.168." + str(a) + "."))
            y = int(input("Zakres hostów do: 192.168." + str(a) + ".")) + 1
        except ValueError:
            print('Wprowadzona została niepoprawna wartość.')
            continue
        login_text = ("Podaj login: ")
        passw_text = ("Podaj hasło: ")
        login = input(login_text)
        passw = input(passw_text)
        http = "http://"
        ip_uniview = "192.168." + str(a) + "."
        currenttime_rest = "/cgi-bin/global.cgi?action=getCurrentTime"
        p = pings.Ping()
        for i in range(x, y):
            ip_rest = str(i)
            ping_ip = str(ip_uniview + ip_rest)
            response = p.ping(ping_ip)
            print(ping_ip)
            if (response.is_reached()):
                currenttime = requests.get(http + ip_uniview + str(ip_rest) + currenttime_rest,auth=HTTPDigestAuth(login, passw))
                if currenttime.text != "":
                    print(currenttime.text)
                else:
                    currenttime = requests.get(http + ip_uniview + str(ip_rest) + currenttime_rest, auth=(login, passw))
                    #print(currenttime.text)
                    #print(currenttime.status_code)
                    if (currenttime.status_code == 401):
                        print("Zły login lub hasło lub konto zablokowane. "+ str(currenttime.status_code))
                    else:
                        print(currenttime.text)
                        #print(currenttime.status_code)
            else:
                print("OFFLINE\n")
        break



def dahua_nvr_new_software():
    while True:
        try:
            a = int(input("Podsieć: 192.168."))
            x = int(input("Zakres hostów od: 192.168." + str(a) + "."))
            y = int(input("Zakres hostów do: 192.168." + str(a) + ".")) + 1
        except ValueError:
            print('Wprowadzona została niepoprawna wartość.')
            continue
        login_text = ("Podaj login: ")
        passw_text = ("Podaj hasło: ")
        login = input(login_text)
        passw = input(passw_text)
        http = "http://"
        ip_uniview = "192.168." + str(a) + "."
        login_text = ("Podaj login: ")
        passw_text = ("Podaj hasło: ")
        login = input(login_text)
        passw = input(passw_text)
        http = "http://"
        ip_uniview = "192.168." + a + "."
        softwareversion_rest = "/cgi-bin/magicBox.cgi?action=getSoftwareVersion"
        p = pings.Ping()
        for i in range(x, y):
            ip_rest = str(i)
            ping_ip = str(ip_uniview + ip_rest)
            response = p.ping(ping_ip)
            print(ping_ip)
            if (response.is_reached()):
                softwareversion = requests.get(http + ip_uniview + str(ip_rest) + softwareversion_rest,auth=HTTPDigestAuth(login, passw))
                if softwareversion.text != "":
                    print(softwareversion.text)
                else:
                    softwareversion = requests.get(http + ip_uniview + str(ip_rest) + softwareversion_rest, auth=(login, passw))
                    #print(softwareversion.text)
                    #print(softwareversion.status_code)
                    if (softwareversion.status_code == 401):
                        print("Zły login lub hasło lub konto zablokowane. "+ str(softwareversion.status_code))
                    else:
                        print(softwareversion.text)
                        #print(softwareversion.status_code)
            else:
                print("OFFLINE\n")
        break


def dahua_nvr_new_channelname():
    while True:
        try:
            a = int(input("Podsieć: 192.168."))
            x = int(input("Zakres hostów od: 192.168." + str(a) + "."))
            y = int(input("Zakres hostów do: 192.168." + str(a) + ".")) + 1
        except ValueError:
            print('Wprowadzona została niepoprawna wartość.')
            continue
        login_text = ("Podaj login: ")
        passw_text = ("Podaj hasło: ")
        login = input(login_text)
        passw = input(passw_text)
        http = "http://"
        ip_uniview = "192.168." + str(a) + "."
        channeltitle_rest = "/cgi-bin/configManager.cgi?action=getConfig&name=ChannelTitle"
        p = pings.Ping()
        for i in range(x, y):
            ip_rest = str(i)
            ping_ip = str(ip_uniview + ip_rest)
            response = p.ping(ping_ip)
            print(ping_ip)
            if (response.is_reached()):
                channeltitle = requests.get(http + ip_uniview + str(ip_rest) + channeltitle_rest, auth=HTTPDigestAuth(login, passw), verify=False, timeout=10)
                if channeltitle.text != "":
                    print(channeltitle.text)
                else:
                    channeltitle = requests.get(http + ip_uniview + str(ip_rest) + channeltitle_rest, auth=(login, passw))
                    print(channeltitle.text)
            else:
                print("OFFLINE\n")
        break


def dahua_nvr_new_devicetype():
    while True:
        try:
            a = int(input("Podsieć: 192.168."))
            x = int(input("Zakres hostów od: 192.168." + str(a) + "."))
            y = int(input("Zakres hostów do: 192.168." + str(a) + ".")) + 1
        except ValueError:
            print('Wprowadzona została niepoprawna wartość.')
            continue
        login_text = ("Podaj login: ")
        passw_text = ("Podaj hasło: ")
        login = input(login_text)
        passw = input(passw_text)
        http = "http://"
        ip_uniview = "192.168." + str(a) + "."
        devicetype_rest = "/cgi-bin/magicBox.cgi?action=getDeviceType"
        p = pings.Ping()
        for i in range(x, y):
            ip_rest = str(i)
            ping_ip = str(ip_uniview + ip_rest)
            response = p.ping(ping_ip)
            print(ping_ip)
            if (response.is_reached()):
                channeltitle = requests.get(http + ip_uniview + str(ip_rest) + devicetype_rest, auth=HTTPDigestAuth(login, passw), verify=False, timeout=10)
                if channeltitle.text != "":
                    print(channeltitle.text)
                else:
                    channeltitle = requests.get(http + ip_uniview + str(ip_rest) + devicetype_rest, auth=(login, passw))
                    print(channeltitle.text)
            else:
                print("OFFLINE\n")
        break


def bs_unv_parse():
    curlparse = "curl 'http://192.168.134.80/cgi-bin/main-cgi' --data 'lLan=1&szUserName=admin&szUserLoginCert=0192023a7bbd73250516f069df18b500'"



def set_unv_cloud():
    while True:
        try:
            a = int(input("Podsieć: 192.168."))
            x = int(input("Zakres hostów od: 192.168." + str(a) + "."))
            y = int(input("Zakres hostów do: 192.168." + str(a) + ".")) + 1
        except ValueError:
            print('Wprowadzona została niepoprawna wartość.')
            continue
        login_text = ("Podaj login: ")
        passw_text = ("Podaj hasło: ")
        login = input(login_text)
        passw = input(passw_text)
        http = "http://"
        ip_uniview = "192.168." + str(a) + "."
        static = "/LAPI/V1.0/"
        static2 = "/cgi-bin/main-cgi/"
        cloud_nvr_unv = "Network/Cloud"
        p = pings.Ping()
        for i in range(x, y):
            ip_rest = str(i)
            ping_ip = str(ip_uniview + ip_rest)
            response = p.ping(ping_ip)
            print(ping_ip)
            #response = p.ping("192.168.135.50"))
            #print (response)
            if (response.is_reached()):
                cloud_nvr_unv_x = requests.get(http + ip_uniview + str(ip_rest) + str(static) + cloud_nvr_unv, auth=HTTPDigestAuth(login, passw))
                cloud_nvr_unv_y = requests.get(http + ip_uniview + str(ip_rest) + str(static2), auth=(login, passw))
                payload = {
                    'lLan=10&szUserName=': 'admin',
                    '&szUserPasswd=': '0192023a7bbd73250516f069df18b500'
                }

                payload2 = {"lLan=10&szUserName=": "admin", "&szUserPasswd=":"admin123"}
                data2 = {"Enabled": 1,
                    "Domain": "bcs.pl",
                    "DeviceName": "UNIVIEW"}
                data = {"bIsEnable": 1,
                         "szDdnsDomain": "bcs.pl"
                }
                data3 = {"cmd":149,"bIsEnable":0,"u8DdnsType":"0","szDdnsDomain":"p2pdevice.bcscctv.pl","szDeviceName":"","szDdnsUserName":"","szDdnsPassword":"","szUserName":"admin","u32UserLoginHandle":-1}
                payloadxxx = {'lLan=1&szUserName=':'admin','&szUserLoginCert=':'0192023a7bbd73250516f069df18b500'}
                headers = {'Host': '192.168.134.80'
                    'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0'
                    'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
                    'Accept-Language: pl,en-US;q=0.7,en;q=0.3'
                    'Accept-Encoding: gzip, deflate'
                    'Referer: http://192.168.134.80/index.html'
                    'Content-Type: application/x-www-form-urlencoded'
                    'Content-Length: 221'
                    'Connection: keep-alive'
                    'Upgrade-Insecure-Requests: 1'}


                datax = {"login":"my_login", "password":"my_password"}

                datamd = {
                    'lLan': '1',
                    'szUserName': 'admin',
                    'szUserLoginCert': '0192023a7bbd73250516f069df18b500'
                }

                responsex = requests.post('http://192.168.134.80/cgi-bin/main-cgi', data=datamd)

                #print(responsex.cookies)
                print(responsex.text)
                #print(responsex.status_code)
                #return requests.get(responsex.url).json()
                #responsex.json()
                #print (xjson)
                #print("xxxxxxxxxxxxxxxx")
                #print(responsex.url)
                #requests.get()

                #filepath = "LOGIN/HTML_" + ping_ip + ".html"
                #os.makedirs(os.path.dirname(filepath), exist_ok=True)
                #with open(filepath, 'w', encoding='utf-8') as g:
                #print(responsex.url,file=g)
                #print(responsex.text, file=g)
                #soup = BeautifulSoup(open("LOGIN/HTML_" + ping_ip + ".html"), "html.parser")
                #soup = BeautifulSoup("LOGIN/HTML1_" + ping_ip + ".html", "LOGIN/HTML2_" + ping_ip + ".html")
                #print(soup.prettify)
                newDictionary = json(str(soup))
                #print(soup)from json import loads


                #g = requests.get(cloud_nvr_unv_y.url)
                #print(g.headers)
                #print(g.cookies)
                #print(g.__attrs__)
                #print(g.status_code)
                #print(g.url)
                #print(g.request.headers)
                #print (g.text)
                #print (cloud_nvr_unv_y.url)HTML_192.168.134.80.html
                #r = requests.post(g.url, data=payloadxxx)
                #print(r.headers)
                #print(r.url)
                #print(r.status_code)
                #print(r.text)
                #print(r.headers)

                headerse = {
                    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0',

                }

                datae = {
                    'json': '{"cmd":149,"bIsEnable":1,"u8DdnsType":"0","szDdnsDomain":"p2pdevice.bcscctv.pl"}'
                }

                #responsen = requests.post('http://192.168.134.80/cgi-bin/main-cgi', headers=headerse, data=datae)
                #print(responsen.url)
                #print(responsen.text)
                #print(responsen.status_code)


                #p = requests.post(r.url, json=data)
                #print(p.status_code)
                #print("Cloud: \n" + cloud_nvr_unv_x.text)
                #print(r.url)
                #print(r.status_code)
                #print(cloud_nvr_unv_y.url)
                #print(cloud_nvr_unv_y.request)
                #print(requests.post)
                #max = requests.get()
                #curl 'http://192.168.134.79/cgi-bin/main-cgi' --data 'lLan=1&szUserName=admin&szUserLoginCert=0192023a7bbd73250516f069df18b500'



def set_unv_cloud2():
    while True:
        try:
            a = int(input("Podsieć: 192.168."))
            x = int(input("Zakres hostów od: 192.168." + str(a) + "."))
            y = int(input("Zakres hostów do: 192.168." + str(a) + ".")) + 1
        except ValueError:
            print('Wprowadzona została niepoprawna wartość.')
            continue
        login_text = ("Podaj login: ")
        passw_text = ("Podaj hasło: ")
        login = input(login_text)
        passw = input(passw_text)
        http = "http://"
        ip_uniview = "192.168." + str(a) + "."
        static = "/LAPI/V1.0/"
        static2 = "/cgi-bin/main-cgi/"
        cloud_nvr_unv = "Network/Cloud"
        p = pings.Ping()
        for i in range(x, y):
            ip_rest = str(i)
            ping_ip = str(ip_uniview + ip_rest)
            response = p.ping(ping_ip)
            print(ping_ip)
            #response = p.ping("192.168.135.50"))
            #print (response)
            if (response.is_reached()):
                cloud_nvr_unv_x = requests.get(http + ip_uniview + str(ip_rest) + str(static) + cloud_nvr_unv, auth=HTTPDigestAuth(login, passw))
                cloud_nvr_unv_y = requests.get(http + ip_uniview + str(ip_rest) + str(static2), auth=(login, passw))

                data2 = {"Enabled": 1,
                    "Domain": "bcs.pl",
                    "DeviceName": "UNIVIEW"}



#hashowanie hasła do MD5
                passwencode = str(passw).encode('utf-8')
                md5pass = (hashlib.md5(passwencode).hexdigest())
                print(md5pass)

                datamd5 = {
                    'lLan': '1',
                    'szUserName': login,
                    'szUserLoginCert': md5pass
                }

                datamd = {
                    'lLan': '1',
                    'szUserName': 'admin',
                    'szUserLoginCert': '0192023a7bbd73250516f069df18b500'
                }

#zapis do pliku HTML z logowania

                responsemd5 = requests.post(http+ping_ip+static2, data=datamd5)
                #responsemd5 = requests.post('http://192.168.134.80/cgi-bin/main-cgi', data=datamd)
                filepath = "LOGIN/HTML_" + ping_ip + ".html"
                os.makedirs(os.path.dirname(filepath), exist_ok=True)
                with open(filepath, 'w', encoding='utf-8') as g:
                    print(responsemd5.url, file=g)
                    print(responsemd5.text, file=g)
                    print(responsemd5.url)
                    mix = responsemd5.text
                    #print(responsemd5.text[520:570].split(":")[1], file=g)

#parsowanie
                #jsonparse = requests.open('GET','LOGIN/HTML_' + ping_ip + '.html').json()
                #print(jsonparse)

                s = """
                <div class="header-product js-header-product" data-product='{
            "sku": "218009200",
            "fullTitle": "iPhone 7 Apple 32GB Preto Matte 4G Tela 4.7”Retina - Câm. 12MP + Selfie 7MP iOS 11 Proc. Chip A10",
            "baseUrl": "https://www.myurl.com.br",
            "variationPath": "iphone-7-apple-32gb-preto-matte-4g-tela-4-7-retina-cam-12mp-selfie-7mp-ios-11-proc-chip-a10/p/2180092/te/iph7/",
            "imageUrl": "https://a-static.mlcdn.com.br/{w}x{h}/iphone-7-apple-32gb-preto-matte-4g-tela-4-7-retina-cam-12mp-selfie-7mp-ios-11-proc-chip-a10/myurl/218009200/f06f03c5ea2ba95deaa3e55e5e0e687e.jpg",
            "urlSubcategories": "https://www.myurl.com.br/iphone-7-e-iphone-7-plus/celulares-e-smartphones/s/te/iph7/",
            "quantitySellers": 1,
            "categoryId": "te",
            "serviceUrl": "/produto/garantia-plus/?product=218009200&amp;marketplaceSellerId=myrul&amp;productDiscountPrice=3199.00&amp;productCashPrice=2879.10&amp;productQuantity=10",
            "title": "iPhone 7 Apple 32GB Preto Matte 4G Tela 4....",
            "serviceUrl": "/produto/garantia-plus/?product=218009200&amp;marketplaceSellerId=myurl&amp;productDiscountPrice=3199.00&amp;productCashPrice=2879.10&amp;productQuantity=10",
            "bestPriceTemplate": " 2.879,10",
            "installmentQuantity": "10",
            "buyTogetherImage": "https://a-static.mlcdn.com.br/195x145/iphone-7-apple-32gb-preto-matte-4g-tela-4-7-retina-cam-12mp-selfie-7mp-ios-11-proc-chip-a10/myurl/218009200/f06f03c5ea2ba95deaa3e55e5e0e687e.jpg",
            "thumbailBuyTogether": "https://a-static.mlcdn.com.br/70x90/iphone-7-apple-32gb-preto-matte-4g-tela-4-7-retina-cam-12mp-selfie-7mp-ios-11-proc-chip-a10/myurl/218009200/f06f03c5ea2ba95deaa3e55e5e0e687e.jpg",
            "list_price_price_parcel_cash_price": "list_price_price_parcel_cash_price.html",
            "listPrice": " 3.499,90",
            "installmentAmount": " 319,90",
            "priceTemplate": " 3.199,00",
            "seller": "myurl",
            "attributes": [{"label":"Cor","value":"Preto Matte","type":"color","id":"218009200","image":"https:\/\/a-static.mlcdn.com.br\/{w}x{h}\/iphone-7-apple-32gb-preto-matte-4g-tela-4-7-retina-cam-12mp-selfie-7mp-ios-11-proc-chip-a10\/myurl\/218009200\/f06f03c5ea2ba95deaa3e55e5e0e687e.jpg","url":"\/iphone-7-apple-32gb-preto-matte-4g-tela-4-7-retina-cam-12mp-selfie-7mp-ios-11-proc-chip-a10\/p\/218009200\/te\/iph7\/","selected":true,"is_delivery_available":true}],
            "variations": ["Preto Matte"] }'> <h1 class="header-product__title" itemprop="name">iPhone 7 Apple 32GB Preto Matte 4G Tela 4.7”Retina - Câm. 12MP + Selfie 7MP iOS 11 Proc. Chip A10</h1> <small class="header-product__code">Código 218009200 <span class="header-product__separator"></span> <a class="header-product__text-interation js-floater-menu-link" href="#anchor-description">Ver descrição completa</a> <span class="header-product__separator"></span> <a class="header-product__text-interation" href="https://www.myurl.com.br/marcas/apple/" itemscope="" itemtype="http://schema.org/Brand"> <span itemprop="name">Apple</span> </a> <meta content="sku:218009200" itemprop="identifier"/> <meta content="http://schema.org/NewCondition" itemprop="itemCondition"/> </small> </div>
             """
                soup = BeautifulSoup(s, "html.parser")
                element = soup.find("div", class_="header-product js-header-product")
                print (element.attrs["data-product"])
                jsonData = json.loads(element.attrs["data-product"])  # Convert to JSON Object.
                print(jsonData['sku'])


                #soup = BeautifulSoup(open("LOGIN/HTML_" + ping_ip + ".html"), "html.parser")
                #soup = BeautifulSoup("LOGIN/HTML1_" + ping_ip + ".html", "LOGIN/HTML2_" + ping_ip + ".html")
                #print(soup.prettify)
                #newDictionary = json(str(soup))
                #print(soup)


                #g = requests.get(cloud_nvr_unv_y.url)
                #print(g.headers)
                #print(g.cookies)
                #print(g.__attrs__)
                #print(g.status_code)
                #print(g.url)
                #print(g.request.headers)
                #print (g.text)
                #print (cloud_nvr_unv_y.url)HTML_192.168.134.80.html
                #r = requests.post(g.url, data=payloadxxx)
                #print(r.headers)
                #print(r.url)
                #print(r.status_code)
                #print(r.text)
                #print(r.headers)

                headerse = {
                    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0',

                }

                datae = {
                    'json': '{"cmd":149,"bIsEnable":1,"u8DdnsType":"0","szDdnsDomain":"p2pdevice.bcscctv.pl"}'
                }

                #responsen = requests.post('http://192.168.134.80/cgi-bin/main-cgi', headers=headerse, data=datae)
                #print(responsen.url)
                #print(responsen.text)
                #print(responsen.status_code)


                #p = requests.post(r.url, json=data)
                #print(p.status_code)
                #print("Cloud: \n" + cloud_nvr_unv_x.text)
                #print(r.url)
                #print(r.status_code)
                #print(cloud_nvr_unv_y.url)
                #print(cloud_nvr_unv_y.request)
                #print(requests.post)
                #max = requests.get()
                #curl 'http://192.168.134.79/cgi-bin/main-cgi' --data 'lLan=1&szUserName=admin&szUserLoginCert=0192023a7bbd73250516f069df18b500'






def uniview_new():
    while True:
        try:
            a = int(input("Podsieć: 192.168."))
            x = int(input("Zakres hostów od: 192.168." + str(a) + "."))
            y = int(input("Zakres hostów do: 192.168." + str(a) + ".")) + 1
        except ValueError:
            print('Wprowadzona została niepoprawna wartość.')
            continue
        login_text = ("Podaj login: ")
        passw_text = ("Podaj hasło: ")
        login = input(login_text)
        passw = input(passw_text)
        http = "http://"
        ip_uniview = "192.168." + str(a) + "."
        static = "/LAPI/V1.0/"
        ddns_both_unv = "Network/DDNS"
        sd_both_unv = "Channel/0/System/DeviceStatus/SD"
        run_ipc_unv = "System/DeviceRunInfo"
        nets_ipc_unv = "NetWork/InterFace/Nets/0"
        mans_ipc_unv = "System/ManageServer"
        localtime_ipc_unv = "System/Time/LocalTime"
        time_ipc_unv = "Channel/0/System/Time"
        people_ipc_unv = "Channel/0/Smart/PeopleCount"
        dns_ipc_unv = "NetWork/DNS"
        port_ipc_unv = "NetWork/Port"
        videoinmode_ipc_unv = "Channel/0/Media/VideoInMode"
        video_ipc_unv = "Channel/0/Media/VideoEncode"
        storage_ipc_unv = "Channel/0/Media/Storage"
        living_ipc_unv = "Channel/0/Media/LivingStream"
        basic_ipc_unv = "System/DeviceBasicInfo"
        osd_ipc_unv = "Channel/0/Media/OSD"
        info_nvr_unv = "System/DeviceInfo"
        currentandsupport_nvr_unv = "System/Language/CurrentAndSupport"
        run_nvr_unv = "System/RunInfo"
        ntp_nvr_unv = "System/TimeNTP"
        ports_nvr_unv = "Network/Ports"
        upnp_nvr_unv = "Network/UPNP"
        channeldetailinfos_nvr_unv = "Channels/System/ChannelDetailInfos"
        containers_nvr_unv = "Storage/Containers"
        advanced_nvr_unv = "System/Advanced"
        cloud_nvr_unv = "Network/Cloud"
        p = pings.Ping()
        for i in range(x, y):
            ip_rest = str(i)
            ping_ip = str(ip_uniview + ip_rest)
            response = p.ping(ping_ip)
            print(ping_ip)
            #response = p.ping("192.168.135.50"))
            #print (response)
            if (response.is_reached()):
                ddns_both_unv_x=requests.get(http + ip_uniview + str(ip_rest) + str(static) + ddns_both_unv, auth=HTTPDigestAuth(login, passw))
                sd_both_unv_x=requests.get(http + ip_uniview + str(ip_rest) + str(static) + sd_both_unv, auth=HTTPDigestAuth(login, passw))
                run_ipc_unv_x=requests.get(http + ip_uniview + str(ip_rest) + str(static) + run_ipc_unv, auth=HTTPDigestAuth(login, passw))
                nets_ipc_unv_x=requests.get(http + ip_uniview + str(ip_rest) + str(static) + nets_ipc_unv, auth=HTTPDigestAuth(login, passw))
                mans_ipc_unv_x=requests.get(http + ip_uniview + str(ip_rest) + str(static) + mans_ipc_unv, auth=HTTPDigestAuth(login, passw))
                localtime_ipc_unv_x=requests.get(http + ip_uniview + str(ip_rest) + str(static) + localtime_ipc_unv, auth=HTTPDigestAuth(login, passw))
                time_ipc_unv_x=requests.get(http + ip_uniview + str(ip_rest) + str(static) + time_ipc_unv, auth=HTTPDigestAuth(login, passw))
                people_ipc_unv_x=requests.get(http + ip_uniview + str(ip_rest) + str(static) + people_ipc_unv, auth=HTTPDigestAuth(login, passw))
                dns_ipc_unv_x=requests.get(http + ip_uniview + str(ip_rest) + str(static) + dns_ipc_unv, auth=HTTPDigestAuth(login, passw))
                port_ipc_unv_x=requests.get(http + ip_uniview + str(ip_rest) + str(static) + port_ipc_unv, auth=HTTPDigestAuth(login, passw))
                videoinmode_ipc_unv_x=requests.get(http + ip_uniview + str(ip_rest) + str(static) + videoinmode_ipc_unv, auth=HTTPDigestAuth(login, passw))
                video_ipc_unv_x=requests.get(http + ip_uniview + str(ip_rest) + str(static) + video_ipc_unv, auth=HTTPDigestAuth(login, passw))
                storage_ipc_unv_x=requests.get(http + ip_uniview + str(ip_rest) + str(static) + storage_ipc_unv, auth=HTTPDigestAuth(login, passw))
                living_ipc_unv_x=requests.get(http + ip_uniview + str(ip_rest) + str(static) + living_ipc_unv, auth=HTTPDigestAuth(login, passw))
                basic_ipc_unv_x=requests.get(http + ip_uniview + str(ip_rest) + str(static) + basic_ipc_unv, auth=HTTPDigestAuth(login, passw))
                osd_ipc_unv_x=requests.get(http + ip_uniview + str(ip_rest) + str(static) + osd_ipc_unv, auth=HTTPDigestAuth(login, passw))
                info_nvr_unv_x=requests.get(http + ip_uniview + str(ip_rest) + str(static) + info_nvr_unv, auth=HTTPDigestAuth(login, passw))
                currentandsupport_nvr_unv_x=requests.get(http + ip_uniview + str(ip_rest) + str(static) + currentandsupport_nvr_unv, auth=HTTPDigestAuth(login, passw))
                run_nvr_unv_x=requests.get(http + ip_uniview + str(ip_rest) + str(static) + run_nvr_unv, auth=HTTPDigestAuth(login, passw))
                ntp_nvr_unv_x=requests.get(http + ip_uniview + str(ip_rest) + str(static) + ntp_nvr_unv, auth=HTTPDigestAuth(login, passw))
                ports_nvr_unv_x=requests.get(http + ip_uniview + str(ip_rest) + str(static) + ports_nvr_unv, auth=HTTPDigestAuth(login, passw))
                upnp_nvr_unv_x=requests.get(http + ip_uniview + str(ip_rest) + str(static) + upnp_nvr_unv, auth=HTTPDigestAuth(login, passw))
                channeldetailinfos_nvr_unv_x=requests.get(http + ip_uniview + str(ip_rest) + str(static) + channeldetailinfos_nvr_unv, auth=HTTPDigestAuth(login, passw))
                containers_nvr_unv_x=requests.get(http + ip_uniview + str(ip_rest) + str(static) + containers_nvr_unv, auth=HTTPDigestAuth(login, passw))
                advanced_nvr_unv_x=requests.get(http + ip_uniview + str(ip_rest) + str(static) + advanced_nvr_unv, auth=HTTPDigestAuth(login, passw))
                cloud_nvr_unv_x = requests.get(http + ip_uniview + str(ip_rest) + str(static) + cloud_nvr_unv, auth=HTTPDigestAuth(login, passw))
                #c = requests.get("192.168.135.50", auth=HTTPDigestAuth(login, passw))
                print("DDNS: \n"+ ddns_both_unv_x.text)
                print("SD: \n"+ sd_both_unv_x.text)
                print("RUNTIME: \n"+ run_ipc_unv_x.text)
                print("Netstat: \n"+ nets_ipc_unv_x.text)
                print("Mans: \n"+ mans_ipc_unv_x.text)
                print("Localtime: \n"+ localtime_ipc_unv_x.text)
                print("Time: \n"+ time_ipc_unv_x.text)
                print("People: \n"+ people_ipc_unv_x.text)
                print("Dns: \n"+ dns_ipc_unv_x.text)
                print("Port: \n"+ port_ipc_unv_x.text)
                print("Videoinmode: \n"+ videoinmode_ipc_unv_x.text)
                print("Video: \n"+ video_ipc_unv_x.text)
                print("Storage: \n"+ storage_ipc_unv_x.text)
                print("Living: \n"+ living_ipc_unv_x.text)
                print("Basic: \n"+ basic_ipc_unv_x.text)
                print("Osd: \n"+ osd_ipc_unv_x.text)
                print("Info: \n"+ info_nvr_unv_x.text)
                print("Currentsupport: \n"+ currentandsupport_nvr_unv_x.text)
                #print("Runtime nvr: \n"+ run_nvr_unv_x.text)
                #print("NTP: \n"+ ntp_nvr_unv_x.text)
                #print("Ports: \n"+ ports_nvr_unv_x.text)
                #print("Upnp: \n"+ upnp_nvr_unv_x.text)
                #print("Channeldetail: \n"+ channeldetailinfos_nvr_unv_x.text)
                #print("Containers: \n"+ containers_nvr_unv_x.text)
                #print("Advanced: \n"+ advanced_nvr_unv_x.text)
                print("Cloud: \n" + cloud_nvr_unv_x.text)
                print(cloud_nvr_unv_x.url)
                print(cloud_nvr_unv_x.request)
                #print(cloud_nvr_unv_x.content)
                #print(cloud_nvr_unv_x.reason)
                #print(cloud_nvr_unv_x.headers)
                #print(cloud_nvr_unv_x.cookies)
                #print(cloud_nvr_unv_x.raw)


            else:
                print("OFFLINE\n")
        break

main()


# /cgi-bin/configManager.cgi?action=getConfig&name=T2UServer' | grep 'RegisterServer' | awk -F '0].' '{print $2}'"))
# print (commands.getoutput("curl --digest -s -u 'admin:admin123' 'http://192.168.135.50/cgi-bin/magicBox.cgi?action=getMachineName'"))
# print (commands.getoutput("curl --digest -s -u 'admin:admin123' 'http://192.168.135.50/cgi-bin/magicBox.cgi?action=getHardwareVersion'"))
# print (commands.getoutput("curl --digest -s -u 'admin:admin123' 'http://192.168.135.50/cgi-bin/magicBox.cgi?action=getSoftwareVersion'"))
# print (commands.getoutput("curl --digest -s -u 'admin:admin123' 'http://192.168.135.50/cgi-bin/global.cgi?action=getCurrentTime'"))
# print (commands.getoutput("curl --digest -s -u 'admin:admin123' 'http://192.168.135.50/cgi-bin/configManager.cgi?action=getConfig&name=Network'"))
# print (commands.getoutput("curl --digest -s -u 'admin:admin123' 'http://192.168.135.50/cgi-bin/configManager.cgi?action=getConfig&name=ChannelTitle'"))
# print (commands.getoutput("curl --digest -s -u 'admin:admin123' 'http://192.168.135.50/cgi-bin/configManager.cgi?action=getConfig&name=Encode' | grep Video.Compression"))
# print ("192.168.135.50: \n"+commands.getoutput("curl --digest -s -u 'admin:admin123' 'http://192.168.135.50/cgi-bin/configManager.cgi?action=getConfig&name=T2UServer' | grep -v 'RegisterServer' | awk -F '0].' '{print $2}'"))