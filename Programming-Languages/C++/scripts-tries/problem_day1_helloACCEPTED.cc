#include <iostream>
#include <string>

int main(){
    std::string s;
    char _find[] = {'h','e','l','l','o'};
    char control_char;
    int limit = sizeof(_find);
    int control_last, first_found;
    int flag = 0;
    int i = 0;

    std::cin >> s;
    // Compare it with the size of wanted characters
    while (i < limit){
        control_char = _find[i];
        
        // std::cout << "\nstep: " << i << std::endl;
        // std::cout << "string: " << s << std::endl; 
        // std::cout << "contrl: " <<control_char << std::endl;
        // std::cout << "first_find: " <<s.find(control_char) << std::endl;
        
        
        // while the wanted is present, go to inner loop
        first_found = s.find(control_char);
        if (first_found != -1){
            /*
            now that we found the wanted character, if present any
            set the substring to s
            */ 
            s = s.substr(s.find(control_char) + 1);
            control_last = s.find_last_of(control_char);
            if ((control_last != s.find(control_char)) && (s.find(_find[i + 1]) > control_last)){
                if (control_char == _find[i + 1]){
                    i++;
                }
                
                while (s.find(control_char) !=  -1){
                s = s.substr(s.find(control_char) + 1);
                }
            }

            
        }
        /* 
        whenever the wanted is not found, end the loop 
        and set flag to 1 which means that 
        the string does not have our wanted characters
        */
        else if (s.find(control_char == -1)){
            flag = 1;
            i == limit;
        }

        else{
            s = s.substr(first_found + 1);
        }
        i++;
        // std::cout << "flag: " << flag << std::endl;
        // std::cout << "fina_string: " << s << std::endl;
    }

    if (flag == 1) std::cout << "NO" << std::endl;
    else std::cout << "YES" << std::endl;
}