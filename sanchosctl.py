# SanchosCTL base for SanchosOS
# SanchosOS - arch based system
#
#


import os
import sys
import time
import config
from utils import installer as inst
from utils import backup as bak



def clr():
	os.system("clear")

clr()
print("SanchosCTL cli for SanchosOS")



help_page =f"""
SanchosCTL usage: 
  -h or --help : this page
  -i or --install : install some apps, available apps: {config.avail_apps} 
  -u or --update : update system and sanchos ecosystem  
  -i or --id : SanchosID login/register/exit acc 
  -vpn or --sanchosvpn : update SanchosVPN subscription 
  -c or --check : full system check 
  -t or --theme : change theme from  
  -b or --backup : make full system backup 
  -w or -tui : run SanchosCtl in terminal interface mode
"""





if "-h" or "--help" in sys.argv:
	print(help_page)
elif "-i" or "" in sys.argv:
	pass
elif "-u" or "" in sys.argv:
	pass
elif "-vpn" or "" in sys.argv:
	pass
elif "-c" or "" in sys.argv:
	pass
elif "-t" or "" in sys.argv:
	pass
elif "-b" or "" in sys.argv:
	pass
elif "-w" or "-tui" in sys.argv:
	pass





#check flags: if "-h" or "-help" in sys.argv:
