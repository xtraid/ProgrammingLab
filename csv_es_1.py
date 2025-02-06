def conta(parola, file):
    try:    
        str(parola)
    except Exception as e:
         print('devi inserire una stringa, hai inserito {}'.format(type(parola)))
    c = 0
    for riga in file:
        try:
            parole = riga.split(',')  # Split each line into words by commas
            c += parole.count(parola)  # Count occurrences of 'parola' in the list
        except Exception as e :
            print('si è verificato un errore nello split o nel parsing della "{}" riga'.format (riga.strip()))
    return c


try:
    lista = []  # Initialize an empty list
    with open('esempio.csv', 'r') as file:
        for elemento in file:
            lista.append(elemento.strip())  # Add lines to the list, strip newlines
except Exception as e:
    print ('si è verificato un errore: {}'.format(e))

def test():
     # Test Case 1: Simple Test for One Occurrence of the Word
    file_content = ["banana,apple,orange", "grape,apple,pear"]
    parola = "apple"
    assert conta(parola, file_content) == 2, "Test Case 1 Failed"

    # Test Case 2: Word Not Found in File
    parola = "mango"
    file_content = ["banana,apple,orange", "grape,pear,kiwi"]
    assert conta(parola, file_content) == 0, "Test Case 2 Failed"

    # Test Case 3: Word Occurs Multiple Times in the Same Line
    parola = "banana"
    file_content = ["banana,banana,banana", "apple,banana"]
    assert conta(parola, file_content) == 4, "Test Case 3 Failed"

    # Test Case 4: Handling of Empty Lines in the File
    parola = "apple"
    file_content = ["banana,apple,orange", "", "apple,apple"]
    assert conta(parola, file_content) == 3, "Test Case 4 Failed"

    # Test Case 5: Input Validation (Non-String Word)
    parola = 123  # Invalid input
    file_content = ["banana,apple,orange", "grape,pear"]
    assert conta(parola, file_content) == 0, "Test Case 5 Failed"  # Should print validation message and return 0

    # Test Case 6: Empty File (No Data)
    parola = "apple"
    file_content = []
    assert conta(parola, file_content) == 0, "Test Case 6 Failed"
    
    # Test Case 7: Special Characters in the Word
    parola = "hello@world"
    file_content = ["hello@world,apple,banana", "grape,hello@world"]
    assert conta(parola, file_content) == 2, "Test Case 7 Failed"

    print("All test cases passed successfully!")

test() 