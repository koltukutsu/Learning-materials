#include <stdio.h>
typedef enum {mon, thues, wed, thurs, fri, sat, sun} DAYS;
int main(){
    DAYS first = thurs;
    printf("\n%d", thurs);
    printf("\n%d\n", first);
}
