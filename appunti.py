#class class_name:
 #       """docstring"""

        #.. variabili ..
        #.. funzioni ..


class Studente:
    ruolo = "studente units"
    
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
        
    def bonjour(self):
        print(self.ruolo, ":", self.nome, self.cognome)

class A:
    x=0
    y=""
    def __init__(self,n,s):
        self.x=n
        self.y=s
    def __str__(self):
        return'a(x='+str(self.x)+', y='+self.y+')'
myobject=A(12345,"hello")
print(myobject.__str__())
print(str(myobject))
print(myobject)




        
def main():
    nome = "manuel"
    cognome = "magnabosco"
    studente1 = Studente(nome, cognome)
    print(studente1.nome, ",", studente1.cognome)
    studente1.bonjour()  # Call the bonjour method to print the role and name

main()

