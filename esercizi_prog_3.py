

def palindromo(parola):
    return parola == parola[::-1]

def test_palindromo():
    assert palindromo("poppi") == True, "Test fallito per 'radar'"
    assert palindromo("python") == False, "Test fallito per 'python'"
    assert palindromo("anna") == True, "Test fallito per 'anna'"
    assert palindromo("civic") == True, "Test fallito per 'civic'"
    assert palindromo("abcd") == False, "Test fallito per 'abcd'"
    print("Tutti i test sono stati superati!")

# Esegui il test
test_palindromo()
