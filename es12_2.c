#include <stdio.h>
#include <stdlib.h>


int* inserimento ( int n){
    int *a=(int*)malloc(n*sizeof(int));

    for (int i =0;i<n;i++){
        printf("inserisci il valore(%d): ",i);
        scanf("%d",(a+i));

    }
    return (a);


}

int lunghezza(){
    printf("inserisci n ");
    int n;
    scanf("%d",&n);
    while(n==0){
        printf("inserisci un valore diverso d 0");
        scanf("%d",&n);
    }
    if(n<0)n=-n;
    return (n);
}

void stampa (int a[], int n){
    for (int i =0;i<n;i++){
        printf("l'elemento alla posizione (%d) è: %d\n", i,*(a+i));
    }
}



int main(){
    int n =lunghezza();
    int *a=inserimento(n);
    stampa(a,n);
}