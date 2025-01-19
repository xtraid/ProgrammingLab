#include <stdio.h>
#include <stdlib.h>

struct obj {
    int num;
    struct obj* next;
};

typedef struct obj lista;
typedef lista* start;

void stampe (start list){
    if (list!=NULL){

        printf("elemento della lista è %d\n",(*list).num);
        stampe(list->next);
    }
   

}

int main(){

 int n = 10;
start new= malloc(sizeof(lista));
(*new).num=1;
start s = new;
for(int i =2;i<n;i++){
    (*new).next=malloc(sizeof(lista));// (*nome_puntatore).nome_attrubuto== nome_puntatore->nome_attributo
    new=(*new).next;// sopost il puntatore in testa
    (*new).num =i; // assegno il valore



}

(*new).next= NULL;
printf("stampe ricorsive: \n");
stampe(s);
 new = s;  // Riporta il puntatore all'inizio della lista
    while (new != NULL) {
        printf("%d -> ", new->num);
        new = new->next;
    }
    printf("NULL\n");

// faciamo una bella stampa 

}