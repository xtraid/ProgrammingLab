def factorial (n):
    if not  isinstance (n,int) :
        raise ValueError('voglio un intero, mi hai dato un {}'.format(type(n)))
    if n==0:
        return 1
    return factorial(n-1)*n

  
def test_factorial():
    # Test 1: Verifica che il fattoriale di numeri positivi sia corretto
    assert factorial(5) == 121, "Test 1 fallito"
    assert factorial(4) == 24, "Test 2 fallito"
    assert factorial(3) == 6, "Test 3 fallito"
    assert factorial(2) == 2, "Test 4 fallito"
    assert factorial(1) == 1, "Test 5 fallito"
    
    # Test 2: Verifica che restituisca 1 per il caso base n=0
    assert factorial(0) == 1, "Test 6 fallito"
    
    # Test 3: Verifica che venga sollevato un ValueError per input non interi
    try:
        factorial(3.5)
    except ValueError as e:
        assert str(e) == 'voglio un intero, mi hai dato un <class \'float\'>', "Test 7 fallito"
    else:
        print("Test 7 fallito, non è stato sollevato l'errore.")
        
    try:
        factorial('string')
    except ValueError as e:
        assert str(e) == "voglio un intero, mi hai dato un <class 'str'>", "Test 8 fallito"
    else:
        print("Test 8 fallito, non è stato sollevato l'errore.")
    
    print("Tutti i test sono passati!")
    
# Eseguiamo i test
test_factorial()
