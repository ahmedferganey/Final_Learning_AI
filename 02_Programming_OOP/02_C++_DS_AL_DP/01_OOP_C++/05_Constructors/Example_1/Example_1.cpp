// Example_1.cpp - Example code for 05_Constructors
#include<iostream> 
#include<cmath>
#include<algorithm>
#include<iomanip>
#include<cstring>

using namespace std;

class Car {       // The class
  public:             // Access specifier
    string myString;  // Attribute (string variable)
    string brand;   
    string model;
    int year;        // Attribute (int variable)


    // Constructor and destractor
    Car(){ // constructor
        cout << "hello, class call from constructor, class initilization" << endl;
    };
    Car(string x, string y, string z, int w){ // constructor
        cout << "hello, class call from  insider Constructor with parameters, class initilization" << endl;
        myString = z;
        brand = x;
        model = y;
        year = w;        
    };
    int speedoutsideclass(int maxSpeed); // Method/function declaration
    int speedinsideclass(int maxSpeed){ // Method/function declaration na deifinition
          return maxSpeed;
    }
};

// Car::Car(string x, string y, string z, int w){  
//     cout << "hello, class call from  outsider Constructor with parameters, class initilization" << endl;
//     myString = z;
//     brand = x;
//     model = y;
//     year = w;
// };

int main() {
    std::cout << "Example_1 example for 05_Constructors" << std::endl;

    Car myObj;    // Create an object of MyClass (this will call the constructor)


    Car carObj1("BMW", "X5", "ahmed", 1999);
    Car carObj2("Ford", "Mustang", "mariam", 1969);

    cout << carObj1.brand << " " << carObj1.model << " " << carObj1.year << "\n";
    cout << carObj2.brand << " " << carObj2.model << " " << carObj2.year << "\n";

    Car carObj3("Tesla", "X5", "ahmed", 2017);
    Car carObj4("MCV", "Mustang", "mariam", 2019);

    return 0;
}
