print("Here's where we can code the Classes")

# Definition of the Mother class CARD
class Card():

    def __init__(self,name,function="Nu"):
        self.name=name
        self.function=function
    

    def reveal(self):

        snd=self.name
        shwd= f"""
        ({" "*len(self.name)})
        ({snd})
        ({" "*len(self.name)})
        """
        print(shwd)


    def __str__(self):
        return f"{self.name} ({self.function}) card "


class PathCard(Card):


    
    def reveal(self):

        fst="   "
        snd=f" {self.function[1]} "
        thd="   "

        if "U" in self.name:
            fst=" | "
        if "L" in self.name:
            snd="-"+snd[1:]
        if "R" in self.name:
            snd=snd[:1]+"-"
        if "D" in self.name:
            thd=" | "
    
        shwd= f"({fst})\n({snd})\n({thd})"
        print(shwd)




carta=PathCard("UDL",'N+')
print(carta)
carta.reveal()