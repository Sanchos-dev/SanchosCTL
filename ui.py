import os
class tui():
    initial_list = ["g1","g2","g3","g4"]
    def clr(self):
        os.system("clear")
    def start(self):
        self.clr()
        print("what you want to do? \n")
        self.draw(self.initial_list, 2)
        pass
    def draw(self,contents, pointer):
        for i in range(len(contents)):
            print(f"{contents[i]} \n")
    pass

class gui():
    pass