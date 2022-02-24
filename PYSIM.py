#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests,os
class _7sim:
    @classmethod
    def GetNumbers(c):

        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
        }
        phones = []
        decode = []

        whisper = requests.get("https://7sim.net/", headers=headers)
        src = whisper.content
        soup = BeautifulSoup(src, "html.parser", from_encoding="iso-8859-1")

        phone = soup.find_all("a", {'class': 'npn nol'})
        for i in range(len(phone)):
            data = str(phone[i].text).strip()
            decode.append(str(phone[i].attrs['href']).strip())
            if '+' in data:
                phones.append(data)

        return phones, decode

    @classmethod
    def GetCode(c, url):

        smss = []
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
        }

        whisper = requests.get(url, headers=headers)
        src = whisper.content
        soup = BeautifulSoup(src, "html.parser", from_encoding="iso-8859-1")
        sms = soup.find_all("td")
        for i in range(len(sms)):
            data = str(sms[i].text).strip()
            smss.append(data)

        return smss


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def Home():
    os.system('clear')
    c = 0
    Numbers = _7sim.GetNumbers()[0]
    DecodedUrls = _7sim.GetNumbers()[1]

    print('''________   _______ ________  ___
| ___ \ \ / /  ___|_   _|  \/  |
| |_/ /\ V /\ `--.  | | | .  . |
|  __/  \ /  `--. \ | | | |\/| |
| |     | | /\__/ /_| |_| |  | |
\_|     \_/ \____/ \___/\_|  |_/
=================================''')
    for i in Numbers:
        print(f' [{c}] {i}')
        c += 1

    inp = int(input('\n - What is your chose: '))
    sms = (_7sim.GetCode(DecodedUrls[inp]))

    a = 0
    b = 1
    c = 2

    print(' ---------------------------------------------------')
    for s in range(len(sms)):
        try:
            print(' ' + sms[a] + ' | ' + sms[b] + ' | ' + sms[c])
            a += 3
            b += 3
            c += 3
        except:
            pass
    print(' ---------------------------------------------------')
    input(' - Press any thing to go back: ')

    cls()
    Home()


Home()