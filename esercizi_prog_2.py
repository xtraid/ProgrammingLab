



def controllo (lettera, parola):
    count=0
    for item in parola:
        if item== lettera :
            count+=1
    return count


print ("in sussurro ci sono {} s".format(controllo('s','assassino')))