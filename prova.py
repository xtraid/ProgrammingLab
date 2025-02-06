# Dati da scrivere nel file
csv_data = [
    "nome,età,città",
    "Alice,30,Roma",
    "Bob,25,Milano"
]

# Apri (e crea) il file in modalità scrittura ('w')
with open('pippo.csv', 'w') as file:
    # Scrivi ogni riga nel file
    for row in csv_data:
        file.write(row + '\n')  # Aggiungi una nuova linea dopo ogni riga
