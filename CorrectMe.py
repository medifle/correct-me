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

def cm(flag):
    # print('Correct the variables and the code to get the proper input :)')

    # alpha = True
    beta = 1
    # charlie = '1'
    delta = 47
    echo = 24

    if len(flag) == 12:
        print("entered if block")
        print("t2", b64encode(bytes(flag,'utf-8')))
        # print("t2", encode(str(b64encode(bytes(flag,'utf-8')))[5:3:-1].lower()))
        foxtrot = chr(ord(str(b64encode(bytes(flag,'utf-8')))[6])-echo) + encode(str(b64encode(bytes(flag,'utf-8')))[3].lower(), 'rot_13') + ' ' + encode(str(b64encode(bytes(flag,'utf-8')))[5:3:-1].lower(), 'rot_13') # It is
        # print('foxtrot', foxtrot)
        foxtrot = foxtrot + ' ' + str(b64encode(bytes(flag,'utf-8')))[10] + chr(ord(str(b64encode(bytes(flag,'utf-8')))[10])+1) + chr(ord(str(b64encode(bytes(flag,'utf-8')))[10])+2) + foxtrot[3] + decode(str(b64encode(bytes(flag,'utf-8')))[6], 'rot_13') + foxtrot[0:2].lower() #  definit
        # print('foxtrot', foxtrot)
        # print('test', str(b64encode(bytes(flag,'utf-8'))))
        # print('test', str(b64encode(bytes(flag,'utf-8')))[-2])
        foxtrot = foxtrot + foxtrot[7] + str(b64encode(bytes(flag,'utf-8')))[-2] + 'y' # ely
        # print('foxtrot', foxtrot[-11]) # ` `
        foxtrot = foxtrot + foxtrot[-11] + decode(str(b64encode(bytes(flag,'utf-8')))[0], 'rot_13') + str(b64encode(bytes(flag,'utf-8')))[0] + foxtrot[4] + str(b64encode(bytes(flag,'utf-8')))[4].lower() #  obsf
        # print('foxtrot', foxtrot)
        # print('N', ord(str(b64encode(bytes(flag,'utf-8')))[-5]))
        foxtrot = foxtrot + str(b64encode(bytes(flag,'utf-8')))[-10] + foxtrot[-2] + chr(ord(str(b64encode(bytes(flag,'utf-8')))[-5])+1) + str(b64encode(bytes(flag,'utf-8')))[6] + 'ted in here.' # uscated in here.
        # print("foxtrot", foxtrot)
        foxtrot = bytes(foxtrot, 'utf-8')
        # print("str(b64encode(foxtrot))", str(b64encode(foxtrot)))
        golf = ''.join(['c', str(b64encode(foxtrot))[6], chr(ord(str(b64encode(foxtrot))[21])+1)])
        # print("golf",golf)
        hotel = decode(golf, 'rot_13') # start from p
        # india = int(9/3) * '\u0075'
        juliet = 'less' + '\u0074' + 'hotel'[0] + flag[1] + 'n' + str(3)
        kilo = flag[1] + 2*flag[10]
        lima = golf[0] + flag[2] + flag[9]
        # mike = '\u0077' + hotel[0]
        
        # for letter in juliet:
        #     print(letter)
        
        november = lima[:-1] + hotel[1] + golf[-1] + flag[4:7]
        oscar = chr(ord(str(b64encode(foxtrot))[25])-1)
        # papa = hotel[0]
        quebec = kilo[-1]
        # romeo = str(b64encode(foxtrot))[delta - echo]
        while delta > echo:
            echo += len(juliet)
        # sierra = juliet[int(-(echo-delta)/2)]
        # tango = juliet[delta-echo]
        # uniform = juliet[echo-delta]
        # victor = str(echo + int(juliet[-1]))
        # whiskey = 3*( '\u0077' )
        # xray = '\u0054'
        # yanke = november[-2] + str('yankee')[beta-1] + lima[beta-1]
        # zulu = '\u0070\u0071\u0072\u0073\u0074\u0075\u0076\u0077\u0078\u0079\u007a\u007b\u007c\u007d\u007e\u007f'

        flag1=decode(flag[6].upper(), 'rot_13') # t -> G, GWFLAG{...} first G
        # print("kilo 1::-1", kilo[1::-1]) # flag[10]+flag[1]
        print("flag quebec", flag, quebec) # flag[10]
        print("foxtrot", foxtrot)
        # print("str(foxtrot)", str(foxtrot))
        # print("str(foxtrot)", str(foxtrot)[12:14])
        print("kilo", kilo)
        print("november", november)
        print("hotel", hotel)
        
        flag1 += ''.join(list(map(lambda coca:coca.upper(),['w', str(foxtrot)[flag.find(quebec)], kilo[1::-1], hotel[november.find(flag[5])]]))[0:4])
        # print("flag1", flag1)
        flag1 += '{S' # romeo is always S, corresponding to line26 y
        print("flag[3].count", flag.count(flag[3]))
        flag1 += hotel[flag.count(flag[3]) - 1]
        # print("flag1", flag1)
        flag1 += flag[-1] + 'll'
        flag1 += str(foxtrot)[12 : 12+flag.count('e')][1::-1] # to increase the flag length
        # print("flag1", flag1)
        flag1 += decode(flag[6],'rot_13') # t -> g
        flag1 += decode(flag[3 - flag.count(flag[3])],'rot_13').upper()
        
        flag1 += 2*flag[4]
        flag1 += '}'

        print("You will know when you get it right: " + flag1)

# for e in "abcdefghijklmnoqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890":
#     print("now", e)
#     flag = '0ao' + e + '0nt00000'
#     cm(flag)
# flag = '0a0j00t00000'
cm(flag)