#include <stdio.h>

void array_printer_2d(int *p, const int rows, const int cols){
    int i, j, value;
    for(i = 0; i < rows; i++){
        for(j = 0; j < cols; j ++){
            value = *(p + (i * cols) + j);
            printf("\ndizi[%d][%d]: %d", i, j, value);
        }
    }
}

void array_printer_1d(int *p, const int cols){
    int i, j, value;
    for (i = 0; i < cols; i++){
        value = *(p + i);
        printf("\ndizi[%d]: %d", i, value);

    }
}
int main(){

    int arr[5][3] = {{10,20,30},{11,22,33},{32,12,32},{15,13,16},{123,123,654}};

    array_printer_2d(arr, 5,3);
    printf("\n%d",sizeof(arr)/4);
    printf("\n%d",arr[4][2]);
}
