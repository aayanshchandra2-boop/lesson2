class myClass:
    __privateVar = 27

    def __privateMeth(self):
        print("I'm inside class myClass")

    def hello(self):
        print("private variable value:", myClass._myClass__privateVar)
        self.__privateMeth()


foo = myClass()
foo.hello()
foo._myClass__privateMeth()
