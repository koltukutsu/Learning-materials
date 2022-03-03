#include <stdio.h>
//*((dizi+a*columns) + b)

void sikistirilmis(int *dizi, int rows, int columns){
        int a, b, value;
        for(a = 0; a < rows; a++){
            for(b = 0; b < columns; b++){
                value = *((dizi+a*columns) + b);
                if (value != 0){
                    printf("\n%d", a);
                    printf(" %d",b);
                    printf(" %d",value);
                }
            }
        }
    }


void terse_sikistirilmis(int dizi_degisecek[][3], int *dizim, int m_rows, int m_columns, int nonzeros){
    int a, b;
    int first, second, third;


    for(a = 0; a < nonzeros; a++){
            first = dizi_degisecek[a][1];
            second = dizi_degisecek[a][2];
            third = dizi_degisecek[a][3];
            }
    
}



int main(){//ilk kisim
    int i,j,nonzero;
    int tercih;
    int flag = 1;
    int row, column;
    
    int max_row = 0, max_column = 0;
    
    // printf("seciniz:");
    // scanf("%d", &tercih);
    // printf("\n%d sectiniz", tercih);


    while(flag == 1){

        printf("\ngiris%d",flag);

        printf("\nMenu:");
        printf("\n(1) seyrek matristen sikistirilmis matrise");
        printf("\n(2) sikistirilmis matristen seyrek matrise");
        printf("\n(3) cikis\n");
        scanf("%d", &tercih);
        printf("%d",tercih);
        if (tercih == 1){
            printf("\nMatris boyutlarini girin (satir, sutun):");
            scanf("%d", &row);
            scanf("%d", &column);
            printf("%d %d",row,column);

            int A[row][column];

            for(i = 0; i < row; i++){

                for(j = 0; j < column; j++){
                    printf("\n[%d][%d]:",i,j);
                    scanf(" %d", &A[i][j]);
                }
            }
            sikistirilmis(A, row, column);
        }

        else if(tercih == 2){
            printf("2 ye girdin");
            printf("\nMatriste Kac tane sifirdan farkli eleman var?\n");
            scanf(" %d", &nonzero);
            int B[nonzero][3];
            for (i = 0;i < nonzero; i++){
                printf("%d. Eleman icin Satir, sutun ve degeri girin\n", i+1);
                scanf("%d", &B[i][1]);
                scanf("%d", &B[i][2]);
                scanf("%d", &B[i][3]);
                
                

                if (B[i][1] > max_column){
                    max_column = B[i][1];
                }
                if (B[i][2] > max_row){
                    max_row = B[i][2];
                }
            }
            int degisecek_dizi[max_row][max_column];
            for(i = 0; i<max_row;i++){

                for(j = 0; j<-max_column;j++){
                    degisecek_dizi[i][j] = 0;
                }
            }
            terse_sikistirilmis(B,degisecek_dizi, max_row, max_column, nonzero);

        }

        else if(tercih == 3){
            
            flag == 0;

        }
        else{
            printf("1 2 3 den baska bir sey girdin");
        }
    }



}// son kisim
