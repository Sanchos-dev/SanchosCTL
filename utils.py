import shutil
import subprocess

class installer():
    #I already hate this shit
    #I HATE "self" IT IS SO ANNOYING
    #I need to add SanchosEcosystem packages to this bitch
    def check_package_existence(self, package):
        return shutil.which(package) is not None
    def install(self, package):
        print(f"trying to install: {package}")
        if self.check_package_existence(package) == True:
            print(f"Package {package} already in the system. Aborting.")
        else:
            print("Trying pacman...")
            res = subprocess.run(["sudo", "pacman", "-S", package])
            if res.returncode != 0: #we're sayin "fuck it" and trying AUR
                print(f"no {package} in pacman, trying yay")
                if self.check_package_existence("yay") == True:
                	res1 = subprocess.run(["yay", "-S", f"{package}"])
                	if res1.returncode == 0:
                		print(f"\n\n\n SUCCESFULLY INSTALLED {package} WITH YAY")
                	else:
                		print("sorry I connot install this package")
                else:
                	print("yay not installed in your system")
            else:
            	print(f"\n\n\n SUCCESFULLY INSTALLED {package} WITH PACMAN")

class updater():
	#I need to add SanchosEcosystem packages to this bitch
	def update(self):
		print("updating system...")
		res = subprocess.run(["sudo", "pacman", "-Syu"])
		if res.returncode == 0:
			print(f"\n\n\nUPDATED")
		else:
			print("\n\n\nerror")

class backup():
	def full(self):
		pass
	def partial(self, directory):
		pass
	def restore(self, arc_dir):
		pass


class tui():
    pass