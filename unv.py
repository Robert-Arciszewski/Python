#!/usr/bin/python3
import json
import requests
from requests.auth import HTTPDigestAuth
import pings
import os
import hashlib
import re
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

def set_unv_cloud():
    while True:
        try:
            a = int(input("Podsieć: 192.168."))
            x = int(input("Zakres hostów od: 192.168." + str(a) + "."))
            y = int(input("Zakres hostów do: 192.168." + str(a) + ".")) + 1
        except ValueError:
            print('Wprowadzona została niepoprawna wartość.')
            continue
        login = WordCompleter(['admin', 'admin1', 'user'])
        login = prompt('Podaj login: ', completer=login)
        login_ac = str(login)
        #login = input("Podaj login: ")

        passw = WordCompleter(['admin123', 'admin', 'Niedzmin1'])
        passw = prompt('Podaj hasło: ', completer=passw)
        passw_ac = str(passw)

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
            if (response.is_reached()):
                info_nvr_unv = "System/DeviceInfo"
                info_nvr_unv_x = requests.get(http + ip_uniview + str(ip_rest) + str(static) + info_nvr_unv,auth=HTTPDigestAuth(login_ac, passw_ac))
                x = json.loads(info_nvr_unv_x.text)
                firmwareversion = (x['Response']['Data']['FirmwareVersion'])
                firmsubstr = int(firmwareversion[3:5])
                fw = "D"+str(firmsubstr)
                print("Wersja firmware: " +fw)
                if(firmsubstr>22):
                    cloud_nvr_unv_x = requests.get(http + ip_uniview + str(ip_rest) + str(static) + cloud_nvr_unv,auth=HTTPDigestAuth(login, passw))
                    cloudname = WordCompleter(['p2pdevice.bcscctv.pl', 'p2p.bcscctv.pl', 'test', 'nic'])
                    prompt('Podaj adres chmury lub wybierz z listy: ', completer=cloudname)
                    cloudname = str(cloudname)
                    cloudstatus = int(input("Czy włączamy chmurę? 0 - NIE, 1 - TAK: "))
                    data = {"Enabled": cloudstatus,
                            "Domain": "" + cloudname + "",
                            "DeviceName": "UNIVIEW"}
                    r = requests.put(cloud_nvr_unv_x.url, auth=HTTPDigestAuth(login, passw), json=data)
                    if (r.status_code != 200):
                        print("Wystąpił nieznany problem, chmura niustawiona. Kod błędu: " + r.status_code)
                    else:
                        print("Adres chmury zmieniony a status chmury ustawiony na " + str(cloudstatus))
                else:

                    cloudname = WordCompleter(['p2pdevice.bcscctv.pl', 'p2p.bcscctv.pl', 'test', 'nic'])
                    prompt('Podaj adres chmury lub wybierz z listy: ', completer=cloudname)
                    cloudname = str(cloudname)
                    cloudstatus = str(input("Czy włączamy chmurę? 0 - NIE, 1 - TAK: "))

                # hashowanie hasła do MD5
                    passwencode = str(passw_ac).encode('utf-8')
                    md5pass = (hashlib.md5(passwencode).hexdigest())

                    datamd5 = {
                        'szUserName': str(login_ac),
                        'szUserLoginCert': md5pass
                    }

                # zapis do pliku JSON z logowania

                    responsemd5 = requests.post(http + ping_ip + static2, data=datamd5)
                    filepath = "LOGIN/JSON_" + ping_ip + ".html"
                    os.makedirs(os.path.dirname(filepath), exist_ok=True)
                    with open(filepath, 'w', encoding='utf-8') as j:
                        JSON = re.compile('GLOBAL_INFO = ({.*?});', re.DOTALL)
                        matches = JSON.search(responsemd5.text)
                        completejson = matches.group(1)
                        jsonx = json.loads(completejson)
                        session_handler = jsonx['stUserInfo']['u32UserLoginHandle']
                        string_session_handler = str(session_handler)

                        data = '{"cmd":149,"bIsEnable":'+cloudstatus+',"u8DdnsType":"0","szDdnsDomain":"'+cloudname+'","szDeviceName":"","szDdnsUserName":"","szDdnsPassword":"","szUserName":"admin","u32UserLoginHandle":'+string_session_handler+'}'
                        response = requests.post(responsemd5.url, data=data)
                        if (response.status_code != 200):
                            print("Wystąpił nieznany problem, chmura nieustawiona. Kod błędu: " + r.status_code)
                        else:
                            print("Adres chmury został zmieniony a status ustawiono na " + str(cloudstatus))
            else:
                print("OFFLINE")
        break
set_unv_cloud()