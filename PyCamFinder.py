#!/usr/bin/python
import sys
import requests
from requests.auth import HTTPDigestAuth
import subprocess
from subprocess import PIPE, run
import pings

def main():
    print("____________________")

    menu()


def menu():
    choice = input("""
                    1: Rejestratory Dahua 
                    2: Kamery Dahua
                    3: Rejestratory Uniview
                    4: Kamery Uniview
                    5: Rejestratory Hikvision
                    6: Kamery Hikvision

                    0: Wyjście

                    Wybieram: """)

    if choice == '1':
        print("___________________________________________________________")
        print("\n Menu -> Rejestratory Dahua")
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
            dahua_nvr_new()
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
        dahua_ipc()
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
    ip_dahua = "192.168." + a + "."
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
        cloud = (login + ip_dahua + str(ip_rest) + cloud_rest)
        systeminfo = (login + ip_dahua + str(ip_rest) + systeminfo_rest)
        machinename = (login + ip_dahua + str(ip_rest) + machinename_rest)
        hardwareversion = (login + ip_dahua + str(ip_rest) + hardwareversion_rest)
        softwareVersion = (login + ip_dahua + str(ip_rest) + softwareVersion_rest)
        currentTime = (login + ip_dahua + str(ip_rest) + currentTime_rest)
        configNetwork = (login + ip_dahua + str(ip_rest) + configNetwork_rest)
        configChannelTitle = (login + ip_dahua + str(ip_rest) + configChannelTitle_rest)
        configEncode = (login + ip_dahua + str(ip_rest) + configEncode_rest)
        # test = cloud +"\n" + systeminfo +"\n" + machinename + "\n" + hardwareversion + "\n" +softwareVersion + "\n" + currentTime + "\n" + configNetwork + "\n" + configChannelTitle + "\n" + configEncode
        print("IP rejestratora dahua: {0}{1}\n".format(str(ip_dahua), str(ip_rest)))
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

def dahua_nvr_new():
    a = input("Podsieć: 192.168.")
    x = int(input("Zakres hostów od: 192.168." + a + "."))
    y = int(input("Zakres hostów do: 192.168." + a + ".")) + 1
    login_text = ("Podaj login: ")
    passw_text = ("Podaj hasło: ")
    login = input(login_text)
    passw = input(passw_text)
    http = "http://"
    ip_dahua = "192.168." + a + "."
    dahua_url = "/cgi-bin/magicBox.cgi?action=getSystemInfo"
    cloud_rest = "/cgi-bin/configManager.cgi?action=getConfig&name=T2UServer"
    p = pings.Ping()
    for i in range(x, y):
        ip_rest = str(i)
        ping_ip = str(ip_dahua + ip_rest)
        response = p.ping(ping_ip)
        print(ping_ip)
        #response = p.ping("192.168.135.50"))
        #print (response)
        if (response.is_reached()):
            systeminfo = requests.get(http + ip_dahua + str(ip_rest) + dahua_url, auth=HTTPDigestAuth(login, passw))
            cloud = requests.get(http + ip_dahua + str(ip_rest) + cloud_rest, auth=HTTPDigestAuth(login, passw))
            #c = requests.get("192.168.135.50", auth=HTTPDigestAuth(login, passw))
            print("Informacje systemowe: \n"+ systeminfo.text)
            print("Chmura: \n"+ cloud.text)
            #print(cloud.url)
            #print(c.status_code)
        else:
            print("OFFLINE\n")


def dahua_nvr_new_cloud():
    a = input("Podsieć: 192.168.")
    x = int(input("Zakres hostów od: 192.168." + a + "."))
    y = int(input("Zakres hostów do: 192.168." + a + ".")) + 1
    login_text = ("Podaj login: ")
    passw_text = ("Podaj hasło: ")
    login = input(login_text)
    passw = input(passw_text)
    http = "http://"
    ip_dahua = "192.168." + a + "."
    dahua_url = '/cgi-bin/magicBox.cgi?action=getSystemInfo'
    p = pings.Ping()
    for i in range(x, y):
        ip_rest = str(i)
        ping_ip = str(ip_dahua + ip_rest)
        response = p.ping(ping_ip)
        print(ping_ip)
        if (response.is_reached()):
            c = requests.get(http + ip_dahua + str(ip_rest) + dahua_url, auth=HTTPDigestAuth(login, passw))
            print(c.text)
        else:
            print("OFFLINE\n")


