#include <stdio.h>
//setlocale(LC_ALL, "turkish");
int fact(int x);
int main(){
    int taken;
    int first, second;
    float result;
    int run = 1;
    
    printf("\n1)toplama\n2)cikarma\n3)carpma\n4)bolme\n5)faktoriyel\nEnter)cikis\n>");
    while(run){
        //scanf("%d", &taken);
        taken = getchar();
        switch(taken){
            case 49:
                printf("input 1 :");
                scanf("%d", &first);
                printf("input 2 :");
                scanf("%d", &second);

                result = first + second;
                printf("%d + %d = %f", first, second, result);
                break;
            case 50:
                printf("input 1 :");
                scanf("%d", &first);
                printf("input 2 :");
                scanf("%d", &second);

                result = first - second;
                printf("%d - %d = %f", first, second, result);
                break;
            case 51:
                printf("input 1 :");
                scanf("%d", &first);
                printf("input 2 :");
                scanf("%d", &second);

                result = first * second;
                printf("%d * %d = %f", first, second, result);
                break;
            case 52:
                printf("input 1 :");
                scanf("%d", &first);
                printf("input 2 :");
                scanf("%d", &second);

                result = first / second;
                printf("%d / %d = %f", first, second, result);
                break;
            case 53:
                printf("input 1 :");
                scanf("%d", &first);

                result = fact(first);
                printf("factorial(%d) = %f", first, result);

                break;
            case 10:
                run = 0;
                break;
            default:
                printf("the input is incompatible, give a new input");
                scanf("%d", &taken);
        }
    }

    return 0;
}

int fact(int x){
    if (x == 1) return 1;
    return x * fact(x - 1);
}
