class Reservation :
    
    def __init__ (self,typeChambre:str,withBreakfast:bool,estinterne:bool,nuite:int,nombrePersonne:int,cinClient:str):
        self.CinCmient=cinClient
        self.NombrePersonne =nombrePersonne
        self.Nuite=nuite
        self.TypeChambre=typeChambre
        self.WithBreakfast=withBreakfast
        self.EstInterne=estinterne

    def __str__ (self)->str:
        return str(self.TypeChambre) +"- BF :"+str(self.WithBreakfast)+" - Interne :"+str(self.EstInterne)+"- "+" NUite  "+str(self.Nuite)+" - NP :"+str(self.NombrePersonne)+" - "+self.CinCmient
    
    def CalculerPrix(self):
        if self.TypeChambre=="Simple":
            if self.EstInterne==True:
                prix=300*0.90*self.Nuite
            else:
                prix=300*self.Nuite
        elif self.TypeChambre=="Double":
            if self.EstInterne==True:
                prix=450*0.90*self.Nuite
            else:
                prix=450*self.Nuite
        else:
            if self.EstInterne==True:
                prix=550*0.90*self.Nuite
            else:
                prix=550*self.Nuite
        if self.WithBreakfast==True:
            prix+=40*self.NombrePersonne*self.Nuite
        else:
            prix=prix
        return prix
    
    
    
  
    
client=Reservation("Simple","oui","non",4,1,"Imane")
print(client)
print(client.CalculerPrix())

ListRes=[]