def dahua_nvr_cloud():
    a = input("Podsieć: 192.168.")
    x = int(input("Zakres hostów od: 192.168." + a + "."))
    y = int(input("Zakres hostów do: 192.168." + a + ".")) + 1
    login = "curl --digest -s -u 'admin:admin123' '"
    ip_dahua = "192.168." + a + "."
    for ip_rest in range(x, y):
        cloud_rest = "/cgi-bin/configManager.cgi?action=getConfig&name=T2UServer' | grep 'RegisterServer' | awk -F '0].' '{print $2}'"
        cloud = (login + ip_dahua + str(ip_rest) + cloud_rest)
        print("IP rejestratora dahua: {0}{1}\n".format(str(ip_dahua), str(ip_rest)))
        print(subprocess.Popen(cloud, shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip())



def dahua_nvr_ip():
    a = input("Podsieć: 192.168.")
    x = int(input("Zakres hostów od: 192.168." + a + "."))
    y = int(input("Zakres hostów do: 192.168." + a + ".")) + 1
    login = "curl --digest -s -u 'admin:admin123' '"
    ip_dahua = "192.168." + a + "."
    for ip_rest in range(x, y):
        configNetwork_rest = "/cgi-bin/configManager.cgi?action=getConfig&name=Network'"
        configNetwork = (login + ip_dahua + str(ip_rest) + configNetwork_rest)
        print("IP rejestratora dahua: {0}{1}\n".format(str(ip_dahua), str(ip_rest)))
        print(subprocess.Popen(configNetwork, shell=True, stdout=subprocess.PIPE).communicate()[0].decode(
            'utf-8').strip())


def dahua_nvr_encode():
    a = input("Podsieć: 192.168.")
    x = int(input("Zakres hostów od: 192.168." + a + "."))
    y = int(input("Zakres hostów do: 192.168." + a + ".")) + 1
    login = "curl --digest -s -u 'admin:admin123' '"
    ip_dahua = "192.168." + a + "."
    for ip_rest in range(x, y):
        configEncode_rest = "/cgi-bin/configManager.cgi?action=getConfig&name=Encode' | grep Video.Compression"
        configEncode = (login + ip_dahua + str(ip_rest) + configEncode_rest)
        print("IP rejestratora dahua: {0}{1}\n".format(str(ip_dahua), str(ip_rest)))
        print(
            subprocess.Popen(configEncode, shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip())


def dahua_nvr_time():
    a = input("Podsieć: 192.168.")
    x = int(input("Zakres hostów od: 192.168." + a + "."))
    y = int(input("Zakres hostów do: 192.168." + a + ".")) + 1
    login = "curl --digest -s -u 'admin:admin123' '"
    ip_dahua = "192.168." + a + "."
    for ip_rest in range(x, y):
        currentTime_rest = "/cgi-bin/global.cgi?action=getCurrentTime'"
        currentTime = (login + ip_dahua + str(ip_rest) + currentTime_rest)
        print("\nIP rejestratora dahua: {0}{1}\n".format(str(ip_dahua), str(ip_rest)))
        print(
            subprocess.Popen(currentTime, shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip())


def dahua_nvr_software():
    a = input("Podsieć: 192.168.")
    x = int(input("Zakres hostów od: 192.168." + a + "."))
    y = int(input("Zakres hostów do: 192.168." + a + ".")) + 1
    login = "curl --digest -s -u 'admin:admin123' '"
    ip_dahua = "192.168." + a + "."
    for ip_rest in range(x, y):
        softwareVersion_rest = "/cgi-bin/magicBox.cgi?action=getSoftwareVersion'"
        softwareVersion = (login + ip_dahua + str(ip_rest) + softwareVersion_rest)
        print("\nIP rejestratora dahua: {0}{1}\n".format(str(ip_dahua), str(ip_rest)))
        print(subprocess.Popen(softwareVersion, shell=True, stdout=subprocess.PIPE).communicate()[0].decode(
            'utf-8').strip())


def dahua_nvr_channelname():
    a = input("Podsieć: 192.168.")
    x = int(input("Zakres hostów od: 192.168." + a + "."))
    y = int(input("Zakres hostów do: 192.168." + a + ".")) + 1
    login = "curl --digest -s -u 'admin:admin123' '"
    ip_dahua = "192.168." + a + "."
    for ip_rest in range(x, y):
        configChannelTitle_rest = "/cgi-bin/configManager.cgi?action=getConfig&name=ChannelTitle'"
        configChannelTitle = (login + ip_dahua + str(ip_rest) + configChannelTitle_rest)
        print("\nIP rejestratora dahua: {0}{1}\n".format(str(ip_dahua), str(ip_rest)))
        print(subprocess.Popen(configChannelTitle, shell=True, stdout=subprocess.PIPE).communicate()[0].decode(
            'utf-8').strip())


def dahua_ipc():
    a = input("Podsieć: 192.168.")
    x = int(input("Zakres hostów od: 192.168." + a + "."))
    y = int(input("Zakres hostów do: 192.168." + a + ".")) + 1
    login = "curl -s -u 'admin:admin' '"
    ip_dahua = "192.168." + a + "."
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
        cloud = (login + ip_dahua + str(ip_rest) + cloud_rest)
        systeminfo = (login + ip_dahua + str(ip_rest) + systeminfo_rest)
        machinename = (login + ip_dahua + str(ip_rest) + machinename_rest)
        hardwareversion = (login + ip_dahua + str(ip_rest) + hardwareversion_rest)
        softwareVersion = (login + ip_dahua + str(ip_rest) + softwareVersion_rest)
        currentTime = (login + ip_dahua + str(ip_rest) + currentTime_rest)
        configNetwork = (login + ip_dahua + str(ip_rest) + configNetwork_rest)
        configChannelTitle = (login + ip_dahua + str(ip_rest) + configChannelTitle_rest)
        configEncode = (login + ip_dahua + str(ip_rest) + configEncode_rest)
        # test = cloud +"\n" + systeminfo +"\n" + machinename + "\n" + hardwareversion + "\n" +softwareVersion + "\n" + currentTime + "\n" + configNetwork + "\n" + configChannelTitle + "\n" + configEncode
        print("IP kamery dahua: {0}{1}\n".format(str(ip_dahua), str(ip_rest)))
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

