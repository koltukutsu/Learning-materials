#include "stdio.h"

void deneme(int *p, int row, int column);
void inserter(int *p, int row ,int column);
void printer(int *p, int row, int column);
int main(){

    int i, j, flag = 1;
    printf("row and column");
    scanf("%d",row);
    scanf("%d",column);
    printf("(%d, %d)", row, column);
    int dizi[row][column];
    inserter(dizi, row, column);
    //gives the values for control
    //deneme(dizi, 0, 2);
    //deneme(dizi, 1, 1)

}

deneme(int *p, int row, int column){
    printf("[%d][%d].deger: %d ", row, column, *p);

}
inserter(int *p, int row, int column){
    int i, j;
    for (i = 0; i < row; i++){
        for (j = 0; j < column; j++){
            printf("[%d][%d]",i,j);
            scanf("%d", p);
        }
    }
}
void printer(int *p, int row, int column){

}


