class foo:
    pass  #passes the line

class poke:
    "this class has info of poke"

    def __init__(self, pokename, pokecp, poketype):    #constructor of class, destructors also used in python as no automatic garbage collection
        self.pokename=pokename    #works like this keyword in java
        self.pokecp=pokecp
        self.poketype=poketype
        self.__foo="private variable"

    def displayInfo(self):
        print self.__foo  # double underscore is for private members
        print"my pokemon is %s, with cp %s, and type is %s"%(self.pokename,
            self.pokecp,
            self.poketype)


if __name__=="__main__":
    pikachu=poke("pikachu",'100','electricity')  #instance of the class poke
    print pikachu.pokename
    pikachu.displayInfo()
