#include <iostream>
#include <string>
/*
This line includes the iostream library, which is part of the C++ 
Standard Library. It provides functionalities for input and output 
streams, allowing you to perform input (from the keyboard) and output 
(to the console).
 */

int function(int x, int y);

int main(){

    std::cout << "Hello, World_1!" << std::endl;
    std::cout << "Hello, World!_2";
    std::cout << "Hello, World!_3" << std::endl;
    std::cout << std::endl;    


    // compile time error 
    //     std::cout << std::endl

    // not runtime error where it not use
    //     7/0;
    // runtime error
    // int x = 7/0; std::cout << x << std::endl;



    int a = function(5,6);
    std::cout << a << std::endl; 

    int x{3};
    /*
        std::cout
        std::cin
        std::cerr
        std::clog
        
    */
   std::string name;
   std::string long_name;
   std::cout << "please write your name:" << std::endl;
   std::cin >> name;
   std::cout << "hello: " << name << std::endl;
   std::cout << "Do you love mariam:" << std::endl;
   std::cin >> long_name;
   std::getline(std::cin, long_name);
   std::cout << long_name << std::endl;
   /*
   std::cerr << "Error message : Something is wrong" << std::endl;
   std::clog << "Log message : Something happened " << std::endl; 
   */
//   std::cerr << "Error message : Something is wrong" << std::endl;
//    std::cout << "Do you love mariam:" << std::endl;
    


    return 0;

}


int function(int x, int y){
    int sum = x + y ;
    return sum;
}
