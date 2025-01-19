#include <stdio.h>
#include <stdlib.h>
 
struct oggetto{
 int elemento;
 struct oggetto* next;
 
};

typedef struct oggetto elemento_list;
typedef struct oggetto* puntatore_list;

void add_term (puntatore_list* l, int x ){
    puntatore_list new = malloc(sizeof(elemento_list));
    (*new).elemento=x;
    new->next=*l;
    *l=new;

    
}

void add_coda (puntatore_list *l, int x){
    puntatore_list new = malloc(sizeof(elemento_list));
    new->elemento=x;
    new->next= NULL;
    if(*l==NULL) 
        *l=new;
    else{
        puntatore_list corr =*l;
        while (corr->next!=NULL){
            corr = corr->next;

        }
        corr->next=new;
    }



}

int main (){

puntatore_list new_list=malloc(sizeof(elemento_list));
puntatore_list coda= new_list;
(*new_list).elemento= 1;
int n =20;
for (int i = 2; i<=n;i++){
    (*new_list).next=malloc(sizeof(elemento_list));
    new_list=(*new_list).next;
    (*new_list).elemento=i;
    
}
(*new_list).next=NULL;

//stampiamo sta merda 
puntatore_list app = coda;
int i = 0;

add_term(&app,10);
do {
    i++;
    
    printf("l'elemento (%d) è: %d\n",i,(*app).elemento);
    app=(*app).next;
}while((app)!=NULL);


while(coda!=NULL){
    app= coda->next;
    free (coda);
    coda= app;
}


}





