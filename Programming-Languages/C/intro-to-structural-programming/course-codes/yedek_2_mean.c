#include <stdio.h>
#include <time.h>
#define MAX 52
#define limit 1356
void dizi_yaz(int *A, int i);

int main(){
    double ortalama=0;
    int k = 0;
    int i, j,r;
    int c;
    int A[MAX];
    int B[MAX];
    while (k < limit){
        i=0;
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
            }
        k++;
        // dizi_yaz(A, MAX);
        // printf("%d kere denedik",c);
        ortalama += c;
    }
    dizi_yaz(A, MAX);
    int son = limit;

    printf("%d kereden gelen ortalama budur %f", son, 1.0*ortalama/limit);
}
void dizi_yaz(int A[MAX], int i){
    int j;
    for(j=0;j<i;j++){
        printf("%d-",A[j]);
    }
    printf("\n");
}