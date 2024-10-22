#include <iostream>
#include <vector>

const int Pen{ 10 };
const int Marker{ 20 };
const int Eraser{ 30 };
const int Rectangle{ 40 };
const int Circle{ 50 };
const int Ellipse{ 60 };


int main(){
   int tool {Eraser};

    switch (tool)
    {
        case Pen : {
             std::cout << "Active tool is Pen" << std::endl;
        }
        break;

        case Marker : {
             std::cout << "Active tool is Marker" << std::endl;
        }
        break;


        case Eraser :{
             std::cout << "Eraser" << std::endl;
        }
        case Rectangle : 
        case Circle : {
             std::cout << "Drawing Shapes" << std::endl;
        }
        break;

        case Ellipse : {
             std::cout << "Active tool is Ellipse" << std::endl;
        }
        break;
    
        default: {
            std::cout << "No match found" << std::endl;
        }
            break;
    }

    std::cout << "Moving on" << std::endl;

/////////////////////////////////////////////////////////////
int max = (1 < 5)? true : false;
            std::cout << max << std::endl;
bool fast = true;
int speed{fast? true:false};
            std::cout << fast << std::endl;
            std::cout << speed << std::endl;
//////////////////////////////////////////////////////////////////
for (unsigned int i{1}; i<10; i++){
    std::cout << "i love mariam" << std::endl;
}

    std::vector<int> numbers = {1, 2, 3, 4, 5};

    // Using size_t
    for (size_t i{}; i < numbers.size(); ++i) {
        std::cout << "size_t index: " << i << " value: " << numbers[i] << std::endl;
    }

    // Using unsigned int
    unsigned int count = 5;
    for (unsigned int i = count; i > 0; --i) {
        // This works fine, but let's see what happens if we go too far
        std::cout << "unsigned int index: " << i << " value: " << numbers[i - 1] << std::endl;
    }

    // Example of potential issue with unsigned int
    unsigned int negativeIndex = -1; // This wraps around to a large positive number
    std::cout << "Wrap around with unsigned int: " << negativeIndex << std::endl;


/////////////////////////////////////////////////////////////////

   //Don't hard code values : BAD!

    const size_t COUNT{100};
    /*
If you hard-code values like 100 directly into the loop, 
it can make your code harder to maintain and understand, 
especially in more complex programs where 100 might have 
some specific meaning. By using COUNT, it's clear what 
the value represents and makes future modifications simpler.    
    */

    for(size_t i{0} ; i < COUNT ; ++i){
        std::cout << i << " : I love C++" << std::endl;
    }
    std::cout << "Loop done!" << std::endl;



    size_t i{0}; // Iterator defined outside

    for(  ; i < 10 ; ++i){
        std::cout << i << " : I love C++" << std::endl;
    }
    std::cout << "Loop done!" << std::endl;
    std::cout << "i : " << i << std::endl;
    for (size_t i{0} , x {5}, y{22} ; y > 15 ; ++i , x+=5 , y-=1){
        std::cout << "i: " << i << ", x : " << x << ", y : " << y << std::endl;

    }
    ///////////////////////////////////////////
    int increment {5};
    int number1 {10};
    int number2 {20};
    int number3 {25};
    int result = (number1 *= ++increment, number2 - (++increment), number3 += ++increment);
    std::cout << "number1 : " << number1 << std::endl; // 60
    std::cout << "number2 : " << number2 << std::endl; // 20
    std::cout << "number3 : " << number3 << std::endl; // 33
    std::cout << "result : " <<  result << std::endl; // 33
    //////////////////////////////////////////////
    int bag_of_values [] {1,2,3,4,5,6,7,8,9,10}; 
   // The variable value will be assigned a value from the values array on each iteration
	

    //In this loop, you're using size_t as the loop index to iterate over the array bag_of_values[].
    for(size_t i {0} ; i < 4 ; ++i){
        std::cout << "value : " << bag_of_values[i] << std::endl;
    }
    
  //Here, you’re using auto to automatically deduce the type of value in the loop.
   // Using auto in a Range-Based For Loop
   //Auto type deduction
	for (auto value : {1,2,3,4,5,6,7,8,9,10}){
        //value holds a copy of the current iteration in the whole bag
        std::cout << " value : " << value << std::endl;
        /*
By default, in this range-based for loop, the variable value is copied from the element in the range. This means each element is not a reference to the original but a copy.
The loop will behave as though value were declared as int explicitly.        
         */
    }   	
    
    // by refrence
    for (auto& value : {1,2,3,4,5,6,7,8,9,10}){
        std::cout << " value : " << value << std::endl;
        /*
Initializer List: In the code you provided, {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} is 
an initializer list, which is a temporary object. It contains values of type 
int and is not stored anywhere; it's created just for the loop.        
        */
    }
    
    
    
    for (int value : bag_of_values){
        //value holds a copy of the current iteration in the whole bag
        std::cout << " value : " << value << std::endl;
        /*
In this loop, the variable value is of type int, which means that for each iteration, 
a copy of the element in bag_of_values is created and assigned to value.   
This is the most common and efficient way to iterate over arrays of small types 
(like int, char, float, etc.), where the cost of copying is minimal.     
         */
    }
    
    for (auto& value : bag_of_values){
        // value is a reference to the current element in the array
        std::cout << " value : " << value << std::endl;

    /*
    What happens here?
    In this loop, value is declared as a reference (&) to each element in bag_of_values.
     This means that instead of copying each element, the loop iterates over references 
     to the elements in the array.

    Efficiency:
    Using a reference is generally more efficient when dealing with large or complex objects 
    (like std::string, std::vector, or user-defined types), as it avoids the cost of copying.
     However, for primitive types like int, the difference in performance is minimal or
      non-existent because copying an integer is already cheap.

    Use case:
    Using auto& would be more beneficial when iterating over collections of non-primitive 
    data types or when you need to modify the elements in the array. In this case, using references prevents unnecessary copying and allows direct modification of the elements.
    */    
    }




   //Specify the collection in place
   
    for (int value : {1,2,3,4,5,6,7,8,9,10}){
        //value holds a copy of the current iteration in the whole bag
        std::cout << " value : " << value << std::endl;
    }
  

    //////////////////////////////////////////////

    const size_t COUNT2{100};
    size_t i2{0}; // Iterator declaration

    while(i2 < COUNT2 ){ // Test
       std::cout << i2 << " : I love C++" << std::endl;

       ++i2; // Incrementation 
    }
    std::cout << "Loop done!" << std::endl;
    i=11;
    do{
        std::cout << i << " : I love C++" << std::endl;
        ++i; // Incrementation
    }while( i < COUNT);

    std::cout << "Loop done!" << std::endl;
//////////////////////////////////////////////

}
