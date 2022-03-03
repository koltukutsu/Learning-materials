#include <iostream>
#include <string>
#include <vector>

void vec_printer(const std::vector<int>* v, int len);
int main(){
    std::vector<int> vect;
    std::string str;
    int value;
    int flag = 0;
    int i = 0;
    int n;

    std::cin >> n;
    str.reserve(n);
    std::cin.ignore();
    std::getline(std::cin, str);

    // std::cout << str.size() << std::endl;
    int pos = 0, length;
    // splitting in cpp!
    while(i < str.size())
    {
        if ((str[i] == 32)|| (i == str.size() - 1)){
            if (i == str.size() - 1) {
                length++;
            }
            value = std::stoi(str.substr(pos, length));
            vect.push_back(value);
            pos = i + 1;
            length = 0;
        }
        else{
            length++;
        }
        i++;
    }

    int v_size = vect.size();

    if (vect[0] != vect[v_size - 1]){
      //printf("first\n");
      flag++;
      if (vect[0] < vect[v_size - 1]) {
       vect[v_size - 1] = (vect[0] == 0) ? 1 : vect[0];
      }
      else {
       vect[0] = vect[v_size - 1];
         }
      }

     for (i = 1; i < v_size / 2; i++) {
       if (vect[i] != vect[i - 1] + 1) {
       //printf("second-1\n");
         flag++;
         vect[i] = vect[i - 1] + 1;
       }

       if (vect[v_size - i - 1] != vect[v_size - i] + 1) {
         //std::cout<< "i: " <<i << std::endl;
         //printf("second-2\n");
        flag++;
        //std::cout << vect[v_size - 1 - i] << std::endl;
        vect[v_size - i - 1] = vect[v_size - i] + 1;
        //std::cout << "degisen deger: " <<vect[v_size - i - 1] << std::endl;
        //std::cout << vect[v_size - 1 - i] << std::endl;
        }
      //vec_printer(&vect, vect.size());
     }

     if ((n % 2 == 1) && (vect[v_size / 2] != vect[v_size / 2 - 1] + 1)) {
        //printf("final\n");
      flag++;
     }
    std::cout << flag << std::endl;
}

void vec_printer(const std::vector<int>* v, int len){
    //std::cout << len << std::endl;
    for (int i = 0; i < len; i++){
        std::cout << v->at(i) << " ";
    }
    std::cout << "\n";
}
