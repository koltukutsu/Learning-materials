#include <stdio.h>
#include <time.h>
#define MAX 52

void dizi_yaz(int *A, int i);

int main(){
    int i=0, j=0,r;
    int c=0;
    int A[MAX]={0};
    int B[MAX] = {0};
    srand(time(NULL));
    while (i<MAX){
        r=rand()%MAX;
        j=0;
        c++;
        if (B[r]==0){
            B[r]=1;///buradaki mantik hashing mantigi
            A[i]=r;
            i++;
        }/*else{
            printf("%d daha once uretilmis\n",r);
        }*/
        if(((i*1.0)>=MAX*0.95)){ //buyuk esittir oldugu duruma baktim cunku esit olmayabilir, nede olsa float mukeyesesi
            printf("\n dizinin yuzde 95i %d. denemede doldu",c);
        }
    }
    printf("\n");
    dizi_yaz(A, i);
    printf("\n%d kere denedik",c);
}

void dizi_yaz(int *A, int i){
    int j;
    for(j=0;j<i;j++){
        printf("%d-",A[j]);
    }
    printf("\n");
}