#include <iostream>
#include <cstring>

using namespace std;

int main(){
    char favCol[] = "blue";
    char key[10];
    
    do
    {
        cout << "give me your favoure color:\t\n" << endl;
        cin >> key;
    } while (strcmp(key, favCol)); // comparison example
    printf("found it!!");
    cout << key << endl << strcat(favCol, key) << endl << key << endl; // concatanating

    char new_str[10];
    strcpy(new_str, key);
    cout << new_str << endl << key << endl;
}