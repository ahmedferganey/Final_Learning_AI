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
    // virtual destructor ensures proper cleanup
    virtual ~Animal(){
        cout << "Animal destructor called waa waa waa" << endl;
    }
};

// Derived class Dog overriding the base class sound() method
class Dog : public Animal {

public:
    // override the virtual function
    void sound() override{
        cout << "Dog barks" << endl;
    }
    // Destructor
    ~Dog(){
        cout << "Dog destructor called" << endl;
    }
};

// Derived class Cat overriding the base class's sound() method
class Cat : public Animal {
public:
    // Override the virtual function
    void sound() override {
        cout << "Cat meows" << endl;
    }

    // Destructor
    ~Cat() {
        cout << "Cat destructor called" << endl;
    }
};

int main() {
    std::cout << "Example_1 example for 09_Virtual_Functions" << std::endl;

    // base class pointer to Dog object
    Animal* animalptr = new Dog();
    animalptr->sound();  // Calls Dog's overridden sound() method
    delete animalptr;    // Calls Dog's destructor, then Animal's destructor

    // Base class pointer to Cat object
    animalptr = new Cat();
    animalptr->sound();  // Calls Cat's overridden sound() method
    delete animalptr;    // Calls Cat's destructor, then Animal's destructor



    return 0;
}
