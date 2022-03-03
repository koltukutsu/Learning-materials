#include <stdio.h>
#include <time.h>
#define MAX 15

void dizi_yaz(int *A, int i);

int main(){
     int i=0;
     int r1, r2, t;
     int A[MAX];
     int c=MAX; // c degeri degiseiblir, artarsa karisma degeri de artar
     for(i=0;i<MAX;i++){
         A[i]=i;
     }
     dizi_yaz(A, MAX);
     //bu bir uniform dagilimdir
     while(c>0){
         r1=rand()%MAX; // iki tane random deger aldim,1
         r2=rand()%MAX; // buda 2. deger aldigim
         t=A[r1];//temporary'e atadim A[ilk random sayi] dan gelen sonucu
         A[r1]=A[r2];
         A[r2]=t;
         c--;
     }// bu yaptigimiz isleme shuffle islemi deniyor, random olarak dagittim suan
     dizi_yaz(A, MAX);
}

void dizi_yaz(int *A, int i){
    int j;
    for(j=0;j<i;j++){
        printf("%d-",A[j]);
    }
    printf("\n");
}