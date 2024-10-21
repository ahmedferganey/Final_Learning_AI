#include <iostream>




int main(){
    bool right {true};
    bool wrong{false};
    if(right){
        std::cout << "right: " << right <<std::endl;
    }

    if(!wrong){
        std::cout << "wrong: " << wrong <<std::endl;
    }

    std::cout << "size of bool " << sizeof(bool) <<std::endl;


    // character

    char a{'a'};

    std::cout << "a: " << a <<std::endl;

    char value = 65;
    std::cout << "value " << value <<std::endl;
    std::cout << "value(int) " << static_cast<int>(value) <<std::endl;

    // auto
    auto var1{1};
    auto var2{13.0};
    /*
The literal 13.0 is a double by default in C++. Therefore, var2 is deduced 
to be of type double.    
    */
    auto var3{14.0f};
    /*
The literal 14.0f explicitly specifies a float type (using the f suffix).   
    */    
    auto var4{12.0l};
    auto var5{'e'};
    std::cout << "var1 " << var1 <<std::endl;
    std::cout << "var2 " << var2 <<std::endl;
    std::cout << "var3 " << var3 <<std::endl;
    std::cout << "var4 " << var4 <<std::endl;
    std::cout << "var5 " << var5 <<std::endl;

    std::cout << "size of var1 " << sizeof(var1) <<std::endl;
    std::cout << "size of var2 " << sizeof(var2) <<std::endl;
    std::cout << "size of var3 " << sizeof(var3) <<std::endl;
    std::cout << "size of var4 " << sizeof(var4) <<std::endl;
    std::cout << "size of var5 " << sizeof(var5) <<std::endl;


    auto var8{1ul};




    // Assignments be carfull when use auto and assignments 
    auto var7{123};
    var7 = 12;

    auto vara{123u};
    vara = -12; //!!! Danger   Logical error
    std::cout << "vara " << vara <<std::endl;




    // variabbles and adta types
        // tricky in c++
    int varb{123};
    int varbc{varb/2};
    std::cout << "vara " << varb <<std::endl;
    std::cout << "varbc " << varbc <<std::endl;


    // precedence and associativity
    int ll {6};
    int b {3};
    int c {8};
    int d {9};
    int e {3};
    int f {2};
    int result =ll/b*c +d - e + f;  //   16 + 9 - 3 + 2
    std::cout << "result : " << result << std::endl;


	int value11 {5};
    
    //Increment by one
    value11 = value11 + 1; //6
    std::cout << "The value is : " << value11 << std::endl; // 6
    
    value11 = 5; // Reset value to 5
    
    //Decrement by one
    value11 = value11 - 1; // 4
    std::cout << "The value is : " << value11 << std::endl; //4    
    std::cout << "The value is (incrementing) : " << value11++ << std::endl; // 5
    std::cout << "The value is : " << value11 << std::endl; // 6
    std::cout << "++he value is (incrementing) : " << ++value11 << std::endl; // 5
    std::cout << "The value is : " << value11 << std::endl; // 6

    value11 +=5;
    //value +=5; // equivalent to value = value + 5
    std::cout << "The value is (after +=5) : " << value11 << std::endl; // 50
    value11 /= 3;
    std::cout << "The value is (after /=3) : " << value11 << std::endl; // 30
    value11 %= 2;
    std::cout << "The value is (after %=11) : " << value11 << std::endl;// 8

////////////////////////////////////////////////////////////////////////
            // relational operators
    int number1 {20};
    int number2 {20};
    std::cout << "number1 : " << number1 << std::endl;
    std::cout << "number2 : " << number2 << std::endl;
	
	std::cout << std::endl;
	std::cout << "Comparing variables" << std::endl;
    std::cout << std::boolalpha ; // Make bool show up as true/false instead of 1/0
    std::cout << "number1 < number2 : " << (number1 < number2) << std::endl;
	std::cout << "number1 <= number2 : " << (number1 <= number2) << std::endl;
    std::cout << "number1 > number2 : " << (number1 > number2) << std::endl;
    std::cout << "number1 >= number2 : " << (number1 >= number2) << std::endl;
    std::cout << "number1 == number2 : " << (number1 == number2) << std::endl;
    std::cout << "number1 != number2 : " << (number1 != number2) << std::endl;


    bool result123 = (number1 == number2);
    std::cout << number1 << " == " << number2 << " : " << result123 << std::endl;
	    
////////////////////////////////////////////////////////////////////////
            // logical operators
    
    bool ss {true};
    bool dd {false};
    bool aa {true};
	

	std::cout << std::boolalpha; // true / false
	std::cout << "ss : " << ss << std::endl;
	std::cout << "dd : " << dd << std::endl;
	std::cout << "aa : " << aa << std::endl;


    	std::cout << std::endl;
	std::cout << "Basic OR operations" << std::endl;
    std::cout << " ss || dd : " <<    (ss|| dd) << std::endl;
    std::cout << " ss || dd : " <<    (ss|| dd ) << std::endl;
    std::cout << " ss ||dd || aa:" << (ss || dd || aa) << std::endl;






}
