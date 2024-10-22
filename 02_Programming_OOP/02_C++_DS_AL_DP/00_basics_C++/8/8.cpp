#include <iostream>







void passByValue(int x) {
    x = 100;  // Modifies the copy, original remains unchanged
}

void passByPointer(int* x) {
    *x = 200;  // Modifies the original value
}

void passByPointerToConst(const int* x) {
    // *x = 300;  // ERROR: Cannot modify a const pointer's value
    std::cout << "Pointer to Const: " << *x << std::endl;
}

void passByConstPointerToConst(const int* const x) {
    // *x = 400;  // ERROR: Cannot modify the value or pointer
    std::cout << "Const Pointer to Const: " << *x << std::endl;
}

void passByReference(int& x) {
    x = 500;  // Modifies the original value
}

void passByConstReference(const int& x) {
    // x = 600;  // ERROR: Cannot modify a const reference
    std::cout << "Const Reference: " << x << std::endl;
}
///////////////////////////////////////////////////////////////////////////

// Return by value
int returnByValue(int x) {
    return x + 10;  // Copy of the modified value is returned
}

// Return by reference
int& returnByReference(int& x) {
    x += 20;  // Modifies the original value
    return x;  // Returns a reference to the original
}

// Return by pointer
int* returnByPointer(int* x) {
    if (x) {
        *x += 30;  // Modifies the original value through pointer
    }
    return x;  // Returns the pointer (could return nullptr)
}

// Return array element by pointer
int* returnArrayElement(int* array, int index) {
    return &array[index];  // Returns pointer to the specific element
}
///////////////////////////////////////////////////////////////////////////


