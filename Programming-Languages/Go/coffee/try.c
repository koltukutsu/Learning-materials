#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int times;

char **ft_split(const char *string_arr, char delimeter);

void string_printer(char** string_arr);

int main() {
    char **result;
    char *str;
    char delim;

    str = "huzeyfe semih abussamed abi";
    delim = ' ';
    
    
    result = ft_split(str, delim);
    // string_printer(result);
    printf("1");
    
    return 0;
}

void string_printer(char** string_arr){
    int size;
    int i;

    while (i < times) {
        printf("%s\n", string_arr[i]);
    }
    

}

char **ft_split(const char *string_arr, char delimeter){
    int i;
    int j;
    int k;
    int how_many_times;
    int size;
    char **final_array;
    char *temporary_string;
    char *temp_string_2;
    char temp_char;
    int length_of_string;

    i = 0;
    how_many_times = 1;
    size = strlen(string_arr);
    

    
    while (i < size) {
        if (string_arr[i] == delimeter) 
        {
            how_many_times++;
        }
        i++;
    }
    times = how_many_times;
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
            length_of_string = 0;
            memset(temporary_string, 0, sizeof(temporary_string));
            j++;
        } 
        else 
        {   
            // if (strlen(temporary_string) != 0)
            if (i > 0)
            {
            temp_string_2 = (char *)malloc(length_of_string * sizeof(char));
            strcpy(temp_string_2, temporary_string);
            free(temporary_string);
            }

            length_of_string++;            
            temporary_string = (char *)malloc(length_of_string * sizeof(char));
            temp_char = string_arr[i];
            strcpy(temporary_string, temp_string_2);
            strcat(temporary_string, &temp_char);           
        }

        i++;
    } 

    return final_array;
}