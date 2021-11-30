# AUTHOR: Gloriel M. Soto Maldonado

import sys

from ply import yacc
import lexer
import syntax
import intermediate

if __name__ == "__main__":

    lexer.lex
    syntax.yacc

    if intermediate.token == "":
        print(
            "%s[Error]%s Please first set your DigitalOcean token in 'intermediate.py." % (
                intermediate.c["r"], intermediate.c["e"]))
        exit()

    if "-rm" in sys.argv:

        id = int(sys.argv[sys.argv.index("-rm") + 1])

        d = intermediate.get_droplets()

        try:
            name = d[id].name
        except:
            print(
                "%s[Error]%s Droplet ID out of range, do 'python %s -l droplets' to see how many droplets you have." % (
                    intermediate.c["r"], intermediate.c["e"], sys.argv[0]))
            exit()

            ch = input(
                "%s[Confirm]%s Are you sure you want to delete droplet '%s' [Y/N]: " % (
                    intermediate.c["r"], intermediate.c["e"], name))

            if "y" in ch or "Y" in ch:

                try:
                    d[id].destroy()
                except:
                    print("%s[Error]%s DataReadError from DigitalOcean, retry again later" % (
                        intermediate.c["r"], intermediate.c["e"]))
                    exit(1)
                    print("%s[Done]%s Droplet '%s' destroyed." % (intermediate.c["g"], intermediate.c["e"], name))
            exit()

    elif "-l" in sys.argv:
        option = sys.argv[sys.argv.index("-l") + 1]

        if option.lower() == "img":
            print("%s[Option]%s All valid base images." % (intermediate.c["y"], intermediate.c["e"]))
            im = intermediate.manager.get_distro_images()

            for i in im:
                print("%s[Image]%s %s -> '%s'" % (
                    intermediate.c["g"], intermediate.c["e"], str(i.distribution + " " + i.name), i.slug))
            exit()

        elif option.lower() == "loc":
            print("%s[Option]%s All regions." % (intermediate.c["y"], intermediate.c["e"]))
            r = intermediate.manager.get_all_regions()
            for i in r:
                print("%s[Region]%s %s -> '%s'" % (intermediate.c["g"], intermediate.c["e"], i.name, i.slug))
            exit()

        elif option.lower() == "droplets":
            print("%s[Option]%s All your Droplets." % (intermediate.c["y"], intermediate.c["e"]))
            d = intermediate.get_droplets()
            count = 0
            for i in d:
                print("%s[Droplet id: '%d']%s '%s' -> '%s'" % (
                    intermediate.c["g"], count, intermediate.c["e"], i.name, i.ip_address))
                count += 1
            exit()

        else:
            print("%s[Error]%s Option '%s' not recognised, see '%s --help'" % (
                intermediate.c["r"], intermediate.c["e"], option, sys.argv[0]))
            exit()


    elif "-i" in sys.argv:
        intermediate.build()
        exit()

    elif "-f" in sys.argv:
        lista = intermediate.parse_file(sys.argv[sys.argv.index("-f") + 1])
        intermediate.create_from_list(lista)
        exit()
    else:
        intermediate.usage()
