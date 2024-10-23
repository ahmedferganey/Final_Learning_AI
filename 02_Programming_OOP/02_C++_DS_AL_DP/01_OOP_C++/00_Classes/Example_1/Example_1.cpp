// Example_1.cpp - Example code for 00_Classes
#include<iostream> 
#include<cmath>
#include<algorithm>
#include<iomanip>
#include<cstring>

using namespace std;

class Car {       // The class
  public:             // Access specifier
    int year;        // Attribute (int variable)
    string myString;  // Attribute (string variable)
    string brand;   
    string model;

    int speedoutsideclass(int maxSpeed); // Method/function declaration
    int speedinsideclass(int maxSpeed){ // Method/function declaration na deifinition
          return maxSpeed;
    }
};


int Car::speedoutsideclass(int maxSpeed) {
  return maxSpeed;
}


int main() {
    cout << "Example_1 example for 00_Classes" << endl;
    // Create an object of Car
    Car carObj1;
    carObj1.brand = "BMW";
    carObj1.model = "X5";
    carObj1.year = 1999;
    Car carObj2;
    carObj2.brand = "Ford";
    carObj2.model = "Mustang";
    carObj2.year = 1969;

    cout << carObj1.brand << " " << carObj1.model << " " << carObj1.year << "\n";
    cout << carObj2.brand << " " << carObj2.model << " " << carObj2.year << "\n";
    cout << "Speed from inside Class: " <<carObj2.speedinsideclass(120) << endl; 
    cout << "Speed from outside  Class: " <<carObj2.speedoutsideclass(120) << endl; 

    return 0;
}
