def dictionar(A):
    diz={1:'uno',2:'due',3:'tre',4:'quattro',5:'cinque',6:'sei',7:'sette',8:'otto',9:'nove',0:'zero'}
    if not isinstance (A,list):
        raise TypeError ('il tipo richiesto è lista hai dato {}'.format(type(A)))
    if any(x not in diz for x in A):
        raise ValueError ('almeno uno degli elementi nonè una cifra' )
    s = [diz[i] for i in A]
    print (s) 
    return s 





def testcase():
    a=[1,4,2,5,9,4,5,2,1]
    b='pippo'
    c= 3.13
    e=[12,14]


        # Corrected assertions
    try:
        assert dictionar(a) == ['uno', 'quattro', 'due', 'cinque', 'nove', 'quattro', 'cinque', 'due', 'uno'], "Test 1 fallito"
    except Exception as e:
        print(f"Test 1 fallito: {e}")

    try:
        dictionar(b)
    except TypeError:
        print("Test 2 superato: TypeError correttamente sollevato")

    try:
        dictionar(c)
    except TypeError:
        print("Test 3 superato: TypeError correttamente sollevato")

    try:
        dictionar(e)
    except ValueError:
        print("Test 4 superato: ValueError correttamente sollevato")

    print('Tutti i test sono stati completati')

# Running the test cases
testcase()