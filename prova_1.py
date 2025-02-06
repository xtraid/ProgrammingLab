class MovingAverage:
    """
    questa classe si occupa di fare la media tra gli elementi di un vettore
    la media viene fatta a step, ogni step fa la media tra i primi n elementi
    con n scelto dall utente"""
    def __init__(self,window):
        #salvataggio lunghezza finestra, controllo che questa sia accettabile
        if type(window)!=int:
            print('errore nel inserimento della finestra, richiesto un intero, è stato dato un {}, si procede con la finestra di lunghezza 2'.format(type(window)))
            window=2
        elif window<=0:
            print('errore, la finestra deve essere un intero positivo, si procede a impostare la finestara a 2')
            window=2
        self.window=window
    def compute (self,vector):
        """
        questa funzione si occupa di fare la media 
        """
        if len(vector)<self.window:
            self.window=len(vector)#pongo che la finestra sia massima se per caso fosse più lunga della lunghezza del vettore
        clean=[x for x in vector if isinstance(x,float) or isinstance(x,int)]# creo un vettore di soli elementi su cui posso fare la media 
        print('ogni elemento non adatto a fare la media verrà ignorato')
        print(clean)
        result=[]
        for i in range(len(clean)-self.window+1):
            window_elements=clean[i:i+self.window]
            print(window_elements)
            result.append(sum(window_elements)/self.window)
        return result

moving_average= MovingAverage('d')
result=moving_average.compute([2,4,8,16])
print(result)

def testcase():
    a=MovingAverage(5)
    b=MovingAverage('a')
    c=MovingAverage(5.8)
    d=MovingAverage([4,'ciao'])
    



