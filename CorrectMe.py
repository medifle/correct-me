#!/usr/bin/python3

import os
import argparse
from codecs import decode
from codecs import encode
from base64 import b64encode
from base64 import b64decode

parser = argparse.ArgumentParser(description='Process the input.')
parser.add_argument('input', metavar='N', type=str, nargs='+')
flag = parser.parse_args().input[0]

print('Correct the variables and the code to get the proper input :)')

alpha = True
beta = 1
charlie = chr(ord(str(beta)))
delta = 47
echo = 24

if len(flag) < (delta+beta)/4*len(charlie) + beta and len(flag[-1])*(len(str(beta+int(charlie)+delta-echo))+beta)*beta*2*2-beta < len(flag):
    print("entered if block")
    foxtrot = chr(ord(str(b64encode(bytes(flag,'utf-8')))[6])-echo) + encode(str(b64encode(bytes(flag,'utf-8')))[3].lower(), 'rot_13') + ' ' + encode(str(b64encode(bytes(flag,'utf-8')))[5:3:-1].lower(), 'rot_13')
    foxtrot = foxtrot + ' ' + str(b64encode(bytes(flag,'utf-8')))[10] + chr(ord(str(b64encode(bytes(flag,'utf-8')))[10])+beta) + chr(ord(str(b64encode(bytes(flag,'utf-8')))[10])+2*beta) + foxtrot[3] + decode(str(b64encode(bytes(flag,'utf-8')))[6], 'rot_13') + foxtrot[0:2].lower()
    foxtrot = foxtrot + foxtrot[7] + str(b64encode(bytes(flag,'utf-8')))[-beta*(beta+beta)] + 'y'
    foxtrot = foxtrot + foxtrot[-11] + decode(str(b64encode(bytes(flag,'utf-8')))[beta-1], 'rot_13') + str(b64encode(bytes(flag,'utf-8')))[beta-1] + foxtrot[beta*4] + str(b64encode(bytes(flag,'utf-8')))[4].lower()
    foxtrot = foxtrot + str(b64encode(bytes(flag,'utf-8')))[-10] + foxtrot[-2] + chr(ord(str(b64encode(bytes(flag,'utf-8')))[-5])+int(charlie)) + str(b64encode(bytes(flag,'utf-8')))[6] + 'ted in here.'
    foxtrot = bytes(foxtrot, 'utf-8')
    golf = ''.join([chr(ord(str(b64encode(foxtrot))[39])+32), str(b64encode(foxtrot))[6], chr(ord(str(b64encode(foxtrot))[21])+1)])
    hotel = decode(golf, 'rot_13')
    india = int(9/3) * '\u0075'
    juliet = 'less' + '\u0074' + 'hotel'[0] + flag[1] + 'n' + str(3)
    kilo = flag[1] + 2*flag[10]
    lima = golf[0] + flag[2] + flag[10-beta]
    mike = '\u0077' + hotel[0]
    for letter in juliet:
        print(letter)
    november = lima[:-1] + hotel[1] + golf[1-1+1+1-1-1-1] + flag[4:7]
    oscar = chr(ord(str(b64encode(foxtrot))[25])-1)
    papa = hotel[0]
    quebec = kilo[-1]
    romeo = str(b64encode(foxtrot))[delta - echo]
    while delta > echo:
        echo += len(juliet)
    sierra = juliet[int(-(echo-delta)/2)]
    tango = juliet[delta-echo]
    uniform = juliet[echo-delta]
    victor = str(echo + int(juliet[-1]))
    whiskey = 3*( '\u0077' )
    xray = '\u0054'
    yanke = november[-2] + str('yankee')[beta-1] + lima[beta-1]
    zulu = '\u0070\u0071\u0072\u0073\u0074\u0075\u0076\u0077\u0078\u0079\u007a\u007b\u007c\u007d\u007e\u007f'

    flag1=decode(flag[6].upper(), 'rot_13')
    print("test mike", mike)
    print("test zulu", zulu[0])
    print("test flag1", flag1)
    print("test flag1.count zulu", flag1.count(zulu[0]))
    print("test", mike[flag1.count(zulu[0])])
    flag1 += whiskey.split(mike[flag1.count(zulu[0])])[2].join(list(map(lambda coca:coca.upper(),[mike[beta-int(charlie)],str(foxtrot)[flag1.find(quebec)],kilo[1::-1], hotel[november.find(flag1[echo-delta+int(charlie)])]]))[0:4])
    flag1 += zulu[len(flag1)-beta] + romeo
    flag1 += hotel[flag1.count(flag1[int((echo-delta)/2)+int(alpha)])-int(alpha)]
    flag1 += flag1[-1] + 'l'.join(['','',''])
    flag1 += str(foxtrot)[len(flag1):len(flag1)+flag1.count(str(alpha)[-beta])][1::-1]
    flag1 += decode(flag1[int((int(alpha)+beta+int(charlie))*(echo-delta)/2)],'rot_13')
    flag1 += decode(flag1[int(juliet[-1])-flag1.count(flag1[int(juliet[-1])])],'rot_13').upper()
    flag1 += 2*flag1[echo-delta]
    flag1 += zulu[len(flag1)+int(alpha)]

print("You will know when you get it right: " + flag1)