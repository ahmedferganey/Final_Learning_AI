#include <iostream>
#include <iomanip> // Required for std::setprecision
#include <cmath>  // for std::isinf and std::isnan



// floating types and precision after .

int main(){

    float f = 1.23456789f;
    double d = 1.234567890123456789;
    long double ld = 1.2345678901234567890123456789;

    // Default precision
    std::cout << "Default precision:" << std::endl;
    std::cout << "float: " << f << std::endl;
    std::cout << "double: " << d << std::endl;
    std::cout << "long double: " << ld << std::endl;

    // Setting precision
    std::cout << "\nSetting precision to 5:" << std::endl;
    std::cout << std::fixed << std::setprecision(5);
    std::cout << "float: " << f << std::endl;
    std::cout << "double: " << d << std::endl;
    std::cout << "long double: " << ld << std::endl;

    // Setting precision to 10
    std::cout << "\nSetting precision to 10:" << std::endl;
    std::cout << std::fixed << std::setprecision(10);
    std::cout << "float: " << f << std::endl;
    std::cout << "double: " << d << std::endl;
    std::cout << "long double: " << ld << std::endl;


    // float number1 {15611565165}; // Complier error

    // logical error during run time
    float number1 (15611565165); 
    number1 = number1 + 1;
    std::cout << "wrong presentation of number1'15611565165+1': " << number1 << std::endl;
    /* 
In C++, a float typically has about 7 decimal digits of precision. The number 15611565165 
(11 digits) exceeds this precision, which means it cannot be accurately represented by a 
float. As a result, when you attempt to add 1 to it, the value remains unchanged, or you 
might see unexpected results due to rounding errors.    
    */

    double z{1.155e8};
    std::cout << "z: " << z << std::endl;

///////////////////////////////////////////////////////////////////////////

    double positive = 5.0;
    double negative = -5.0;
    double zero = 0.0;

    // Positive infinity
    double pos_inf = positive / zero;
    std::cout << "5.0 / 0.0 = " << pos_inf << std::endl;
    if (std::isinf(pos_inf)) {
        std::cout << "Result is positive infinity." << std::endl;
    }

    // Negative infinity
    double neg_inf = negative / zero;
    std::cout << "-5.0 / 0.0 = " << neg_inf << std::endl;
    if (std::isinf(neg_inf)) {
        std::cout << "Result is negative infinity." << std::endl;
    }

    // NaN
    double nan = zero / zero;
    std::cout << "0.0 / 0.0 = " << nan << std::endl;
    if (std::isnan(nan)) {
        std::cout << "Result is NaN." << std::endl;
    }
///////////////////////////////////////////////////////////////////////////







}
