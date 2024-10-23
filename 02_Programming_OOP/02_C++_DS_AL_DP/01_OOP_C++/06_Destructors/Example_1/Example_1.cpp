// Example_1.cpp - Example code for 06_Destructors
#include <iostream>
#include <memory>

using namespace std;

// Traditional C++
class MyClass {
private:
    int* data;  // Pointer to dynamically allocated memory

public:
    // Constructor
MyClass(int value) {
        data = new int;  // Allocate memory dynamically
        *data = value;
        std::cout << "Constructor called! Allocated memory and set value: " << *data << std::endl;
    }

    // Destructor
    ~MyClass() {
        std::cout << "Destructor called! Deleting allocated memory." << std::endl;
        delete data;  // Free the dynamically allocated memory
    }
    // Method to print the value
    void print() {
        std::cout << "Value: " << *data << std::endl;
    }    
};


// Modern c++
class Data_class{
private:
    unique_ptr<int> data; // Smart pointer to manage dynamic memory
public:
    Data_class(int value) : data(make_unique<int>(value)){
        std::cout << "Constructor called! Allocated memory and set value: " << *data << std::endl;
    }
    // Destructor is not needed anymore because std::unique_ptr automatically frees memory
    void printdata() const {
        cout << "Value: " << *data << endl;
    }
};

int main() {
    std::cout << "Example_1 example for 06_Destructors" << std::endl;
    Data_class obj(42);  // Constructor allocates memory and sets value to 42
    obj.printdata();  // Output the value
    // Destructor will automatically be called at the end of the scope, freeing memory (handled by std::unique_ptr)
    
    
    MyClass obj2(42);  // Constructor allocates memory and sets value to 42
    obj2.print(); // Output the value
    // Destructor will automatically be called at the end of the scope, freeing memory


    return 0;
}
