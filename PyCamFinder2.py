#!/usr/bin/python
import sys
import requests
from requests.auth import HTTPDigestAuth
import subprocess
from subprocess import PIPE, run
import pings
import socket
from datetime import datetime

socket.setdefaulttimeout(0.5)

def main():
    print ("\n\n")
    print("_______________ PyCamScanner v1.0 _______________")
    print("\n")
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
                    1: Kompletny raport
                    2: Chmura
                    3: Adresy IP
                    4: Kodowanie H.264/H.265
                    5: Ustawione godziny
                    6: Wersja oprogramowania
                    7: Nazwy kanałów

                    9: Powrót do menu
                    0: Wyjście

                    Wybieram: """)
        if choice == '1':
            dahua_new()
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
            dahua_nvr_new_ip()
        elif choice == '9':
            menu()
        elif choice == '0':
            sys.exit()
        else:
            print("Podana została nieobsługiwana wartość")
            menu()

    elif choice == '2':
        uniview_new()
        #save_to_file()
    elif choice == '3':
        uniview_nvr()
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



def dahua_nvr_old():
    a = input("Podsieć: 192.168.")
    x = int(input("Zakres hostów od: 192.168." + a + "."))
    y = int(input("Zakres hostów do: 192.168." + a + ".")) + 1
    login = "curl --digest -s -u 'admin:admin123' '"
    ip_uniview = "192.168." + a + "."
    for ip_rest in range(x, y):
        cloud_rest = "/cgi-bin/configManager.cgi?action=getConfig&name=T2UServer' | grep 'RegisterServer' | awk -F '0].' '{print $2}'"
        systeminfo_rest = "/cgi-bin/magicBox.cgi?action=getSystemInfo'"
        machinename_rest = "/cgi-bin/magicBox.cgi?action=getMachineName'"
        hardwareversion_rest = "/cgi-bin/magicBox.cgi?action=getHardwareVersion'"
        softwareVersion_rest = "/cgi-bin/magicBox.cgi?action=getSoftwareVersion'"
        currentTime_rest = "/cgi-bin/global.cgi?action=getCurrentTime'"
        configNetwork_rest = "/cgi-bin/configManager.cgi?action=getConfig&name=Network'"
        configChannelTitle_rest = "/cgi-bin/configManager.cgi?action=getConfig&name=ChannelTitle'"
        configEncode_rest = "/cgi-bin/configManager.cgi?action=getConfig&name=Encode' | grep Video.Compression"
        cloud = (login + ip_uniview + str(ip_rest) + cloud_rest)
        systeminfo = (login + ip_uniview + str(ip_rest) + systeminfo_rest)
        machinename = (login + ip_uniview + str(ip_rest) + machinename_rest)
        hardwareversion = (login + ip_uniview + str(ip_rest) + hardwareversion_rest)
        softwareVersion = (login + ip_uniview + str(ip_rest) + softwareVersion_rest)
        currentTime = (login + ip_uniview + str(ip_rest) + currentTime_rest)
        configNetwork = (login + ip_uniview + str(ip_rest) + configNetwork_rest)
        configChannelTitle = (login + ip_uniview + str(ip_rest) + configChannelTitle_rest)
        configEncode = (login + ip_uniview + str(ip_rest) + configEncode_rest)
        # test = cloud +"\n" + systeminfo +"\n" + machinename + "\n" + hardwareversion + "\n" +softwareVersion + "\n" + currentTime + "\n" + configNetwork + "\n" + configChannelTitle + "\n" + configEncode
        print("IP rejestratora dahua: {0}{1}\n".format(str(ip_uniview), str(ip_rest)))
        print(subprocess.Popen(cloud, shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip())
        print(subprocess.Popen(systeminfo, shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip())
        print(
            subprocess.Popen(machinename, shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip())
        print(subprocess.Popen(hardwareversion, shell=True, stdout=subprocess.PIPE).communicate()[0].decode(
            'utf-8').strip())
        print(subprocess.Popen(softwareVersion, shell=True, stdout=subprocess.PIPE).communicate()[0].decode(
            'utf-8').strip())
        print(
            subprocess.Popen(currentTime, shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip())
        print(subprocess.Popen(configNetwork, shell=True, stdout=subprocess.PIPE).communicate()[0].decode(
            'utf-8').strip())
        print(subprocess.Popen(configChannelTitle, shell=True, stdout=subprocess.PIPE).communicate()[0].decode(
            'utf-8').strip())
        print(
            subprocess.Popen(configEncode, shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip())

def dahua_new():
    a = input("Podsieć: 192.168.")
    x = int(input("Zakres hostów od: 192.168." + a + "."))
    y = int(input("Zakres hostów do: 192.168." + a + ".")) + 1
    login_text = ("Podaj login: ")
    passw_text = ("Podaj hasło: ")
    login = input(login_text)
    passw = input(passw_text)
    http = "http://"
    ip_uniview = "192.168." + a + "."
    uniview_url = "/cgi-bin/magicBox.cgi?action=getSystemInfo"
    cloud_rest = "/cgi-bin/configManager.cgi?action=getConfig&name=T2UServer"
    confignetwork_rest = "/cgi-bin/configManager.cgi?action=getConfig&name=Network"
    configencode_rest = "/cgi-bin/configManager.cgi?action=getConfig&name=Encode"
    currenttime_rest = "/cgi-bin/global.cgi?action=getCurrentTime"
    softwareversion_rest = "/cgi-bin/magicBox.cgi?action=getSoftwareVersion"
    channeltitle_rest = "/cgi-bin/configManager.cgi?action=getConfig&name=ChannelTitle"
    p = pings.Ping()
    for i in range(x, y):
        ip_rest = str(i)
        ping_ip = str(ip_uniview + ip_rest)
        response = p.ping(ping_ip)
        print(ping_ip)
        #response = p.ping("192.168.135.50"))
        #print (response)
        if (response.is_reached()):
            systeminfo = requests.get(http + ip_uniview + str(ip_rest) + uniview_url, auth=HTTPDigestAuth(login, passw))
            cloud = requests.get(http + ip_uniview + str(ip_rest) + cloud_rest, auth=HTTPDigestAuth(login, passw))
            confignetwork = requests.get(http + ip_uniview + str(ip_rest) + confignetwork_rest, auth=HTTPDigestAuth(login, passw))
            configencode = requests.get(http + ip_uniview + str(ip_rest) + configencode_rest, auth=HTTPDigestAuth(login, passw))
            currenttime = requests.get(http + ip_uniview + str(ip_rest) + currenttime_rest,auth=HTTPDigestAuth(login, passw))
            softwareversion = requests.get(http + ip_uniview + str(ip_rest) +softwareversion_rest,auth=HTTPDigestAuth(login, passw))
            channeltitle = requests.get(http + ip_uniview + str(ip_rest) + channeltitle_rest,auth=HTTPDigestAuth(login, passw))
            #c = requests.get("192.168.135.50", auth=HTTPDigestAuth(login, passw))
            #file = open('Dahua.txt', 'w')
            #file.write(
            print("Informacje systemowe: \n"+ systeminfo.text)
            print("Czas: \n" + currenttime.text)
            print("Wersja oprogramowania: \n" + softwareversion.text)
            print("Chmura: \n"+ cloud.text)
            print("Konfiguracja sieci: \n" + confignetwork.text)
            print("Kodowanie: \n" + configencode.text)
            print("Kanały: \n" + channeltitle.text)
            print(confignetwork.url)
            print(confignetwork.status_code)
        else:
            print("OFFLINE\n")
            #)
            #file.close()


def dahua_nvr_new_cloud():

    a = input("Podsieć: 192.168.")
    x = int(input("Zakres hostów od: 192.168." + a + "."))
    y = int(input("Zakres hostów do: 192.168." + a + ".")) + 1
    login_text = ("Podaj login: ")
    passw_text = ("Podaj hasło: ")
    login = input(login_text)
    passw = input(passw_text)
    http = "http://"
    ip_uniview = "192.168." + a + "."
    cloud_rest = "/cgi-bin/configManager.cgi?action=getConfig&name=T2UServer"
    p = pings.Ping()
    for i in range(x, y):
        ip_rest = str(i)
        ping_ip = str(ip_uniview + ip_rest)
        response = p.ping(ping_ip)
        print("\n"+ping_ip+"\n")
        if (response.is_reached()):
            #rejestratory
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


def dahua_nvr_ip():
    a = input("Podsieć: 192.168.")
    x = int(input("Zakres hostów od: 192.168." + a + "."))
    y = int(input("Zakres hostów do: 192.168." + a + ".")) + 1
    login = "curl --digest -s -u 'admin:admin123' '"
    ip_uniview = "192.168." + a + "."
    for ip_rest in range(x, y):
        cloud_rest = "/cgi-bin/configManager.cgi?action=getConfig&name=T2UServer' | grep 'RegisterServer' | awk -F '0].' '{print $2}'"
        cloud = (login + ip_uniview + str(ip_rest) + cloud_rest)
        print("IP rejestratora dahua: {0}{1}\n".format(str(ip_uniview), str(ip_rest)))
        print(subprocess.Popen(cloud, shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip())


def dahua_nvr_new_ip():
    a = input("Podsieć: 192.168.")
    x = int(input("Zakres hostów od: 192.168." + a + "."))
    y = int(input("Zakres hostów do: 192.168." + a + ".")) + 1
    login_text = ("Podaj login: ")
    passw_text = ("Podaj hasło: ")
    login = input(login_text)
    passw = input(passw_text)
    http = "http://"
    ip_uniview = "192.168." + a + "."
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


def dahua_nvr_ip():
    a = input("Podsieć: 192.168.")
    x = int(input("Zakres hostów od: 192.168." + a + "."))
    y = int(input("Zakres hostów do: 192.168." + a + ".")) + 1
    login = "curl --digest -s -u 'admin:admin123' '"
    ip_uniview = "192.168." + a + "."
    for ip_rest in range(x, y):
        configNetwork_rest = "/cgi-bin/configManager.cgi?action=getConfig&name=Network'"
        configNetwork = (login + ip_uniview + str(ip_rest) + configNetwork_rest)
        print("IP rejestratora dahua: {0}{1}\n".format(str(ip_uniview), str(ip_rest)))
        print(subprocess.Popen(configNetwork, shell=True, stdout=subprocess.PIPE).communicate()[0].decode(
            'utf-8').strip())


def dahua_nvr_encode():
    a = input("Podsieć: 192.168.")
    x = int(input("Zakres hostów od: 192.168." + a + "."))
    y = int(input("Zakres hostów do: 192.168." + a + ".")) + 1
    login = "curl --digest -s -u 'admin:admin123' '"
    ip_uniview = "192.168." + a + "."
    for ip_rest in range(x, y):
        configEncode_rest = "/cgi-bin/configManager.cgi?action=getConfig&name=Encode' | grep Video.Compression"
        configEncode = (login + ip_uniview + str(ip_rest) + configEncode_rest)
        print("IP rejestratora dahua: {0}{1}\n".format(str(ip_uniview), str(ip_rest)))
        print(
            subprocess.Popen(configEncode, shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip())




def dahua_nvr_new_encode():
    a = input("Podsieć: 192.168.")
    x = int(input("Zakres hostów od: 192.168." + a + "."))
    y = int(input("Zakres hostów do: 192.168." + a + ".")) + 1
    login_text = ("Podaj login: ")
    passw_text = ("Podaj hasło: ")
    login = input(login_text)
    passw = input(passw_text)
    http = "http://"
    ip_uniview = "192.168." + a + "."
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



def dahua_nvr_time():
    a = input("Podsieć: 192.168.")
    x = int(input("Zakres hostów od: 192.168." + a + "."))
    y = int(input("Zakres hostów do: 192.168." + a + ".")) + 1
    login = "curl --digest -s -u 'admin:admin123' '"
    ip_uniview = "192.168." + a + "."
    for ip_rest in range(x, y):
        currentTime_rest = "/cgi-bin/global.cgi?action=getCurrentTime'"
        currentTime = (login + ip_uniview + str(ip_rest) + currentTime_rest)
        print("\nIP rejestratora dahua: {0}{1}\n".format(str(ip_uniview), str(ip_rest)))
        print(
            subprocess.Popen(currentTime, shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip())


def dahua_nvr_new_time():
    a = input("Podsieć: 192.168.")
    x = int(input("Zakres hostów od: 192.168." + a + "."))
    y = int(input("Zakres hostów do: 192.168." + a + ".")) + 1
    login_text = ("Podaj login: ")
    passw_text = ("Podaj hasło: ")
    login = input(login_text)
    passw = input(passw_text)
    http = "http://"
    ip_uniview = "192.168." + a + "."
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


def dahua_nvr_software():
    a = input("Podsieć: 192.168.")
    x = int(input("Zakres hostów od: 192.168." + a + "."))
    y = int(input("Zakres hostów do: 192.168." + a + ".")) + 1
    login = "curl --digest -s -u 'admin:admin123' '"
    ip_uniview = "192.168." + a + "."
    for ip_rest in range(x, y):
        softwareVersion_rest = "/cgi-bin/magicBox.cgi?action=getSoftwareVersion'"
        softwareVersion = (login + ip_uniview + str(ip_rest) + softwareVersion_rest)
        print("\nIP rejestratora dahua: {0}{1}\n".format(str(ip_uniview), str(ip_rest)))
        print(subprocess.Popen(softwareVersion, shell=True, stdout=subprocess.PIPE).communicate()[0].decode(
            'utf-8').strip())


def dahua_nvr_new_software():
    a = input("Podsieć: 192.168.")
    x = int(input("Zakres hostów od: 192.168." + a + "."))
    y = int(input("Zakres hostów do: 192.168." + a + ".")) + 1
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



def dahua_nvr_channelname():
    a = input("Podsieć: 192.168.")
    x = int(input("Zakres hostów od: 192.168." + a + "."))
    y = int(input("Zakres hostów do: 192.168." + a + ".")) + 1
    login = "curl --digest -s -u 'admin:admin123' '"
    ip_uniview = "192.168." + a + "."
    for ip_rest in range(x, y):
        configChannelTitle_rest = "/cgi-bin/configManager.cgi?action=getConfig&name=ChannelTitle'"
        configChannelTitle = (login + ip_uniview + str(ip_rest) + configChannelTitle_rest)
        print("\nIP rejestratora dahua: {0}{1}\n".format(str(ip_uniview), str(ip_rest)))
        print(subprocess.Popen(configChannelTitle, shell=True, stdout=subprocess.PIPE).communicate()[0].decode(
            'utf-8').strip())


def dahua_nvr_new_channelname():
    a = input("Podsieć: 192.168.")
    x = int(input("Zakres hostów od: 192.168." + a + "."))
    y = int(input("Zakres hostów do: 192.168." + a + ".")) + 1
    login_text = ("Podaj login: ")
    passw_text = ("Podaj hasło: ")
    login = input(login_text)
    passw = input(passw_text)
    http = "http://"
    ip_uniview = "192.168." + a + "."
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



def dahua_ipc():
    a = input("Podsieć: 192.168.")
    x = int(input("Zakres hostów od: 192.168." + a + "."))
    y = int(input("Zakres hostów do: 192.168." + a + ".")) + 1
    login = "curl -s -u 'admin:admin' '"
    ip_uniview = "192.168." + a + "."
    for ip_rest in range(x, y):
        cloud_rest = "/cgi-bin/configManager.cgi?action=getConfig&name=T2UServer' | grep 'RegisterServer' | awk -F '0].' '{print $2}'"
        systeminfo_rest = "/cgi-bin/magicBox.cgi?action=getSystemInfo'"
        machinename_rest = "/cgi-bin/magicBox.cgi?action=getMachineName'"
        hardwareversion_rest = "/cgi-bin/magicBox.cgi?action=getHardwareVersion'"
        softwareVersion_rest = "/cgi-bin/magicBox.cgi?action=getSoftwareVersion'"
        currentTime_rest = "/cgi-bin/global.cgi?action=getCurrentTime'"
        configNetwork_rest = "/cgi-bin/configManager.cgi?action=getConfig&name=Network'"
        configChannelTitle_rest = "/cgi-bin/configManager.cgi?action=getConfig&name=ChannelTitle'"
        configEncode_rest = "/cgi-bin/configManager.cgi?action=getConfig&name=Encode' | grep Video.Compression"
        cloud = (login + ip_uniview + str(ip_rest) + cloud_rest)
        systeminfo = (login + ip_uniview + str(ip_rest) + systeminfo_rest)
        machinename = (login + ip_uniview + str(ip_rest) + machinename_rest)
        hardwareversion = (login + ip_uniview + str(ip_rest) + hardwareversion_rest)
        softwareVersion = (login + ip_uniview + str(ip_rest) + softwareVersion_rest)
        currentTime = (login + ip_uniview + str(ip_rest) + currentTime_rest)
        configNetwork = (login + ip_uniview + str(ip_rest) + configNetwork_rest)
        configChannelTitle = (login + ip_uniview + str(ip_rest) + configChannelTitle_rest)
        configEncode = (login + ip_uniview + str(ip_rest) + configEncode_rest)
        # test = cloud +"\n" + systeminfo +"\n" + machinename + "\n" + hardwareversion + "\n" +softwareVersion + "\n" + currentTime + "\n" + configNetwork + "\n" + configChannelTitle + "\n" + configEncode
        print("IP kamery dahua: {0}{1}\n".format(str(ip_uniview), str(ip_rest)))
        print(subprocess.Popen(cloud, shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip())
        print(subprocess.Popen(systeminfo, shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip())
        print(
            subprocess.Popen(machinename, shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip())
        print(subprocess.Popen(hardwareversion, shell=True, stdout=subprocess.PIPE).communicate()[0].decode(
            'utf-8').strip())
        print(subprocess.Popen(softwareVersion, shell=True, stdout=subprocess.PIPE).communicate()[0].decode(
            'utf-8').strip())
        print(
            subprocess.Popen(currentTime, shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip())
        print(subprocess.Popen(configNetwork, shell=True, stdout=subprocess.PIPE).communicate()[0].decode(
            'utf-8').strip())
        print(subprocess.Popen(configChannelTitle, shell=True, stdout=subprocess.PIPE).communicate()[0].decode(
            'utf-8').strip())
        print(
            subprocess.Popen(configEncode, shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip())


def uniview_nvr():
    a = input("Podsieć: 192.168.")
    x = int(input("Zakres hostów od: 192.168." + a + "."))
    y = int(input("Zakres hostów do: 192.168." + a + ".")) + 1
    login = "curl -s -u 'admin:admin123' '"
    ip_uniview = "192.168." + a + "."
    for ip_rest in range(x, y):
        timentp_rest = "/LAPI/V1.0/System/TimeNTP'"
        runinfo_rest = "/LAPI/V1.0/System/RunInfo'"
        lang_rest = "/LAPI/V1.0/System/Language/CurrentAndSupport'"
        timentp = (login + ip_uniview + str(ip_rest) + timentp_rest)
        runinfo = (login + ip_uniview + str(ip_rest) + runinfo_rest)
        lang = (login + ip_uniview + str(ip_rest) + lang_rest)
        # test = cloud +"\n" + systeminfo +"\n" + machinename + "\n" + hardwareversion + "\n" +softwareVersion + "\n" + currentTime + "\n" + configNetwork + "\n" + configChannelTitle + "\n" + configEncode
        print("IP kamery uniview: {0}{1}\n".format(str(ip_uniview), str(ip_rest)))
        print(subprocess.Popen(timentp, shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip())
        print(subprocess.Popen(runinfo, shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip())
        print(subprocess.Popen(lang, shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip())


def uniview_new():
    a = input("Podsieć: 192.168.")
    x = int(input("Zakres hostów od: 192.168." + a + "."))
    y = int(input("Zakres hostów do: 192.168." + a + ".")) + 1
    login_text = ("Podaj login: ")
    passw_text = ("Podaj hasło: ")
    login = input(login_text)
    passw = input(passw_text)
    http = "http://"
    ip_uniview = "192.168." + a + "."
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
            print("Runtime nvr: \n"+ run_nvr_unv_x.text)
            print("NTP: \n"+ ntp_nvr_unv_x.text)
            print("Ports: \n"+ ports_nvr_unv_x.text)
            print("Upnp: \n"+ upnp_nvr_unv_x.text)
            print("Channeldetail: \n"+ channeldetailinfos_nvr_unv_x.text)
            print("Containers: \n"+ containers_nvr_unv_x.text)
            print("Advanced: \n"+ advanced_nvr_unv_x.text)
            #print(systeminfo.url)
            #print(systeminfo.status_code)
        else:
            print("OFFLINE\n")    

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