import os
import subprocess
class tui():
	#i need to make it scalable
	initial_list = ["install package","remove package","update system and sanchos ecosystem packages","SanchosID login, register, or exit account", "Update SanchosVPN subscription", "Perform full system check", "Change system theme", "Create full system backup", "reate partial backup", "Restore files from backup", "Run in user interface mode"]
	

	def sub_handler(self, num, name):
		if num == 0:
			self.clr()
			print("What package do you want to install?")
			pkg_name = input("package name: ")
			try:
				subprocess.run(["sanchosctl", "-i", f"{pkg_name}"])
			except:
				subprocess.run(["python", "sanchosctl.py", "-i", f"{pkg_name}"])
		elif num == 1:
			self.clr()
			print("What package do you want to uninstall?")
			pkg_name = input("package name: ")
			try:
				subprocess.run(["sanchosctl", "-r", f"{pkg_name}"])
			except:
				subprocess.run(["python", "sanchosctl.py", "-r", f"{pkg_name}"])
		elif num == 2:
			subprocess.run(["sanchosctl", "-u"])
		elif num == 3:
			subprocess.run(["sanchosctl", "-id"])
			
			
	def clr(self):
		os.system("clear")
	def start(self):
		self.clr()
		self.draw(self.initial_list)
		sub_num = int(input("option: "))
		sub_name = self.initial_list[sub_num]
		self.sub_handler(sub_num, sub_name)
	def draw(self,contents):
		self.clr()
		print("select option:\n")
		for i in range(len(contents)):
			print(f"{i}: {contents[i]}")
	pass

class gui():
	pass