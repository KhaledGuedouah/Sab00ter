print("Here's where we can code the Classes")

# Definition of the Mother class CARD
class Card():

    def __init__(self,name,function="Nu"):
        self.name=name
        self.function=function
    
    def display_card(self):

        fst=" "*len(self.name)
        snd=self.name
        thd=" "*len(self.name)
        shwd= f"({fst})\n({snd})\n({thd})"
        return shwd

    def __str__(self):
        return f"{self.name} ({self.function}) card "


class PathCard(Card):
    def display_card(self):
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
        return shwd


class ActionCard(Card):
    def display_card(self):
        fst=f" {self.name[0]} "
        snd=f"{self.name}"
        thd=f" {self.name[2]} "
        if self.function == "Nx":
            fst=f"ATT"
            snd=f" {self.name[0]} "
            thd=f"   "
        elif self.function == "N+":
            fst=f"DIF"
            snd=f" {self.name[0]} "
            thd=f"   "
        shwd= f"({fst})\n({snd})\n({thd})"
        return shwd


class GoldCard(Card):

    def __init__(self, name, function="Nu",gain=1):
        Card.__init__(self,name,function)
        self.gain=gain

    def display_card(self):
        fst=f" {self.gain} "
        snd=f"{self.name}"
        thd=f"   "
        shwd= f"({fst})\n({snd})\n({thd})"
        return shwd


class GoalCard(PathCard):
    def __init__(self, name, function="Nu",value='N'):
        PathCard.__init__(self,name,function)
        self.value=value

    def showcard(self):
        fst="   "
        snd=f" {self.value} "
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
        return shwd
        
    def display_card(self):
        fst=f"   "
        snd=f"END"
        thd=f"   "
        shwd= f"({fst})\n({snd})\n({thd})"
        return shwd




'''
carta=PathCard("UDL",'Nx')
print(carta)
carta.display_card()
carta=ActionCard("MAP",'Nu')
print(carta)
carta.display_card()
carta=ActionCard("Lit",'N+')
print(carta)
carta.display_card()
carta=GoldCard("Gld",'Nu',4)
print(carta)
carta.display_card()

carta=GoalCard("ULD",'Nu','N')
print(carta)
dis=carta.display_card()
print(dis)
print(carta.showcard())
'''