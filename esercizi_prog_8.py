def element (a,b):
    if not isinstance (a, str) or not isinstance (b,str):
        raise TypeError("a o b sono di tipo incompatibile: a risulta {} mentre b risulta {}".format(type(a), type(b)))
    if any(a[i]==b[j] for i in range (len (a))  for j in range (len (b))):
        return True
    return False


def testcase():
    a = 'parole'
    b = 'ettore'
    c = 'gesù'
    d = [1, 5, 4, 8, 6, 5, 6]
    e = 3.5

    # Test 1: String vs String (Expected: True because 'e' appears in both)
    assert element(a, b) == True, "Test 1 Failed"

    # Test 2: String vs String (Expected: True because 'e' appears in both)
    assert element(a, c) == True, "Test 2 Failed"

    # Test 3: String vs List (Expected: TypeError because 'd' is not a string)
    try:
        element(a, d)
    except TypeError as err:
        assert str(err) == "a o b sono di tipo incompatibile: a risulta <class 'str'> mentre b risulta <class 'list'>", f"Test 3 Failed: {err}"

    # Test 4: List vs Number (Expected: TypeError because 'e' is not a string)
    try:
        element(d, e)
    except TypeError as err:
        assert str(err) == "a o b sono di tipo incompatibile: a risulta <class 'list'> mentre b risulta <class 'float'>", f"Test 4 Failed: {err}"

    # Test 5: List vs String (Expected: TypeError because 'd' is not a string)
    try:
        element(d, c)
    except TypeError as err:
        assert str(err) == "a o b sono di tipo incompatibile: a risulta <class 'list'> mentre b risulta <class 'str'>", f"Test 5 Failed: {err}"

    # Test 6: String vs String (Expected: False because no common characters between 'parole' and 'hello')
    assert element('parole', 'bibbi') == False, "Test 6 Failed"

    # Test 7: Empty String vs String (Expected: False because an empty string has no characters)
    assert element('', 'test') == False, "Test 7 Failed"

    # Test 8: String vs Empty String (Expected: False because 'parole' has characters but '' is empty)
    assert element('parole', '') == False, "Test 8 Failed"

    print("All tests passed!")

# Run the test cases
testcase()
