#include <stdio.h>
void sikistirilmis_array_printer_2d(int *p, const int rows, const int cols){
    int i, j, value;
    printf("\nSikistirilmis Matris");
    for(i = 0; i < rows; i++){
        for(j = 0; j < cols; j ++){
            value = *(p + (i * cols) + j);
            if (value != 0){
                printf("\n%d   %d   %d", i, j, value);
            }

        }
    }
}
//void reverser(int *p, int *p_2, const int rows, const int cols){
void reverser(int *p, int dizi[][3], const int nonzeros, const int col_number){

    // 2, yaklasim
    int i, row, col, value;
    printf("\ninside");
    fflush(stdin);
    for(i = 0; i < nonzeros; i++){

        row = dizi[i][0];
        printf("\n-1 :: %d", row);
        col = dizi[i][1];
        printf("\n-2 :: %d", col);
        value = dizi[i][2];
        printf("\n-3 :: %d", value);

        *(p + ((row) * col_number) + (col)) = value;
    }
}

void array_printer_2d(int *p, const int rows, const int cols){

    int i, j, value;

    for(i = 0; i < rows; i++){
        printf("\n");
        for(j = 0; j < cols; j ++){
            value = *(p + (i * cols) + j);
            printf("%d  ", value);
        }
    }
}
int main(){
    int flag = 1;
    int i, j, choice;

    while (flag == 1){
        printf("\n(1) Seyrek Matristen Sikistirilmis Matrise");
        printf("\n(2) Sikistirilmis Matristen Seyrek Matrise");
        printf("\n(3) Cikis\n");
        scanf("%d", &choice);

        if (choice == 1){
            // ilk kisim
            int rows, cols;
            printf("\nMatrisin Boyutlarini Girin (Satir, Sutun): ");
            scanf("%d", &rows);
            scanf("%d", &cols);
            int arr[rows][cols];
            int *p;
            p = arr;

            for (i = 0; i < rows ; i++){
                for (j = 0; j < cols; j++){
                    printf("[%d][%d]: ", i, j);
                    scanf("%d", (p + (i * cols) + j));
                }
            }
            printf("\nrow->%d column->%d", sizeof(arr) / ((sizeof(arr[0])) ), sizeof(arr[0]) / 4);

            sikistirilmis_array_printer_2d(arr, rows, cols);

        }
        else if(choice == 2){
            int items, max_rows = 0, max_cols = 0;
            printf("\nMatriste kac tane sifirdan farkli eleman var(sikistirilmis): ");
            scanf("%d", &items);
            int arr_items[items][3];
            //int *p;
            //p = arr_items;

            for (i = 0; i < items; i++){
                printf("\n%d. Eleman icin Satir, Sutun ve Degeri Girin", i+1);
                scanf("%d",&arr_items[i][0]); // rows
                scanf("%d",&arr_items[i][1]); // cols
                scanf("%d",&arr_items[i][2]);
                if (arr_items[i][0] > max_rows){
                    max_rows = arr_items[i][0];
                }
                if ( arr_items[i][1] > max_cols){
                    max_cols = arr_items[i][1];
                }
            }
            max_rows++;
            max_cols++;

            printf("before assigning values");
            printf("\ninside %d--%d", max_rows, max_cols);
            int new_matrix[max_rows][max_cols];
            for (i = 0; i < max_rows; i++){
                for (j = 0; j < max_cols; j++){
                    new_matrix[i][j] = 0;
                }
            }


            array_printer_2d(new_matrix, max_rows, max_cols);
            printf("\noutside");

            printf("\nSikistirilmis Matrix");
            for (i = 0; i < items; i++){
                printf("\n%d  %d  %d", arr_items[i][0], arr_items[i][1], arr_items[i][2]);
            }
            //

            reverser(new_matrix, &arr_items, items, max_cols);
            printf("\nSeyrek Matris:\n");
            array_printer_2d(new_matrix, max_rows, max_cols);
        }
        else if(choice == 3){
            flag = 0;
        }
    }
}
