#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char **ft_split(const char *string_arr, char delimeter){
    int i;
    int j;
    int k;
    int how_many_times;
    int size;
    char **final_array;
    char temporary_string[255];
    int length_of_string;

    i = 0;
    how_many_times = 1;
    size = strlen(string_arr);
    strcpy(temporary_string, "");
    

    
    while (i < size) {
        if (string_arr[i] == delimeter) 
        {
            how_many_times++;
        }
        i++;
    }

    final_array = (char **)malloc(how_many_times * sizeof(char*));
   
    if (final_array == NULL){
        printf("Error");
        return final_array;
    }
    
    i = 0;
    j = 0;
    length_of_string = 0;
    while (i < size) {
        if ((string_arr[i] == delimeter) || (i == size - 1))
        {
            final_array[j] = (char *)malloc(length_of_string * sizeof(char));
            strcpy(final_array[j], temporary_string);
            // k = 0;
            // while (k < i) {
            //     final_array[j][k] = string_arr[k];  
            // }
            length_of_string = 0;
            memset(temporary_string, 0, sizeof(temporary_string));
            j++;
        } 
        else 
        {   
            length_of_string++;
            strcat(temporary_string, &string_arr[i]);           
        }

        i++;
    } 

    return final_array;
}

int main() {
    char *str = "huzeyfe semih mehmet";
    char delim = ' ';
    printf("1233");
    ft_split(str, delim);
    printf("123");
    return 0;
}