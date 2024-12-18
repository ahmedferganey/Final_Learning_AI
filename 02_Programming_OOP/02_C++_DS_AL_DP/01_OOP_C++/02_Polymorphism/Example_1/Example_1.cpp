// Example_1.cpp - Example code for 02_Polymorphism
#include <iostream>
#include <cmath>
#include <algorithm>
#include <iomanip>
#include <cstring>

using namespace std;

// Base class for Vehicle
class vehicle {
protected: // Change to protected so derived classes can access it
    string brand{"car"}; // Initialize with a default value

public:
    // Constructor
    vehicle(string your_brand = "car") { 
        cout << "Hello, vehicle class call from constructor, class initialization" << endl;
        brand = your_brand; // Corrected the variable name
        cout << brand << endl;
    }    

    // Virtual function for polymorphism
    virtual void honk() {
        cout << "Tuut, tuut! Generic vehicle honk!\n";
    }
};

// Another base class for Engine
class Engine {
protected:
    int horsepower;

public:
    Engine(int hp = 100) : horsepower(hp) {
        cout << "Hello, Engine class call from constructor, class initialization" << endl;
        cout << horsepower << endl;
    }

    void showHorsepower() {
        cout << "Horsepower: " << horsepower << " HP" << endl;
    }
};

// Derived class
class Car : public vehicle, public Engine { // The class inherits from vehicle and Engine
private:
    int Manuf_year = 5; // private member 
    int id_num{}; // private member 

public: // Access specifier
    string myString;  // Attribute (string variable)
    string model;
    int year; // Attribute (int variable)

    // Default constructor
    Car() : vehicle(), Engine() { // Initialize the base class constructors
        cout << "Hello, Car class call from constructor, class initialization" << endl;
    }

    // Parameterized constructor
    Car(string x, string y, string z, int w, int hp) : vehicle(x), Engine(hp) { // Initialize the base classes
        cout << "Hello, Car class call from insider Constructor with parameters, class initialization" << endl;
        myString = z;
        model = y;
        year = w;        
    }

    // Override the honk method
    void honk() override {
        cout << "Beep beep! Car honk!\n";
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

// Another derived class, Truck
class Truck : public vehicle {
public:
    // Constructor
    Truck(string your_brand) : vehicle(your_brand) {
        cout << "Hello, Truck class call from constructor, class initialization" << endl;
    }

    // Override the honk method
    void honk() override {
        cout << "Honk Honk! Truck horn!\n";
    }
};

int main() {
    cout << "Example of polymorphism in vehicle honks" << endl;

    // Creating a Car object
    Car myCar("BMW", "X5", "Luxury SUV", 2020, 250);
    // Creating a Truck object
    Truck myTruck("Ford");

    // Using base class pointer for polymorphism
    vehicle* myVehicle;

    // Pointing to Car object
    myVehicle = &myCar;
    myVehicle->honk(); // Calls the Car version of honk()

    // Pointing to Truck object
    myVehicle = &myTruck;
    myVehicle->honk(); // Calls the Truck version of honk()

    // Accessing the base class methods
    myCar.showHorsepower();
    
    // Setting and getting the manufacturer year and ID number
    myCar.set_Manuf_year(2020);
    myCar.set_id_num(12345);
    
    // Displaying car information
    myCar.displayInfo();

    return 0;
}
