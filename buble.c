#include <stdio.h>
#include <stdlib.h>

int* buble(int a[], int n){
    int controllo=0;
    int    i =0;
    do{
        controllo=0;
            for (int j =i;j<n;j++){
                if(a[j]>a[j+1]){
                    controllo=1;
                    int app = a[j];
                    a[j]=a[j+1];
                    a[j+1]=app;
                }
            }
    }while(controllo==1);


}