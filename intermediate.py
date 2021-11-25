import string

import lexer
import syntax
from tabulate import tabulate

# def createvm(name: lexer.t_NAME, region: lexer.t_REGION, server: lexer.t_SERVER, os: lexer.t_OS):
# name = input('Please enter the Name')
#
# if name != lexer.t_NAME:
# print('Please enter a valid Name. Run again.')
#   exit()
#
# d = [["NYC1, NYC2*, NYC3", "New York City, United States"],
#     ["AMS2*, AMS3", "Amsterdam, the Netherlands"],
#     ["SFO1*, SFO2*", "San Francisco, United States"],
#    ["SGP1", "Singapore"],
#    ["LON1", "London, United Kingdom"],
#      ["FRA1", "Frankfurt, Germany"],
#         ["TOR1", "Toronto, Canada"],
#         ["BLR1", "Bangalore, India"]]
#
# print("\n" + tabulate(d, headers=['Name', 'Region']))
#
# region = input('\n' + 'Please enter the Name of the Region you want.')
#
#   if region != lexer.t_REGION and tabulate('Name'):
#        print('Please enter a valid Name. Run again.')
#   exit()
#
#   server = input('Please enter the Server')
#
#   if server != lexer.t_SERVER:
#        print('Please enter a valid Server. Run again.')
#   exit()
#
# d = [["69452245", "freebsd-11-x64-zfs", "FreeBSD 11.4 ZFS", "free11z", "z11"],
#    ["69500386", "freebsd-11-x64-ufs", "FreeBSD 11.4 UFS", "free11u", "u11"],
#    ["77558491", "freebsd-12-x64-ufs", "FreeBSD 12.2 UFS", "free12u", "u12"],
#    ["77558552", "freebsd-12-x64-zfs", "FreeBSD 12.2 ZFS", "free12z", "z12"],
#    ["78547182", "rancheros", "RancherOS 1.5.8 x86 image", "ranch1", "r1"],
#    ["84780898", "fedora-34-x64", "Fedora 34 x64", "fedora34", "f34"],
#    ["85722003", "centos-7-x64", "CentOS 7 x64", "centos7", "c7"],
#    ["85779954", "centos-8-x64", "CentOS 8.3 x64", "centos8", "c8"],
#    ["85779974", "debian-9-x64", "Debian 9 x86 image", "debian9", "d9"],
#    ["85780245", "fedora-33-x64", "Fedora 33 x64", "fedora33", "f33"],
#    ["86718194", "debian-10-x64", "Debian 10 Image", "debian10", "d10"],
#    ["89199942", "rockylinux-8-x64", "RockyLinux 8.4 x64", "rocky8", "r8"],
#    ["89246461", "centos-stream-8-x64", "CentOS Stream 8 x64", "centos8s", "s8"],
#    ["92517214", "debian-11-x64", "Debian 11 Image", "debian11", "d11"],
#    ["93524084", "ubuntu-18-04-x64", "Ubuntu 18.04 x86 image", "ubuntu18", "u18"],
#       ["93525508", "ubuntu-20-04-x64", "Ubuntu 20.04 x86", "ubuntu20", "u20"],
#       ["94389391", "ubuntu-21-10-x64", "Ubuntu 21.10 x64", "ubuntu21", "u21"],
#        ["95344509", "fedora-35-x64", "Fedora 35 x64", "fedora35", "f35"]]
#
#   print("\n" + tabulate(d, headers=['id', 'Slug', 'Description', 'option2', 'Unique Name']))
#
#   os = input("\n" + 'Please enter the unique name of the Operating System. The Operating Systems are: ')
#
#  if os != lexer.t_OS and tabulate('Name'):
#       print('Please enter a valid Name.Run again.')
#        exit()

#Created 11/24/21

import lang


def CREATE(name, region, server, os):
    name = lang.LETTERS
    region = lang.LETTERS
    server = lang.LETTERS
    os = lang.LETTERS_DIGITS


def DELETE(iden, tag):
    iden = lang.LETTERS_DIGITS
    tag = lang.LETTERS


def SHOW(iden, tag):
    iden = lang.LETTERS_DIGITS
    tag = lang.LETTERS


if __name__ == '__main__':

    text = input("Please enter your command (Create, Delete, Show) or write stop to end program ")

    if text == 'stop':
        exit()
    elif text == 'create':
        CREATE()
    elif text == 'delete':
        DELETE()
    elif text == 'show':
        SHOW()

    result, error = lang.run('<stdin>', text)

#Network1 = {type : private, ip : 4, region : New York}
#Droplets1 = {PremiumIntel1 : RockyLinux8.4x64 , Basic2 : 
#CentOS8x64, PremiumAMD1 : FreeBSD12.2}
#for i in droplets1:
#Create droplets1(i) in network1
#Status = status + “/n“ + (return)
#Print (status)
