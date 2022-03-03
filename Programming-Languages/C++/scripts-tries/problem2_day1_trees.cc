#include <iostream>
#include <string>
#include <vector>

void vec_printer(const std::vector<int>* v, int len);
int controller(const int pos, const std::vector<int>* v, int size, int mod);

int main(){
    std::vector<int> vect;
    std::string str; 
    int i = 0;
    int value;
    int n;
    int flag = 0;

    std::cin >> n;
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
    std::cout << "something great" << std::endl;
    // std::cout << "len of the vect" << vect.size() << std::endl;
    
    int v_size = vect.size();
    int left, right;
    i = 1;
    if (vect[0] != vect[v_size - 1]){
        flag++;
    }

    while (i < v_size / 2) {
        left = controller(i, &vect, vect.size(), 1);
        right = controller(v_size - i - 1, &vect, vect.size(), 0);

        if ((n % 2 == 1) && (i == v_size / 2 + 1)){
            flag += controller(i, &vect, vect.size(), 1);
        }
        else if (left == 1 && right == 1) {
            vect[i] = vect[i - 1] + 1;
            vect[v_size - i - 1] = vect[v_size - i] + 1;
            flag++;
            flag++;
        }
        else if (vect[i] != vect[v_size - i]) {
            if (vect[i] < vect[v_size - i]){
                vect[i] = vect[v_size - i];
            }
            else {
                vect[v_size - i] = vect[i];
            }
            flag++;
        }
        i++;
    }
    vec_printer(&vect, v_size);
    std::cout << flag << std::endl;
}

void vec_printer(const std::vector<int>* v, int len){
    std::cout << len << std::endl;
    for (int i = 0; i < len; i++){
        std::cout << v->at(i) << " ";
    }
    std::cout << "\n";
}

int controller(const int pos, const std::vector<int>* v, int size, int mod){
    int i;
    int current_value = v->at(pos);
    if (mod == 1){
       for (i = 0; i < pos; i++)
        {
        // std::cout << "step" << i << " current:"<< current << " vect value: " << v->at(i) << std::endl;
        if (current_value <= v->at(i))
            {
            // std::cout << "interestingly got out" << std::endl;
            // std::cout << current << v->at(i) << std::endl;
            return 1;
            }
        }

      }
    
    else if (mod == 0){
        for (i = size; i > pos; i--)
        {
        // std::cout << "step" << i << " current:"<< current << " vect value: " << v->at(i) << std::endl;
        if ((current_value <= v->at(i)))
            {
            // std::cout << "interestingly got out" << std::endl;
            // std::cout << current << v->at(i) << std::endl;
            return 1;
            }
        }


    }
    return 0;
}
