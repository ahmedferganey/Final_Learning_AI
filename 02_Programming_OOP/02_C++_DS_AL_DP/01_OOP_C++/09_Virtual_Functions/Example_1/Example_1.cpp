// Example_1.cpp - Example code for 09_Virtual_Functions
#include <iostream>

using namespace std;

// base class
class Animal{
public:
    // virtual function that can be overidden
    virtual void sound(){
        cout << "Animal makes a sound" << endl;
    }
}

int main() {
    std::cout << "Example_1 example for 09_Virtual_Functions" << std::endl;
    return 0;
}
