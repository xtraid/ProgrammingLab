class Veicolo:
    def __init__(self,modello,marca,anno,speed):
        self.modello=modello
        self.marca=marca
        self.anno=anno
        self.speed=speed
    def __str__(self):
        return 'i dettagli del veicolo sono: modello= {}, marca= {} ,anno del veicolo= {}, velocità attuale= {}'.format(self.modello,self.marca,self.anno,self.speed)
    def accellerare(self):
        self.speed+=5
    def frenare(self):
        self.speed-=5
    def get_speed(self):
        return self.speed
class Veicolo_con_porte(Veicolo):
    def __init__(self,modello,marca,anno,speed,n_porte):
        super().__init__(modello,marca,anno,speed)
        self.n_porte=n_porte
    def __str__(self):
        return 'i dettagli del veicolo sono: modello= {}, marca= {} , il numero di porte è= {}, anno del veicolo= {}, velocità attuale= {}'.format(self.modello,self.marca,self.n_porte,self.anno,self.speed)