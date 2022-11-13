print("Here's where we can code the Classes")

# Definition of the Mother class CARD
class Card():

    def __init__(self,name,function="Nu"):
        self.name=name
        self.function=function
    

    def reveal(self):
        a= f"""
        ({" "*len(self.name)})
        ({self.name})
        ({" "*len(self.name)})
        """
        print(a)


    def __str__(self):
        return f"{self.name} ({self.function}) card "


#carta=Card("SAB")
#print(carta)
#carta.reveal()