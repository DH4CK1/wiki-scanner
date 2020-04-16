#!/bin/python2.7
#-*- coding: utf-8 -*-
"""
Copyright (c) 2020 Dst_207
"""

"""
Silahkan dipelajari slur tools nya
tapi asal jangan di recode/reupload ya
kak kalo mau pelajari pelajari aja ok!
"""

import os, time, sys, json, re, requests
from bs4 import BeautifulSoup as bs
from var_animate import *

logo = banner('Wiki-Indo','Dst_207','0.1')
alert = animvar()
input = animinput()
## Coloring ##
c = color().show
me = c('red')
bi = c('blue')
i = c('green')
cy = c('cyan')
pu = c('white')
os.system('clear')
print(logo)
print('{}Team{}: {}Black Coder Crush {}& {}DevSecID\n').format(cy,me,pu,bi,pu)

key = input.ask('Masukan Keyword')
key = key.replace(' ','+')

res = requests.get('https://id.m.wikipedia.org/w/index.php?search={}&ns0=1'.format(key)).text
hasil = re.search('''<div class='mw-search-result-heading'><a href="(.*?)" title="(.*?)" data-serp-pos="0">''',res)
url = 'https://id.m.wikipedia.org'+hasil.group(1)
print('\n{}[{}*{}] {}Judul{}: {}{}').format(pu,i,pu,pu,me,cy,hasil.group(2))
time.sleep(1)
print('{}[{}*{}] {}Tautan{}: {}{}').format(pu,i,pu,pu,me,cy,url)
time.sleep(1)
print('\n  {}[  {}Pengertian {}{}  {}]').format(i,pu,bi,hasil.group(2),i)
print('{}<{}═════════════════════════════════════════════{}>').format(pu,bi,pu)
res2 = requests.get(url).text
b = bs(res2,"html.parser")
pengertian = b.find('p').text
pengertian = pengertian.replace('\n','')
print(pengertian)
print('{}<{}═════════════════════════════════════════════{}>').format(pu,bi,pu)
