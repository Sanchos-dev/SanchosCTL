class installer():
    #I already hate this shit
    #I HATE "self" IT IS SO ANNOYING
    import shutil
    import subprocess
    def check_package_existence(self, package):
        return self.shutil.which(package) is not None

    def install(self, package):
        print(f"trying to install: {package}")
        if self.check_package_existence(package) == True:
            print(f"Package {package} already in the system. Aborting.")
        else:
            
            print("Trying pacman...")
            res = self.subprocess.run(["sudo", "pacman", "-S", package])
            if res.returncode != 0: #we're sayin "fuck it" and trying AUR
                print(f" no {package} in pacman, trying yay")
                if self.check_package_existence("yay") == True:
                	res1 = self.subprocess.run(["yay", "-S", f"{package}"])
                	if res1.returncode != 0:
                		print(f"\n\n\n SUCCESFULLY INSTALLED {package} WITH YAY")
            else:
            	print(f"\n\n\n SUCCESFULLY INSTALLED {package} WITH PACMAN")








class backup():
    pass

class tui():
    pass