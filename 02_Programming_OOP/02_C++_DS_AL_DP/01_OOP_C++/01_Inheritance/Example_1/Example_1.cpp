// Example_1.cpp - Example code for 01_Inheritance
#include <iostream>
#include <cmath>
#include <algorithm>
#include <iomanip>
#include <cstring>

using namespace std;

// Base class
class vehicle {
protected: // Change to protected so derived classes can access it
    string brand{"car"}; // Initialize with a default value

public:
    // Constructor
    vehicle(string your_brand = "car") { 
        cout << "Hello, vehicle class call from constructor, class initialization" << endl;
        brand = your_brand; // Corrected the variable name
    }    

    void honk() {
        cout << "Tuut, tuut! \n";
    }
};

// Derived class
class Car : public vehicle { // The class inherits from vehicle
private:
    int Manuf_year = 5; // private member 
    int id_num{}; // private member 

public: // Access specifier
    string myString;  // Attribute (string variable)
    string model;
    int year; // Attribute (int variable)

    // Default constructor
    Car() : vehicle() { // Initialize the base class constructor
        cout << "Hello, Car class call from constructor, class initialization" << endl;
    }
/*
    Car() {
        cout << "Hello, class call from constructor, class initialization" << endl;
    }
In this case, the base class's default constructor (if it exists) 
will be called implicitly.
If the base class has no default constructor and only has a constructor 
that takes parameters, this will lead to a compilation error.
 */    

    // Parameterized constructor
    Car(string x, string y, string z, int w) : vehicle(x) { // Initialize the base class with brand
        cout << "Hello, Car class call from insider Constructor with parameters, class initialization" << endl;
        myString = z;
        model = y;
        year = w;        
    }

    // Method/function declarations
    int speedoutsideclass(int maxSpeed);
    int speedinsideclass(int maxSpeed) { 
        return maxSpeed;
    }

    // Encapsulation
    void set_Manuf_year(int s) {
        Manuf_year = s;
    }

    void set_id_num(int t) {
        id_num = t;
    }

    int get_Manuf_year() {
        return Manuf_year;
    }

    int get_id_num() {
        return id_num;
    }

    // Method to display car details
    void displayInfo() {
        cout << "Brand: " << brand << ", Model: " << model << ", Year: " << year 
             << ", Manufacturer Year: " << Manuf_year << ", ID: " << id_num << endl;
    }
};

int main() {
    std::cout << "Example_1 example for 01_Inheritance" << std::endl;

    // Creating a Car object
    Car myCar("BMW", "X5", "Luxury SUV", 2020);
    
    // Accessing the base class method
    myCar.honk();

    // Setting and getting the manufacturer year and ID number
    myCar.set_Manuf_year(2020);
    myCar.set_id_num(12345);
    
    // Displaying car information
    myCar.displayInfo();

    return 0;
}
