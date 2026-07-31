class installer():
    #I already hate this shit
    #I HATE "self" IT IS SO ANNOYING
    import shutil
    import subprocess
    def check_package_existance(self, package):
        return self.shutil.which(package) is not None

    def install(self, package): #this goes first
        print(f"trying to install: {package}")
        if self.check_package_existance(package) == True:
            print(f"Package {package} already in the system. Aborting.")
        else:
            try:
                print("Trying pacman...")
                self.subprocess.run(["sudo", "pacman", "-S", f"{package}"])
            except Exception as e:
            	print(e)



class backup():
    pass

class tui():
    pass