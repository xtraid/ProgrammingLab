def count_evry_word(file):
        #my_dict = {}  # Create an empty dictionary
        #my_dict['apple'] = 5  # Add a key-value pair ('apple': 5)
        #print(my_dict)  # Output: {'apple': 5}
    my_dict={}
    for line in file :
        try:
            riga=line.split(',')
            for parola in riga :
                try:
                    str(parola)
                    parola=parola.strip()
                    if parola not in my_dict:
                        my_dict[parola]=1
                    else:
                        my_dict[parola]+=1
                except Exception as e:
                    print( 'si è verificato un errore inaspettato alla parola {}, dettagli sull errore: {}'.format(parola,e))
        except Exception as e :
            print(' si è verificato un errore alla riga {}, dettagli sull errore: {}'.format(line,e))
    return my_dict


def call ():
    try :
        with open('esempio.csv','r') as file:
            #print(count_evry_word(file))
            print(type(file))  # Questo stamperà <class '_io.TextIOWrapper'>

    except Exception as e:
        print('si è verificato un errore del tipo {e} nell apertura del file ')


call()

def testcase():
    a=[]
    b=['giovanni','marco']
    c=['giovanni','giovanni']
    d=1