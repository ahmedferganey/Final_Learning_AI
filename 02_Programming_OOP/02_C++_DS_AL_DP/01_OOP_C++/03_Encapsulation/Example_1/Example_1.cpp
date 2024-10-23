// Example_1.cpp - Example code for 03_Encapsulation
#include<iostream> 
#include<cmath>
#include<algorithm>
#include<iomanip>
#include<cstring>

using namespace std;

class Car {       // The class
    int Manuf_year = 5; // private member 
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


    // encapsulation
    void set_Manuf_year(int s){
        Manuf_year = s;
    };
    void set_id_num(int t){
        id_num = t;
    };

    int get_Manuf_year(){
        return Manuf_year;
    };
    int get_id_num(){
        return id_num;
    };

  private:
    int id_num{}; // private member 
};


int target{};

int main() {
    std::cout << "Example_1 example for 03_Encapsulation" << std::endl;

    Car carObj3("Tesla", "X5", "ahmed", 2017);
    Car carObj4("MCV", "Mustang", "mariam", 2019);

    cout << carObj4.get_Manuf_year() << "\n"; // allowed cause applying encapsulation
    cout <<  "before settting  id : " << endl;
    cout << carObj4.get_id_num() << "\n"; // allowed cause applying encapsulation
    carObj4.set_id_num(5); // allowed cause applying encapsulation
    cout << "after settting  id : " << carObj4.get_id_num() << "\n"; // allowed cause applying encapsulation

    return 0;
}
