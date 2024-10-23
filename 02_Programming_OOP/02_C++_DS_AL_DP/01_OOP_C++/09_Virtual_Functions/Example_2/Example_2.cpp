// Example_2.cpp - Example code for 09_Virtual_Functions
#include <iostream>

using namespace std;

// 1. simple virtual function
class base {
    public:
        virtual void show(){
            cout << "Base class show function" << endl;
        }
};
class derived : public base{
    public:
        void show() {  // No `override` keyword
            cout << "Derived class show function" << endl;            
        }
};


// 2. pure virtual function
class base2{
    public:
        virtual void show()=0; // pure virtual function
        /* forces derived classes to implememnt it */

};
class derived2 : public base2{
    public:
        void show() override{
        cout << "Derived class show function" << endl;
    }
};
// 3. virtual destructor
class base3{
    public:
        virtual ~base3(){
            cout << "Base destructor" << endl;
        }
};
class derived3 : public base3{
    public:
        ~derived3(){
        cout << "Derived destructor" << endl;
    }
};

// 4. final virtual function
class Base4 {
public:
    virtual void show() final {
        cout << "Base class final show function" << endl;
    }
};

class Derived4 : public Base4 {
    // This will cause a compilation error since `show()` is final in Base
    // void show() override { 
    //     cout << "Derived class show function" << endl;
    // }
};


// 5. override virtual function
class Base5 {
public:
    virtual void show() {
        cout << "Base class show function" << endl;
    }
};

class Derived5 : public Base5 {
public:
    void show() override {
        cout << "Derived class show function" << endl;
    }
};

// 6. Covariant Return Type in Virtual Function
class base6{
    public:
        virtual base6* clone(){
            return new base6();
        }
};
class derived6 : public base6 {
    public:
        derived6* clone() override{ // Covariant return type
             return new derived6();
        }
};

// 7. Virtual Copy Constructor (Non-standard)
class Base {
public:
    virtual Base* clone() const = 0;  // Pure virtual clone function
};

class Derived : public Base {
public:
    Derived* clone() const override {
        return new Derived(*this);
    }
};



int main() {
    std::cout << "Example_2 example for 09_Virtual_Functions" << std::endl;
    return 0;
}
