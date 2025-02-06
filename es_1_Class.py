class Errore (Exception):
    pass

class CsvFile:
    def __init__(self, nome):
        try:
            if not isinstance(nome, str):
                raise TypeError('il tipo non è una stringa')
            self.nome = nome
        
        except Exception as e:
            print(f'si è verificata un eccezione: {e}')

    def get_data(self):
        with open(self.nome, 'r') as file:
            data = [row.strip().split(',') for i, row in enumerate(file.readlines()) if i > 0]
            if not data:  # Check if the data is empty
                raise Errore("il file è vuoto")
        return data

# Example usage
try:
    esempio = CsvFile('shampoo_sales.csv')
    lists = esempio.get_data()
    
    for lista in lists:
        lista[1] = float(lista[1])  # Convert the third column to float
    
    for lista in lists:
        print(lista)

except Errore as e:
    print(f"Errore nell'elaborazione del file: {e}")