int main(){


    int int_data{33};
    double double_data{55};

    //References
    int& ref_int_data{int_data};
    double& ref_double_data{double_data};

    //Print stuff out
    std::cout << "int_data : " << int_data << std::endl;
    std::cout << "&int_data : " << &int_data << std::endl;
    std::cout << "double_data : " << double_data << std::endl;
    std::cout << "&double_data : " << &double_data << std::endl;

    std::cout << "=======================" << std::endl;

    std::cout << "ref_int_data : " << ref_int_data << std::endl;
    std::cout << "&ref_int_data : " << &ref_int_data << std::endl;
    std::cout << "ref_double_data : " << ref_double_data << std::endl;
    std::cout << "&ref_double_data : " << &ref_double_data << std::endl;

  ref_int_data = 1012;
    ref_double_data = 1000.45;


   //Print stuff out
    std::cout << std::endl;
    std::cout << "int_data : " << int_data << std::endl;
    std::cout << "&int_data : " << &int_data << std::endl;
    std::cout << "double_data : " << double_data << std::endl;
    std::cout << "&double_data : " << &double_data << std::endl;

    std::cout << "=======================" << std::endl;

    std::cout << "ref_int_data : " << ref_int_data << std::endl;
    std::cout << "&ref_int_data : " << &ref_int_data << std::endl;
    std::cout << "ref_double_data : " << ref_double_data << std::endl;
    std::cout << "&ref_double_data : " << &ref_double_data << std::endl;
    
/////////////////////////////////////////////////////////////
	//Declare pointer and reference

    double double_value {12.34};
    double& ref_double_value {double_value}; // Reference to double_value
    double* p_double_value {&double_value}; //Pointer to double_value
	
	//Reading
	std::cout << "double_value : " << double_value << std::endl;
	std::cout << "ref_double_value : " << ref_double_value << std::endl;
	std::cout << "p_double_value : " << p_double_value << std::endl;
	std::cout << "*p_double_value : " << *p_double_value << std::endl;

	//Writting through pointer
	*p_double_value = 15.44;
	
    std::cout << std::endl;
	std::cout << "double_value : " << double_value << std::endl;
	std::cout << "ref_double_value : " << ref_double_value << std::endl;
	std::cout << "p_double_value : " << p_double_value << std::endl;
	std::cout << "*p_double_value : " << *p_double_value << std::endl;
	
	//Writting through reference
	ref_double_value = 18.44;
	
    std::cout << std::endl;
	std::cout << "double_value : " << double_value << std::endl;
	std::cout << "ref_double_value : " << ref_double_value << std::endl;
	std::cout << "p_double_value : " << p_double_value << std::endl;
	std::cout << "*p_double_value : " << *p_double_value << std::endl;


/////////////////////////////////////////////////////////////////
  double some_other_double{78.45};

    //Make the reference reference something else.
    ref_double_value = some_other_double;

    std::cout << "Making the reference reference something else..." << std::endl;
    std::cout << std::endl;
	std::cout << "double_value : " << double_value << std::endl;
	std::cout << "ref_double_value : " << ref_double_value << std::endl;
	std::cout << "p_double_value : " << p_double_value << std::endl;
	std::cout << "*p_double_value : " << *p_double_value << std::endl;
////////////////////////////////////////////////////////////
	//Non const reference
	std::cout << std::endl;
	std::cout << "Non const reference : " << std::endl;
	int age {27};
	const int& ref_age{age};

	std::cout << "age : " << age << std::endl;
	std::cout << "ref_age : " << ref_age << std::endl;
	
        // ref_age=44; // compiler error , read only refrence

   //Simulating reference behavior with pointers
   const int * const p_age {&age};
        // *p_age = 45; // compiler error , read only refrence

///////////////////////////////////////////////////////////////

int scores[] {1,2,3,4,5,6,7,8,9,10};  // Initialize an array 'scores' with 10 integers.

std::cout << std::endl;  // Print a newline for formatting.

std::cout << "Scores : ";  // Print a label to indicate the array content is being printed.
    
for ( auto score : scores){  // Range-based for loop to iterate over each element of the array 'scores'.
    std::cout << " " << score*2 ;  // Print each element (score) of the array followed by a space.
}

std::cout << std::endl;  // Print another newline at the end for formatting.


    std::cout << "still same old values " << std::endl;  
for ( auto score : scores){  
    std::cout << " " << score ;  
}
std::cout << std::endl;  


    std::cout << "using refrence" << std::endl;   

   for ( auto& score : scores){
        score = score * 10;
/*
Reference (auto&): In this range-based for loop, auto& score is a 
reference to each element in the array. By using a reference (&), 
you directly modify the original elements in the scores array. 
Without the reference, score would just be a copy of each element, 
and the original array would remain unchanged.
*/        
    }
    std::cout << "after using ref changed the values " << std::endl;  
for ( auto score : scores){  
    std::cout << " " << score ;  
}
std::cout << std::endl;  

////////////////////////////////////////////////////////////////////////////
        // function

    
    int a = 10;

    passByValue(a);
    std::cout << "After passByValue: " << a << std::endl;  // Output: 10 (unchanged)

    passByPointer(&a);
    std::cout << "After passByPointer: " << a << std::endl; // Output: 200 (modified)

    passByPointerToConst(&a);
    passByConstPointerToConst(&a);

    passByReference(a);
    std::cout << "After passByReference: " << a << std::endl; // Output: 500 (modified)

    passByConstReference(a);
////////////////////////////////////////////////////////////////////////////////
    int aaa = 10;
    int arr[5] = { 1, 2, 3, 4, 5 };

    // Return by Value
    int val = returnByValue(aaa);
    std::cout << "Return by Value: " << val << std::endl;  // Output: 20

    // Return by Reference
    int& ref = returnByReference(aaa);
    std::cout << "Return by Reference: " << aaa << std::endl;  // Output: 30 (modified original)
    std::cout << "Reference value: " << ref << std::endl;     // Output: 30

    // Return by Pointer
    int* ptr = returnByPointer(&aaa);
    if (ptr) {
        std::cout << "Return by Pointer: " << *ptr << std::endl;  // Output: 60 (modified original)
    }

    // Return Array Element by Pointer
    int* arrayElement = returnArrayElement(arr, 2);
    std::cout << "Return Array Element by Pointer: " << *arrayElement << std::endl;  // Output: 3


}
