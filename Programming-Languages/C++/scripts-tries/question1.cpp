#include <iostream>
 
using namespace std;
 
int main(){
	
	int given;
 
	cin >> given; 
	if ((given >= 0) && (given <= 100) && (given != 2))
	{
		if (given & 0x1) cout << "NO" << endl;	

		else 
		{   
			printf("YES");
		}
	}
	else{
        printf("NO");
    }
	return 0;
	
}
