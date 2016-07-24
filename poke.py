def favorite(pokemon_type="water"):
    if pokemon_type=="fire":
        return "pikachu"
    elif pokemon_type=="water":
        return "squirtel"
print favorite("water")
# def lst(a,b,c,d):
def lst1(*args):   #stored in tuple form
    for i in args:
         print i
def lst(**kwargs):  #stored in dictionary form
     print kwargs.keys()

def lst(**ele):
    for keys,valuess in ele.items():
        print keys,valuess 


print lst1("pikachu","vv","mk","do")
print lst(a="pikachu",b="vv",c="mk",d="do")

