// Example_1.cpp - Example code for 04_Abstraction
#include <iostream>
#include <cmath>
#include <algorithm>
#include <iomanip>
#include <cstring>


using namespace std;

// Abstract base class for vehicle
class vehicle{
protected:
    string brand;
public:
    vehicle(string your_brand = "generic") : brand(your_brand){
        cout << "Vehicle constructor called: " << brand << endl;
    }
    // pure virtual function to make the class abstract 
    virtual void honk()=0; // pure virtual no implementation
    // virtual destructor to allow proper cleanup of derived classes
    virtual ~vehicle(){
        cout << "vehicle destructor called for:" << brand << endl;
    }
};


// Engine class (not abstract , but used by derived classes)
class Engine{
protected:
    int horsepower;
public:
    Engine(int hp = 100) : horsepower(hp){
        cout << "Engine constructor called with " << horsepower << " HP" << endl;
    };
    void showHorsepower() {
        cout << "Horsepower: " << horsepower << " HP" << endl;
    }
    ~Engine(){
        cout << "Engine destructor called for " << horsepower << " HP" << endl;
    }

};

class car : public vehicle, public Engine{
private:
    string model;
    int year;
public:
    // constructor 
    car(string your_brand, string your_model, int your_year, int hp) 
    : vehicle(your_brand), Engine(hp), model(your_model), year(your_year) 
    {
        cout << "Car constructor called for " << brand << " " << model << endl;
    };
    // Override the pure virtual function honk()
    void honk() override {
        cout << "Beep beep! Car honk for " << brand << " " << model << "!\n";
    }

    void displayInfo() {
        cout << "Car info: " << brand << " " << model << ", Year: " << year << endl;
    }

    ~car() {
        cout << "Car destructor called for " << brand << " " << model << endl;
    }
};


// Derived class Truck inheriting from vehicle
class Truck : public vehicle {
private:
    int loadCapacity;

public:
    // Constructor
    Truck(string your_brand, int capacity) 
        : vehicle(your_brand), loadCapacity(capacity) {
        cout << "Truck constructor called for " << brand << " with load capacity " << loadCapacity << " tons" << endl;
    }

    // Override the pure virtual function honk()
    void honk() override {
        cout << "Honk honk! Truck horn for " << brand << " with load capacity " << loadCapacity << " tons!\n";
    }

    ~Truck() {
        cout << "Truck destructor called for " << brand << endl;
    }
};


int main() {
    std::cout << "Example_1 example for 04_Abstraction" << std::endl;

    cout << "Abstraction example with vehicles\n";

    // Create Car object using abstract base class pointer
    vehicle* myCar = new car("BMW", "X5", 2020, 250);
    myCar->honk();  // Calls Car's honk method
    delete myCar;   // Proper cleanup due to virtual destructor

    cout << "\n";

    // Create Truck object using abstract base class pointer
    vehicle* myTruck = new Truck("Ford", 10);
    myTruck->honk();  // Calls Truck's honk method
    delete myTruck;   // Proper cleanup due to virtual destructor




    return 0;
}
