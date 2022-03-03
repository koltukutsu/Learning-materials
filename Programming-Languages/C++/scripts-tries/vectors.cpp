#include <iostream>
#include <string>

int foo(int x);
void control(int x);
int main(){
    int value;
    int value1 = 0;
    while (value1 != 1){
        std::cin >> value; 
        std::cout << "boolean: " << foo(value) << std::endl;
        std::cout << "if result: "; control(value);
    }
}

int foo(int x){

    if (x == 1) return true;
    else return false;
}

void control(int x){
    if (x) std::cout << "it's alive" << std::endl;
}