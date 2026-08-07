# SanchosCTL base for SanchosOS
# SanchosOS - arch based system
### TODO ###
# installer: done
# SanchosEcosystem integration : in process
# SanchosOS-base integragion : in process
# 
# 
###

import os
import sys
import time
import config
from utils import installer, backup, tui, ui, updater
inst = installer()
bak = backup()



args = sys.argv[1:]

help_page =f"""
SanchosCTL usage: 
  -h or --help : this page
  -i [pkg_name] or --install [pkg_name] : install app automaticly
  -r [pkg_name] or --remove [pkg_name] : remove app automaticly
  -u or --update : update system and sanchos ecosystem packages 
  -id or --id : SanchosID login/register/exit acc 
  -vpn or --sanchosvpn : update SanchosVPN subscription 
  -c or --check : full system check
  -t or --theme : change theme from
  -fb or --fullbackup : make full system backup
  -b [dir] or --backup [dir] : make partial backup
  -rb [achive] or --restorebackup [achive] : restore files from backup
  -w or -tui : run SanchosCtl in terminal interface mode
  -ui or --ui : run SanchosCtl in ui mode
"""


def clr():
	os.system("clear")
clr()

if "-h" in args or "--help" in args:
	print(help_page)

elif "-i" in args or "--install" in args:
    flag = "-i" if "-i" in args else "--install"
    index = args.index(flag)
    if index + 1 < len(args):
        app = args[index + 1]
        inst.install(app)
    else:
        print("ERROR: idk")

elif "-r" in args or "--remove" in args:
    flag = "-r" if "-r" in args else "--remove"
    index = args.index(flag)
    if index + 1 < len(args):
        app = args[index + 1]
        inst.remove(app)
    else:
        print("ERROR: idk")
        
elif "-u" in args or "--update" in args:
	updater.update()

elif "-id" in args or "--id" in args:
	pass

elif "-vpn" in args or "--sanchosvpn" in args:
	pass

elif "-c" in args or "--check" in args:
	pass

elif "-t" in args or "--theme" in args:
	pass

elif "-b" in args or "--backup" in args:
    flag = "-b" if "-b" in args else "--backup"
    index = args.index(flag)
    if index + 1 < len(args):
        directory = args[index + 1]
        bak.partial(directory)
    else:
        print("ERROR: idk")

elif "-fb" in args or "--fullbackup" in args:
	bak.full()

elif "-rb" in args or "--restorebackup" in args:
    flag = "-rb" if "-rb" in args else "--restorebackup"
    index = args.index(flag)
    if index + 1 < len(args):
        achive = args[index + 1]
        bak.restore(achive)
    else:
        print("ERROR: idk")
elif "-w" in args or "--tui" in args:
	pass

elif "-ui" in args or "--ui" in args:
    pass


###
# Made by Sanchos from sanchos.su
###