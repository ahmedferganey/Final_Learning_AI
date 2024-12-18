#include<iostream> 
#include<cmath>
#include<algorithm>
#include<iomanip>
#include<cstring>


using namespace std;

int main(){

    cout << "i love mariam" << endl;
    cout << abs(-10) << endl;
    cout << max(10, 20) << endl;
    cout << max(max(10,20), 30) << endl;


    // array
    char g[]{"1500"};
    cout << "g as string " << g << endl;
    cout << atoi(g) + 1 << endl ;
    cout << atol(g) + 1 << endl ;
    cout << atoll(g) + 1 << endl ;
    cout << sizeof(atoi(g) +   1)     << endl ;
    cout << sizeof(atol(g) +   1)     << endl ;
    cout << sizeof(atoll(g) +  1)    << endl ;


}