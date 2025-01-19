def main ():
    quadrati= []
    for n in range (10):
        quadrati.append(n**2)
    quadrati_1=[n**2 for n in range (10)]
    print (quadrati)
    print(quadrati_1)
    


main()
