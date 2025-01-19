#include <stdio.h>

struct elemento{

    //valore memorizzato
    int info;
    //puntatore al prossimo elemento della lista 
    struct elemento* next;
};

typedef struct elemento Elementodilista;
typedef Elementodilista* listadielementi;


int main (){

Elementodilista elem;
// per accedere aal campo della lista: none_struct.nome_campo
elem.info=10;
elem.next=NULL; // null== non inizializzato

//ma sta roba fa schifo perchè è statica
// famola nello heep 

listadielementi lista;
// allocazione di namica
lista=(Elementodilista*)malloc(sizeof(Elementodilista));
// accesso allo heep con deferenziazione
(*lista).info=10;
(*lista).next=NULL;








    return (0);
}

