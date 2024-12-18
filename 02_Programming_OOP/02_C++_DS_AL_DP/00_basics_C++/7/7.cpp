#include <iostream>
#include <iostream>
#include <cstdlib>  // for std::rand() and std::srand()
#include <ctime>    // for std::time()



int main(){

////////////////////////////////////////////////////////////////////
    // Declare an array of ints
    int scores [10]; // Junk data
	double salaries[5] {12.7, 7.5, 13.2, 8.1, 9.3};     //Declare and initialize at the same time
    int families[5] {12, 7, 5}; //If you don't initialize all the elements, those you leave out are initialized to 0
	int class_sizes[] {10,12,15,11,18,17,23,56};  //Omit the size of the array at declaration
    int scores2[]{1,2,3,4,45};
    int count{std::size(scores2)};    



    std::cout << "sizeof(scores) : " << sizeof(scores2) << std::endl;
    std::cout << "sizeof(scores[0]) : " << sizeof(scores2[0]) << std::endl;
    //std::cout << "size(scores) : " << std::size(scores2[0]) << std::endl;
    std::cout << "size(scores) : " << std::size(scores) << std::endl; // is used to print the number of elements in the array scores.


    std::cout << "count : " << count << std::endl;

   // Read only arrays
   
   const int birds[] {10,12,15,11,18,17,23,56}; 
//    birds[2] = 8;
   


    for(size_t i{0}; i < 5; ++i){
		std::cout << "families[" << i << "] : " << families[i] << std::endl;
	}

    // Read data

   std:: cout << " scores [0] : " << scores[0] << std::endl;
   std:: cout << " scores [1] : " << scores[1] << std::endl;
   

    //Read with a loop
    
    for( size_t i {0} ; i < 10 ; ++i){
        std::cout << "scores [" << i << "] : " << scores[i] << std::endl;
    }
//////////////////////////////////////////////////////////////////////
        std::cout << "null termination \n\n\n" << std::endl; 

    // Declare an array of characters (C-string)
    char message[6] = "Hello";  // Ensure there is room for the null terminator
    std::cout << "Original message: " << message << std::endl; // Print the original message

    // Change characters in our array
    message[1] = 'a';  // Changing 'e' to 'a'
    std::cout << "Modified message: " << message << std::endl; // Print the modified message

    // Demonstrating C-strings and null termination
    char message1[] = {'H', 'e', 'l', 'l', 'o', '\0'};  // Proper C-string with null terminator
    std::cout << "C-string message1: " << message1 << std::endl;
    std::cout << "Size of message1: " << sizeof(message1) << std::endl;  // Includes null terminator

    char message2_without_null_terminator[6] = {'H', 'e', 'l', 'l', 'o'};  // No null terminator
    std::cout << "Size of message2_without_null_terminator: " << sizeof(message2_without_null_terminator) << std::endl; // Size without null terminator

    // Demonstrating integer array
    int numbers[] = {1, 2, 3, 4, 5};
    std::cout << "Numbers: ";
    for (auto num : numbers) {
        std::cout << num << " ";  // Print each number
    }
    std::cout << std::endl;

    // Show the size of the integer array
    std::cout << "Size of numbers: " << sizeof(numbers) / sizeof(numbers[0]) << std::endl; // Number of elements

    char message_probably_garpage[6]{'a','d','h'};
    // Will probably print garbage after your char array if not null-terminated
    std::cout << "Raw message (may contain garbage): " << message_probably_garpage << std::endl; // No null terminator example

//////////////////////////////////////////////////////////////////////

	int numbers44324[] {1,2,3,4,5,6,7,8,9,0};
	
	//Read beyond bounds : Will read garbage or crash your program
	//std::cout << "numbers[12] : " << numbers[12] << std::endl;

	//Write beyond bounds. The compiler allows it. But you don't own 
	//the memory at index 12, so other programs may modify it and your
	//program may read bogus data at a later time. Or you can even
	//corrupt data used by other parts of your ptogram
//////////////////////////////////////////////////////////////////////
    // Seed the random number generator
    std::srand(static_cast<unsigned int>(std::time(0))); // Seed with the current time

    // Generate random numbers in a loop
    std::cout << "Random numbers in range [1, 10]: " << std::endl;
    int random_num;
    for (size_t i {0}; i < 20; ++i) {
        // Generate a random number in the range [1, 10]
        random_num = std::rand() % 10 + 1; 
        std::cout << "random_num " << i << " : " << random_num << std::endl; // Output random number
    }

    // Demonstrating character array
    char message1312321[6] = "Hello"; // Initialize a character array (C-string)
    std::cout << "Message: " << message1312321 << std::endl; // Print the message

    // Modify and print the character array
    message1312321[1] = 'a'; // Change 'e' to 'a'
    std::cout << "Modified message: " << message1312321 << std::endl;

    // Show size of the character array
    std::cout << "Size of message: " << sizeof(message1312321) << std::endl; // Includes null terminator

    // Demonstrating integer array
    int numbers1212[] = {1, 2, 3, 4, 5};
    std::cout << "Numbers: ";
    for (auto num : numbers1212) {
        std::cout << num << " "; // Print each number
    }
    std::cout << std::endl;

    // Show size of the integer array
    std::cout << "Size of numbers: " << sizeof(numbers1212) / sizeof(numbers1212[0]) << std::endl; // Number of elements



//////////////////////////////////////////////////////////////////////
            // pointer
    
        //Declare and initialize pointer
    int* p_number {}; // Will initialize with nullptr
    double*  p_fractional_number{};

    //Explicitly initialize with nullptr
    int* p_number1{nullptr};
    int* p_fractional_number1{nullptr};

    //Pointers to different variables are  of the same size
    std::cout << "sizeof(int) : "                   << sizeof(int) << std::endl; // 4
    std::cout << "sizeof(double) : "                << sizeof(double) << std::endl; // 8
    std::cout << "sizeof(double*) : "               << sizeof(double*) << std::endl;
    std::cout << "sizeof(int*) : "                  << sizeof(int*) << std::endl;
    std::cout << "sizeof(p_number1) : "             << sizeof(p_number1) << std::endl;
    std::cout << "sizeof(p_fractional_number1) : "  << sizeof(p_fractional_number1) << std::endl;

    int *p_number5{nullptr}, other_int_var{};
    //It is better to separate these declarations on different lines though
    int *p_number7{};
    int other_int_var7{}; // No room for confusion this time

  //Initializing pointers and assigning them data
    //We know that pointers store addresses of variables
    int int_var {43};
    int *p_int{&int_var};// The address of operator (&);
    
    std::cout << "Int var : " << int_var << std::endl;
    std::cout << "p_int (Address in memory)  : " << p_int << std::endl;

    //You can also change the address stored in a pointer any time
    int int_var1 {65};
    p_int = &int_var1; // Assign a different address to the pointer
    std::cout << "p_int (with different address)  : " << p_int << std::endl;


    //Can't cross assign between pointers of different types
    int *p_int1{nullptr};
    double double_var{33};

    //p_int = &double_var; // Compiler error


    //Dereferencing a pointer : 
    int* p_int2 {nullptr};
    int int_data {56};
    p_int2 = &int_data;

    std::cout << "value : " << *p_int2 << std::endl; // Dereferencing a pointer    
//////////////////////////////////////////////////////////////////////
  
    const char * messagepp {"Hello World!"};
    std::cout << "messagepp : " << messagepp << std::endl;
    //*message = "B"; // Compiler error

    char * messagepointer {"Hello World!"};
    std::cout << "messagepointer : " << messagepointer << std::endl;
    //*messagepointer = 'a'; // core dumped 
    std::cout << "before" << std::endl;
    char messagepointer2[] = "Hello World!"; // Mutable character array
    messagepointer2[0] = 'a'; // Safely modify the first character
    std::cout << "AFter" << std::endl;
    std::cout << "messagepointer : " << messagepointer2 << std::endl;


//////////////////////////////////////////////////////////////////////

    int number {22}; // Stack
	
	int * p_number223f = &number;
	
	std::cout << std::endl;
	std::cout << "Declaring pointer and assigning address : " << std::endl;
	std::cout << "number : " << number << std::endl;
	std::cout << "p_number : " << p_number223f << std::endl;
	std::cout << "&number : " << &number << std::endl;
	std::cout << "*p_number : " << *p_number223f <<  std::endl;

	int * p_number1fds; // Uninitialized pointer , contains junk address
	int number1 {12};
	p_number1fds = &number1; // Make it point to a valid address
	std::cout << std::endl;
	std::cout << "Uninitialized pointer : " << std::endl;
	std::cout << "*p_number1 : " << *p_number1fds << std::endl;



   //BAD
	//Writing into uninitialized pointer through dereference
    /*
	int *p_number2; // Contains junk address : could be anything
    std::cout << "Writting in the 55" << std::endl;
	*p_number2 = 55; // Writing into junk address : BAD!
	std::cout << std::endl;
	std::cout << "Writing into uninitialized pointer through dereference" << std::endl;
	std::cout << "p_number2 : " << p_number2 << std::endl; // Reading from junk address.
    std::cout << "Dereferencing bad memory" << std::endl;
	std::cout << "*p_number2 : " << *p_number2 << std::endl;
    */


   	int * p_number3fewf {}; // Initialized with pointer equivalent of zero : nullptr
						// A pointer pointing nowhere
	int * p_number3 {nullptr};


//////////////////////////////////////////////////////////////////////

	int *p_number4_NEW{nullptr};
	p_number4_NEW = new int; 	// Dynamically allocate space for a single int on the heap
							// This memory belongs to our program from now on. The system
							// can't use it for anything else, untill we return it.
							//After this line executes, we will have a valid memory location
							// allocated. The size of the allocated memory will be such that it
							// can store the type pointed to by the pointer
                            // new ---> return pointer 

    *p_number4_NEW = 77; // Writting into dynamically allocated memory
	std::cout << "p_number4_NEW: " << *p_number4_NEW << std::endl;

    delete p_number4_NEW;
    p_number4_NEW = nullptr;


//////////////////////////////////////////////////////////////////////
        //It is also possible to initialize the pointer with a valid
	//address up on declaration. Not with a nullptr
     int *p_number5321dsf{ new int}; // Memory location contains junk value
     int *p_number6321dsf{ new int (22) }; // use direct initialization
     int *p_number7321dsf{ new int { 23 } }; // use uniform initialization
	 
	 std::cout << std::endl;
	 std::cout << "Initialize with valid memory address at declaration : " << std::endl;
	 std::cout << "p_number5 : " << p_number5321dsf << std::endl;
	 std::cout << "*p_number5 : " << *p_number5321dsf << std::endl; // Junk value
	 
	 std::cout << "p_number6 : " << p_number6321dsf << std::endl;
	 std::cout << "*p_number6 : " << *p_number6321dsf << std::endl;
	 
	 std::cout << "p_number7 : " << p_number7321dsf << std::endl;
	 std::cout << "*p_number7 : " << *p_number7321dsf << std::endl;
	 
	 //Remember to release the memory
	  delete p_number5321dsf;
	  p_number5321dsf = nullptr;
	  
	  delete p_number6321dsf;
	  p_number6321dsf = nullptr;
	  
	  delete p_number7321dsf;
	  p_number7321dsf = nullptr;

         //Can reuse pointers
      p_number5 = new int(81);
      std::cout << "*p_number : " << *p_number5 << std::endl;


      delete p_number5;
      p_number5 = nullptr;

      //Calling delete twice on a pointer : BAD!
      p_number5 = new int(99);
      std::cout << "*p_number5 : " << *p_number5 << std::endl;


      delete p_number5;
      // delete p_number5; // Core dumped 

    
//////////////////////////////////////////////////////////////////////

            // Dangline pointer
    	//Case1 : Uninitialized pointer
    /*
	int * p_numberDangling; // Dangling uninitialized pointer
   
	std::cout << std::endl;
	std::cout << "Case 1 : Uninitialized pointer : ." << std::endl;
	std::cout << "p_numberDangling : " << p_numberDangling << std::endl;
    std::cout << "*p_numberDangling : " << *p_numberDangling << std::endl; //CRASH! or undefined behavourial
    
   //Case 2 : deleted pointer

   std::cout << std::endl;
   std::cout << "Case 2 : Deleted pointer" << std::endl;
   int * p_number1deleted {new int{67}};
   
   std::cout << "*p_number1 (before delete) : " << *p_number1deleted << std::endl;
   
   delete p_number1deleted;
		
   std::cout << "*p_number1(after delete) : " << *p_number1deleted << std::endl; //CRASH! or undefined behavourial

*/
    	//Case 3 : Multiple pointers pointing to same address
    /*
	std::cout << std::endl;
	std::cout << "Case 3 : Multiple pointers pointing to same address : " << std::endl;
	
    int *p_number3 {new int{83}};
    int *p_number4 {p_number3};
    
    std::cout << "p_number3 - " << p_number3 << " - " << *p_number3 << std::endl;
    std::cout << "p_number4 - " << p_number4 << " - " << *p_number4 << std::endl;
    
    //Deleting p_number3
    delete p_number3;
    
    //p_number4 points to deleted memory. Dereferncing it will lead to
	//undefined behaviour : Crash/ garbage or whatever
    std::cout<< "p_number4(after deleting p_number3) - " << p_number4 << " - " << *p_number4 << std::endl;
*/


  //Solution1 : Initialize your pointers immediately upon declaration
    /*
	std::cout << std::endl;
	std::cout << "Solution 1 : " << std::endl;
    int *p_number5{nullptr};
    int *p_number6{new int(87)};
	
	//Check for nullptr before use

	if(p_number6!= nullptr){
		std::cout << "*p_number6 : " << *p_number6 << std::endl;
	}else{
        std::cout << "Invalid address" << std::endl;
    }
    */

	//Solution 2 : 
    //Right after you call delete on a pointer, remember to reset
	//the pointer to nullptr to make it CLEAR it doesn't point anywere
    /*
	std::cout << std::endl;
	std::cout << "Solution 2 : " << std::endl;
    int *p_number7{new int{82}};
    
    //Use the pointer however you want
    std::cout << "p_number7 - " << p_number7 << " - " << *p_number7 << std::endl;
   
    delete p_number7;
    p_number7 = nullptr; // Reset the pointer
	
	//Check for nullptr before use
	if(p_number7!= nullptr){
		std::cout << "*p_number7 : " << *p_number7 << std::endl;
	}else{
        std::cout << "Invalid memory access!" << std::endl;
    }
    */



   	//Solution 3 
	//For multiple pointers pointing to the same address ,  Make sure there is
	//one clear pointer (master pointer) that owns the memory ( responsible for releasing when
    // necessary) , other pointers should only be able to dereference when the master pointer is valid
    
	std::cout << std::endl;
	std::cout << "Solution 3 : " << std::endl;
    int * p_number8 {new int{382}};// Let's say p_number8 is the master pointer
    int * p_number9 {p_number8};
    
    //Dereference the pointers and use them
    std::cout << "p_number8 - " << p_number8 << " - " << *p_number8 << std::endl;
    
    if(!(p_number8 == nullptr)){ // Only use slave pointers when master pointer is valid
           std::cout<< "p_number9 - " << p_number9 << " - " << *p_number9 << std::endl;
    }
    
    delete p_number8; // Master releases the memory
    p_number8 = nullptr;
    
    if(!(p_number8 == nullptr)){ // Only use slave pointers when master pointer is valid
           std::cout<< "p_number9 - " << p_number9 << " - " << *p_number9 << std::endl;
    }else{
        std::cerr << "WARNING : Trying to use an invalid pointer" << std::endl;
    }
    

    std::cout << "Program is ending well" << std::endl;
  

//////////////////////////////////////////////////////////////////////

            //  Memory leak
     /*
    int *p_number {new int{67}}; // Points to some address, let's call that address1
    
    //Should delete and reset here 
    
    int number{55}; // stack variable
    
    p_number = &number; // Now p_number points to address2 , but address1 is still in use by 
                        // our program. But our program has lost access to that memory location.
						//Memory has been leaked.
    */

	//Double allocation 
    /*
    int *p_number1 {new int{55}};
    
	//Use the pointer
    
	//Should delete and reset here.
	
    p_number1 = new int{44}; // memory with int{55} leaked.

    delete p_number1;
    p_number1 = nullptr;
    */

	//Nested scopes with dynamically allocated memory
	{
		int *p_number2 {new int{57}};

        //Use the dynamic memory

	}
	//Memory with int{57} leaked.

    std::cout << "Program ending well" << std::endl;

  /*
    //int * data = new int[10000000000000000]; // 

    for(size_t i{0} ; i < 10000000 ; ++i){
        int * data = new int[100000000];
    }
    */

   //exception
   /*
    for(size_t i{0} ; i < 100 ; ++i){
        try{
            int * data = new int[1000000000];
        }catch(std::exception& ex){
            std::cout << "  Something went wrong : " << ex.what() << std::endl;
        }
    }
    */


   //std::nothrow
    for(size_t i{0} ; i < 100 ; ++i){
   
        int * data = new(std::nothrow) int[1000000000];

        if(data!=nullptr){
            std::cout << "Data allocated" << std::endl;
        }else{
            std::cout << "Data allocation failed" << std::endl;
        }
       
    }

    //It is OK call delete on a nullptr
	//Calling delete on a nullptr is OK
    int *p_number1swqsqw {};
    
    delete p_number1swqsqw;	// This won't cause any problem
						//if p_number1 contains nullptr

///////////////////////////////////////////////////////////
                // Dynamic VS Static Array

   const size_t size{10};
    
    //Different ways you can declare an array
	//dynamically and how they are initialized
	
    double *p_salaries { new double[size]}; // salaries array will
															//contain garbage  values
    int *p_students { new(std::nothrow) int[size]{} }; // All values initialized to 0 
    
    double *p_scores { new(std::nothrow) double[size]{1,2,3,4,5}}; // Allocating memory space
																	// for an array  of size double
																	//vars. First 5 will be initialized
																	//with 1,2,3,4,5, and the 
																	//rest will be 0's.
//nullptr check and use the allocated array
    if(p_scores){
        std::cout << "size of scores (it's a regular pointer) : " << sizeof(p_scores) << std::endl;
        std::cout << "Successfully allocated memory for scores."<< std::endl;
        
        //Print out elements. Can use regular array access notation, or pointer arithmetic
        for( size_t i{}; i < size ; ++i){
           std::cout << "value : " << p_scores[i] << " : " << *(p_scores + i) << std::endl; 
        }
    }

    delete [] p_salaries;
    p_salaries = nullptr;

    delete [] p_students;
    p_students = nullptr;

   delete [] p_scores;
   p_scores = nullptr;

   //Static arrays Vs dynamic arrays
   std::cout << "=====================================" << std::endl;

   int scores[10] {1,2,3,4,5,6,7,8,9,10}; // Lives on the stack

   std::cout << "scores size : " << std::size(scores) << std::endl;
   for( auto s : scores){
       std::cout << "value : " << s << std::endl;
   }

   int* p_scores1 = new int[10] {1,2,3,4,5,6,7,8,9,10}; // Lives on the heap.
   //std::cout << "p_scores1 size : " << std::size(p_scores) << std::endl;
   /*
   for( auto s : p_scores1){
       std::cout << "value : " << s << std::endl;
   }
   */
  


    std::cout << "Program ending well" << std::endl;

}
