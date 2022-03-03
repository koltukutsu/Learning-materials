#include <iostream>
#include <vector>
#include <string>

int main(){
  std::vector<int> vect;
  std::string value;
  int cur;
  std::cin >> cur;
  vect.push_back(cur);
  for (int i = 0; i < 3; i++) {
    std::cin >> value;
    cur = std::stoi(value);
    vect.push_back(cur);
  }

  for (int i = 0; i< vect.size(); i++)std::cout << vect[i] << std::endl;
}
