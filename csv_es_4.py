class csv_handler :
    def __init__(self,nome):
        self.nome=nome
    
    def readit(self):
        try:
            list=[]
            with open(self.nome,'r') as file:
                contenuto=file.readlines()
                return contenuto
        except Exception as e :
            print('si è verificato lerrore ì'.format(e))



    def clean (self):
        file_1 = []
        for row in self.readit() :
            try:
                
                if row in file_1:
                    continue
                else :
                    file_1.append(row)
            except ValueError:
                print('errore nel valore, si procede a saltare la riga')
                continue
        with open('es_1.csv','w') as new:
            for elemento in file_1:
                new.write(elemento + "\n")
   

es = csv_handler('esempio.csv')

es.clean()