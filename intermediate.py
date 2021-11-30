#!/usr/bin/python

import sys
import time
import digitalocean
import xml.etree.ElementTree as ET
from ply.cpp import xrange

###########################################################################
#
token = "f2f119a305767d634c37bceb7c1cd2e6f8ab22316dbf6cbe7662fb2da3796fa7"
#
###########################################################################
version = "1.0"
c = {"r": "\033[1;31m", "g": "\033[1;32m", "y": "\033[1;33m", "e": "\033[0m"}
manager = digitalocean.Manager(token=token)


def get_droplets():
    return manager.get_all_droplets()


def get_my_token(token):
    return getpass.getpass()


def create_droplet(token, name, region, os, ram, ssh):
    if len(ssh) < 1:
        ssh = ""

    droplet = digitalocean.Droplet(token=token,
                                   name=name,
                                   region=region,
                                   image=os,
                                   size_slug=ram,
                                   backups=False,
                                   ssh_keys=ssh)

    x = droplet.create()

    print("%s[Droplet]%s '%s' Created." % (c["g"], c["e"], name))


def interactive_build():
    num = int(input("How many droplets do you want to create: "))

    name = input("VPS name (if # of VPS > 1, name will become %name%-01, %name%-02 etc): ")

    for i in manager.get_all_regions():
        print("%s : '%s'" % (i.name.strip(), i.slug.strip()))
    region = input("What region: ")

    for i in manager.get_all_images():
        print("'%s'" % i.slug)
    os = input("What base image: ")

    ram = input("What size RAM (e.g. 4096): ")
    if "mb" in ram or "MB" in ram:
        ram = ram[:2]

    for n in xrange(num - 1):
        x = create_droplet(token, name, region, os, ram)
        print("\033[1;32m[+]\033[0m Droplet '%s' created -> IP address '%s'" % (str(name + str("-" + n)), x.ip_address))


def parse_file(file):
    try:
        f = open(file, "r").close()
    except:
        print("%s[Error]%s Accessing file '%s'" % (c["r"], c["e"], file))
        exit()

    d = {"amount": 1, "name": "newDroplet", "ram": "512", "location": "lon1", "image": "fedora-22-x64", "ssh_key": ""}

    try:
        root = ET.parse(file).getroot()
    except:
        print("%s[Error]%s Invalid XML file '%s', refer to README for schema information." % (c["r"], c["e"], file))
        exit()

    for child in root:
        childd = child.tag.lower()
        if childd == "amount":
            d["amount"] = int(child.text)

        elif childd == "name":
            d["name"] = child.text.lower()

        elif (childd == "ram") and (int(child.text) >= 256):
            d["ram"] = int(child.text)

        elif childd == "location":
            d["location"] = child.text.lower()

        elif childd == "image":
            d["image"] = child.text.lower()

        elif childd == "ssh_key":
            d["ssh_key"] = []
            d["ssh_key"].append(child.text.lower())
        else:
            print("%s[Error]%s Invalid XML Schema, tag '%s' is not a valid identifier, see README." % (
                c["r"], c["e"], childd))
            exit()

    return d


def create_droplets_from_list(drop_dic):
    for num in range(0, drop_dic["amount"]):
        name = drop_dic["name"] + "-" + str(num)
        ram = str(drop_dic["ram"]) + "mb"
        img = drop_dic["image"]
        loc = drop_dic["location"]
        ssh = drop_dic["ssh_key"]
        create_droplet(token, name, loc, img, ram, ssh)


def usage():
    print("\n# python %s [options]" % sys.argv[0])
    print("")
    print("Please Add Your DigitalOcean Token in 'intermediate.py'")
    print("Options: ")
    print("\t-l\t[arg]\t\t-\tList information about '[arg]' -> droplets, loc, img")
    print("\t-f\t[file.xml]\t-\tCreate droplets from XML schema, see README.")
    print("\t-i\t\t\t\t-\tCreate droplets from interactive menu (Easy)")
    print("\t-rm\t[id]\t\t-\tDelete droplet [id]")
    print("")
    exit(1)
