#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <locale.h>

int main(){
    setlocale(LC_ALL, "turkish");
    char main_text[500] = "Ali ata bak, don git bir daha bak";
    char searched[500];
    int main_text_length, searched_text_length, i, j, control = 0;

    printf("Aramak istediginiz kelimeyi giriniz : ");
    gets(searched);
    printf("\n%s", searched);
    i = 0;
    while(main_text[i] != '\0')
    {
        main_text[i] = tolower(main_text[i]);
        i++;
    }
    main_text_length = i;

    printf("Main text kucuk harflerle : %s", main_text);
}
