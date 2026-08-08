import shutil
import subprocess
import os

class installer():
    #I already hate this shit
    #I HATE "self" IT IS SO ANNOYING
    #I need to add SanchosEcosystem packages to this bitch
    def check_package_existence(self, package):
        return shutil.which(package) is not None
    def remove(self, package):
        print(f"trying to uninstall: {package}")
        if self.check_package_existence(package) == True:
            print(f"Package {package} in the system. Removing.")
            res = subprocess.run(["sudo", "pacman", "-R", "--noconfirm", package])
            if res.returncode == 0:
                print(f"\n\n\n SUCCESFULLY UNINSTALLED {package} WITH PACMAN")
            else:
                if self.check_package_existence("yay") == True:
                    res1 = subprocess.run(["yay", "-R", "--noconfirm", package])
                    if res1.returncode == 0:
                        print(f"\n\n\n SUCCESFULLY UNINSTALLED {package} WITH YAY")
                    else:
                        print("sorry i cannot uninstall this package")
                else:
                    print("\n\n\nyay not installed in your system")
                    print("installing yay...")
                    res = subprocess.run(["sudo", "pacman", "-Syu", "--noconfirm"])
                    if res.returncode == 0:
                        res = subprocess.run(["sudo", "pacman", "-S", "--noconfirm", "--needed", "base-devel", "git"])
                        if res.returncode == 0:
                            res = subprocess.run(["git", "clone", "https://aur.archlinux.org/yay.git"])
                            if res.returncode == 0:
                                res = subprocess.run(["makepkg", "-si", "--noconfirm"], cwd="yay")
                                if res.returncode == 0:     
                                    shutil.rmtree("yay", ignore_errors=True)           
                                    print("pacman cannot uninstall this package. trying yay.")
                                    res1 = subprocess.run(["yay", "-R", "--noconfirm", package])
                                    if res1.returncode == 0:
                                        print(f"\n\n\n SUCCESFULLY UNINSTALLED {package} WITH YAY")
                                    else:
                                        print("sorry i cannot uninstall this package")
        else:
        	print("There's no such package in the system")

    def install(self, package):
        print(f"trying to install: {package}")
        if self.check_package_existence(package) == True:
            print(f"Package {package} already in the system. Aborting.")
        else:
            print("Trying pacman...")
            res = subprocess.run(["sudo", "pacman", "-S", "--noconfirm", package])
            if res.returncode != 0: #we're sayin "fuck it" and trying AUR
                print(f"no {package} in pacman, trying yay")
                if self.check_package_existence("yay") == True:
                    res1 = subprocess.run(["yay", "-S", "--noconfirm", package])
                    if res1.returncode == 0:
                        print(f"\n\n\n SUCCESFULLY INSTALLED {package} WITH YAY")
                    else:
                        print("sorry I cannot install this package")
                else:
                    print("\n\n\nyay not installed in your system")
                    print("installing yay...")
                    res = subprocess.run(["sudo", "pacman", "-Syu", "--noconfirm"])
                    if res.returncode == 0:
                        res = subprocess.run(["sudo", "pacman", "-S", "--noconfirm", "--needed", "base-devel", "git"])
                        if res.returncode == 0:
                            res = subprocess.run(["git", "clone", "https://aur.archlinux.org/yay.git"])
                            if res.returncode == 0:
                                res = subprocess.run(["makepkg", "-si", "--noconfirm"], cwd="yay")
                                if res.returncode == 0:     
                                    shutil.rmtree("yay", ignore_errors=True)           
                                    if self.check_package_existence("yay") == True:
                                        res1 = subprocess.run(["yay", "-S", "--noconfirm", package])
                                    if res1.returncode == 0:
                                        print(f"\n\n\n SUCCESFULLY INSTALLED {package} WITH YAY")
                                    else:
                                        print("sorry I still cаnnot install this package")
            else:
            	print(f"\n\n\n SUCCESFULLY INSTALLED {package} WITH PACMAN")

class updater():
	#I need to add SanchosEcosystem packages to this bitch
	def update():
		print("updating system...")
		res = subprocess.run(["sudo", "pacman", "-Syu", "--noconfirm"])
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


