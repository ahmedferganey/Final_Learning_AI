#include <iostream>

// variables and data types
/*
c++ core lang
standard library
STL
*/

int main(){
    bool y = true;
    int num1 = 15;    
    int num2 = 0b0101;
    int num3 = 0x15;
    int num4 = 015;
    std::cout << "number1 : " << num1 << std::endl;
    std::cout << "number2 : " << num2 << std::endl;
    std::cout << "number3 : " << num3 << std::endl;
    std::cout << "number4 : " << num4 << std::endl; 

    int a{5};            // Direct list initialization
    double b{3.14};      // Direct list initialization
    double k{ a +b};// initializa with expression
    int arr[3]{1, 2, 3}; // Direct list initialization of arrays
    int l{}; // initialize with zero
    int m;   // initialize with zgarbage

    std::cout << "a: " << a << "\n";
    std::cout << "b: " << b << "\n";
    std::cout << "arr: " << arr[0] << ", " << arr[1] << ", " << arr[2] << "\n";
           
    int c(5);            // Functional initialization
    double d(3.14);      // Functional initialization
    int arr2[3] = {1, 2, 3}; // Functional initialization of arrays
    
    std::cout << "c: " << c << "\n";
    std::cout << "d: " << d << "\n";
    std::cout << "arr2: " << arr2[0] << ", " << arr2[1] << ", " << arr2[2] << "\n";

    int e = 5;           // Assignment initialization
    double f = 3.14;     // Assignment initialization
    int arr3[3] = {1, 2, 3}; // Assignment initialization of arrays
    
    std::cout << "e: " << e << "\n";
    std::cout << "f: " << f << "\n";
    std::cout << "arr3: " << arr3[0] << ", " << arr3[1] << ", " << arr3[2] << "\n";
        

    std::cout << sizeof(arr3) << "\n";
    std::cout << "l: " << l << "\n";
    std::cout << "m: " << m << "\n";
    std::cout << "k: " << k << "\n";

    // narrowing conversion
    // int narrow{3.14};      
    // std::cout << "narrow: " << narrow << "\n";

    // integer modifier
    // unsigned int positive{-1}; // compilier error
    

}
