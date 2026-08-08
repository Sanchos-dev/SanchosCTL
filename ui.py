import os
class tui():
	#i need to make it scalable
	initial_list = ["install package","remove package","update system and sanchos ecosystem packages","SanchosID login, register, or exit account", "Update SanchosVPN subscription", "Perform full system check", "Change system theme", "Create full system backup", "reate partial backup", "Restore files from backup", "Run in user interface mode"]
	

	def sub_handler(self, num, name):
		if num == "0":
			pass

	def clr(self):
		os.system("clear")
	def start(self):
		self.clr()
		self.draw(self.initial_list)
		submenu_num = int(input("option: "))
		sub_name = initial_list[submenu_num]
		self.sub_handler(sub_num, sub_name)
	def draw(self,contents):
		self.clr()
		print("select option:\n")
		for i in range(len(contents)):
			print(f"{i}: {contents[i]}")
	pass

class gui():
	pass