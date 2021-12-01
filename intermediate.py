#!/usr/bin/python
# AUTHOR: Gloriel M. Soto Maldonado

import sys
import time
import digitalocean
import xml.etree.ElementTree as ET
import json

###########################################################################
#
token = "f2f119a305767d634c37bceb7c1cd2e6f8ab22316dbf6cbe7662fb2da3796fa7"
#
###########################################################################
version = "1.0"
c = {"r": "\033[1;31m", "g": "\033[1;32m", "y": "\033[1;33m", "e": "\033[0m"}
manager = digitalocean.Manager(token=token)

ram = "s-1vcpu-1gb"

def get_droplets():
    return manager.get_all_droplets()


def get_token(token):    return getpass.getpass()


def create(token, name, region, os, ram):
    droplet = digitalocean.Droplet(token=token,
                                   name=name,
                                   region=region,
                                   image=os,
                                   size_slug=ram,
                                   backups=False)
    droplet.create()
    print("%s[Droplet]%s '%s' Created." % (c["g"], c["e"], name))


def build():
#    print("build initial")
#    num = int(input("How many droplets do you want to create: "))
    num = 1
    name = input("VPS name (if # of VPS > 1, name will become %name%-01, %name%-02 etc): ")

    for i in manager.get_all_regions():
        print("%s : '%s'" % (i.name.strip(), i.slug.strip()))
    region = input("What region (i.e. nyc1): ")

    for i in manager.get_all_images():
        print("'%s'" % i.slug)
    os = input("What base image (i.e. rockylinux-8-x64): ")

    ram = "s-1vcpu-1gb"

    print(num, name, region, os, ram)
#    for n in range(num - 1):
    droplet = digitalocean.Droplet(token=token,
                                   name=name,
                                   region=region,
                                   image=os,
                                   size_slug=ram,
                                   backups=False)
    response = droplet.create()
    print("Creating a ", ram, "'s VM named ", name, " in ", region, " with ", os, ". Please, wait a minute until creation.")
    time.sleep(5)
    print("[.                                                              ]")
    time.sleep(5)
    print("[...                                                            ]")
    time.sleep(5)
    print("[.....                                                          ]")
    time.sleep(5)
    print("[.......                                                        ]")
    time.sleep(5)
    print("[..........                                                     ]")
    time.sleep(5)
    print("[...............                                                ]")
    time.sleep(5)
    print("[...................                                            ]")
    time.sleep(5)
    print("[............................                                   ]")
    time.sleep(5)
    print("[........................................                       ]")
    time.sleep(5)
    print("[..................................................             ]")
    time.sleep(5)
    print("[............................COMPLETED..........................]")
    time.sleep(5)

#    print("\033[1;32m[+]\033[0m Droplet '%s' created -> IP address '%s'" % (str(name + str("-" + n)), response.ip_address))
    print(name,"'s VM has been created.")
    print(get_droplets())

def create_from_list(drop_dic):
    for num in range(0, drop_dic["amount"]):
        name = drop_dic["name"] + "-" + str(num)
        ram = "s-1vcpu-1gb"
        img = drop_dic["image"]
        region = drop_dic["region"]
#        create(token, name, region, img, ram)

        droplet = digitalocean.Droplet(token=token,
                                       name=name,
                                       region=region,
                                       image=img,
                                       size_slug=ram,
                                       backups=False)

        droplet.create()

def usage():
    print("")
    print("# Run in CMD as: %s [options]" % sys.argv[0])
    print("")
    print("Options: ")
    print("\t-l\t[arg]\t\t-\tList information about '[arg]' -> droplets, region, img")
    print("\t-i\t\t\t\t-\tCreate droplets from interactive menu (Easy)")
    print("\t-rm\t[id]\t\t-\tDelete droplet [id]")
    print("")
    exit(1)
