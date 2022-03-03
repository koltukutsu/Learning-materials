#include <iostream>
#include <string>
#include <vector>
int main(){
    std::vector<int> vect{0, 9, 1};
    std::string::iterator it;
    std::string::iterator it2;
    std::string str;
    std::cin >> str;

    for (it = str.begin(); it != str.end(); it++){
        std::cout << *it << std::endl;
    }

    for (it2 = vect.begin(); it2 != vect.end(); it++){
        std::cout << *it << std::endl;
    }

}