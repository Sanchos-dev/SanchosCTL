class tui():
	initial_list = ["","","",""]
    def clr(self):
        os.system("clear")
    def start(self):
        self.clr()
        print("what you want to do? \n")
        self.draw()
        pass
    def draw(self, contents, pointer):
        for i in range(len(contents)):
            print(f"{contents[i]} \n")
    pass

class gui():
    pass