class familymember:
    def __init__(self, eyecolor, height):
        self.eyecolor = eyecolor
        self.height = height
    def showtraits(self):
        print("Eye color:", self.eyecolor)
        print("Height:", self.height)
class Kid(familymember):
    def __init__(self,name,age,eyecolor,height):
        self.name = name
        self.age = age
        super().__init__(eyecolor,height)
    def showtraits(self):
        print("name:",self.name)
        print("age:",self.age)
        super().showtraits()
    def favoritehobby(self,hobby):
        print(self.name,"likes","hobby")
child= Kid("John", 10, "blue", 140)

child.showtraits()
child.favoritehobby("football")


    
