#include <iostream>
#include <cctype>
#include <cstring> // Make sure you include this for strcmp
#include <iostream>
#include <string>
#include <cstdio> 
int main() {
    // Check if character is alphanumeric
    std::cout << "Checking std::isalnum:" << std::endl;
    std::cout << "C is alphanumeric: " << std::isalnum('C') << std::endl; // 1
    std::cout << "^ is alphanumeric: " << std::isalnum('^') << std::endl; // 0

    char input_char{'*'};
    if (std::isalnum(input_char)) {
        std::cout << input_char << " is alphanumeric." << std::endl;
    } else {
        std::cout << input_char << " is not alphanumeric." << std::endl;
    }

    // Check if character is alphabetic
    std::cout << "\nChecking std::isalpha:" << std::endl;
    std::cout << "e is alphabetic: " << std::isalpha('e') << std::endl; // 1
    std::cout << "^ is alphabetic: " << std::isalpha('^') << std::endl; // 0
    std::cout << "7 is alphabetic: " << std::isalpha('7') << std::endl; // 0

    if (std::isalpha('e')) {
        std::cout << 'e' << " is alphabetic." << std::endl;
    } else {
        std::cout << 'e' << " is NOT alphabetic." << std::endl;
    }

    // Check if a character is blank
    std::cout << "\nChecking std::isblank:" << std::endl;
    char message[] = "Hello there. How are you doing? The sun is shining.";
    std::cout << "Message: " << message << std::endl;

    size_t blank_count{};
    for (size_t i{0}; i < std::size(message); ++i) {
        if (std::isblank(message[i])) {
            std::cout << "Found a blank character at index: [" << i << "]" << std::endl;
            ++blank_count;
        }
    }
    std::cout << "In total, we found " << blank_count << " blank characters." << std::endl;

    // Check if character is lowercase or uppercase
    std::cout << "\nChecking std::islower and std::isupper:" << std::endl;
    char thought[] = "The C++ Programming Language is one of the most used on the Planet";
    size_t lowercase_count{};
    size_t uppercase_count{};

    std::cout << "Original string: " << thought << std::endl;

    for (auto character : thought) {
        if (std::islower(character)) {
            std::cout << " " << character;
            ++lowercase_count;
        }
        if (std::isupper(character)) {
            ++uppercase_count;
        }
    }
    std::cout << std::endl;
    std::cout << "Found " << lowercase_count << " lowercase characters and "
              << uppercase_count << " uppercase characters." << std::endl;

    // Check if a character is a digit
    std::cout << "\nChecking std::isdigit:" << std::endl;
        char statement[] = "Mr Hamilton owns 221 cows. That's a lot of cows! The kid exclaimed.";
    std::cout << "Statement: " << statement << std::endl;

    size_t digit_count{};
    for (auto character : statement) {
        if (std::isdigit(character)) {
            std::cout << "Found digit: " << character << std::endl;
            ++digit_count;
        }
    }
    std::cout << "Found " << digit_count << " digits in the statement string." << std::endl;

    // Turning a character to lowercase using std::tolower() and to uppercase using std::toupper()
    std::cout << "\nTransforming characters with std::tolower and std::toupper:" << std::endl;
    char original_str[] = "Home. The feeling of belonging";
    char dest_str[std::size(original_str)];

    // Convert to uppercase
    for (size_t i{}; i < std::size(original_str); ++i) {
        dest_str[i] = std::toupper(original_str[i]);
    }
    std::cout << "Original string: " << original_str << std::endl;
    std::cout << "Uppercase string: " << dest_str << std::endl;

    // Convert to lowercase
    for (size_t i{}; i < std::size(original_str); ++i) {
        dest_str[i] = std::tolower(original_str[i]);
    }
    std::cout << "Lowercase string: " << dest_str << std::endl;
////////////////////////////////////////////////////////////////////

    // std::strlen : Find the length of a string
    // Real arrays and those decayed into pointers
    const char message1[] {"The sky is blue."};
	
    // Array decays into pointer when we use const char*
    const char* message2 {"The sky is blue."};
    std::cout << "message1 : " << message1 << std::endl;
	
    // strlen ignores the null character, calculates the length excluding it
    std::cout << "strlen(message1) : " << std::strlen(message1) << std::endl;
	
    // sizeof includes the null character for arrays
    std::cout << "sizeof(message1) : " << sizeof(message1) << std::endl;
	
    // strlen still works with decayed arrays (pointers)
    std::cout << "strlen(message2) : " << std::strlen(message2) << std::endl;
	
    // Prints the size of the pointer itself, not the string length
    std::cout << "sizeof(message2) : " << sizeof(message2) << std::endl;

    // std::strcmp: Compares two C-style strings lexicographically
    std::cout << std::endl;
    std::cout << "std::strcmp : " << std::endl;

    const char* string_data1{ "Alabama" };
    const char* string_data2{ "Blabama" };

    char string_data3[]{ "Alabama" };
    char string_data4[]{ "Blabama" };

    // Comparing two strings
    std::cout << "std::strcmp (" << string_data1 << "," << string_data2 << ") : "
        << std::strcmp(string_data1, string_data2) << std::endl;

    std::cout << "std::strcmp (" << string_data3 << "," << string_data4 << ") : "
        << std::strcmp(string_data3, string_data4) << std::endl;

    // Changing the values of string_data1 and string_data2
    string_data1 = "Alabama";
    string_data2 = "Alabamb";
    std::cout << "std::strcmp (" << string_data1 << "," << string_data2 << ") : "
        << std::strcmp(string_data1, string_data2) << std::endl;

    string_data1 = "Alacama";
    string_data2 = "Alabama";
    std::cout << "std::strcmp (" << string_data1 << "," << string_data2 << ") : "
        << std::strcmp(string_data1, string_data2) << std::endl;

    string_data1 = "India";
    string_data2 = "France";
    std::cout << "std::strcmp (" << string_data1 << "," << string_data2 << ") : "
        << std::strcmp(string_data1, string_data2) << std::endl;

    string_data1 = "Kigali";
    string_data2 = "Kigali";
    std::cout << "std::strcmp (" << string_data1 << "," << string_data2 << ") : "
        << std::strcmp(string_data1, string_data2) << std::endl;


    // std::strncmp: Compares first 'n' characters of two strings
    size_t n{3};
    std::cout << std::endl;
    std::cout << "std::strncmp : " << std::endl;
    std::cout << "std::strncmp (" << string_data1 << "," << string_data2 << "," << n << ") : " 
              << std::strncmp(string_data1,string_data2,n) << std::endl;
              
    string_data1 = "aaaia";
    string_data2 = "aaance";
    
    std::cout << "std::strncmp (" << string_data1 << "," << string_data2 << "," << n << ") : " 
              << std::strncmp(string_data1,string_data2,n) << std::endl;

    n = 5;
    
    std::cout << "std::strncmp (" << string_data1 << "," << string_data2 << "," << n << ") : " 
              << std::strncmp(string_data1,string_data2,n) << std::endl;
              
    string_data1 = "aaaoa";
    string_data2 = "aaance";
    std::cout << "std::strncmp (" << string_data1 << "," << string_data2 << "," << n << ") : " 
              << std::strncmp(string_data1,string_data2,n) << std::endl;


    // Find the first occurrence of a character in a string using std::strchr
    std::cout << std::endl;
    std::cout << "std::strchr : " << std::endl;

    const char * const str { "Try not. Do, or do not. There is no try."};
    char target = 'T';
    const char *result = str;
    size_t iterations{};
	
    while ((result = std::strchr(result, target)) != nullptr) {
        std::cout << "Found '" << target
                  << "' starting at '" << result << "'\n";
        ++result; // Move to next character
        ++iterations;
    }
    std::cout << "iterations : " << iterations << std::endl;


    // Find the last occurrence of a character using std::strrchr
    std::cout << std::endl;
    std::cout << "std::strrchr : " << std::endl;

    char input[] = "/home/user/hello.cpp";
    char* output = std::strrchr(input, '/');
    if(output)
        std::cout << output + 1 << std::endl; // +1 to skip the '/' and print the file name
///////////////////////////////////////////////////////////
    // Concatenation using std::strcat
    std::cout << "\nstd::strcat:" << std::endl;
    char dest[50] = "Hello ";
    char src[50] = "World!";
    
    // Concatenating strings
    std::strcat(dest, src);
    std::cout << "After strcat: " << dest << std::endl; // Hello World
    
    std::strcat(dest, " Goodbye World!");
    std::cout << "After second strcat: " << dest << std::endl; // Hello World Goodbye World!

    // More concatenation using dynamic memory
    std::cout << "\nMore std::strcat:" << std::endl;
    char* dest1 = new char[30]{'F','i','r','e','l','o','r','d','\0'};
    char* source1 = new char[30]{',','T','h','e',' ','P','h','e','n','i','x',' ','K','i','n','g','!','\0'};

    std::cout << "Before concatenation: dest1: " << dest1 << " | source1: " << source1 << std::endl;
    std::strcat(dest1, source1);
    std::cout << "After strcat: dest1: " << dest1 << std::endl;

    // Clean up dynamic memory
    delete[] dest1;
    delete[] source1;

    // std::strncat: Concatenates n characters from src to dest
    std::cout << "\nstd::strncat:" << std::endl;
    char dest2[50] = "Hello";
    char source2[30] = " There is a bird on my window";
    
    std::cout << std::strncat(dest2, source2, 6) << std::endl; // Concatenates first 6 chars
    std::cout << "The concatenated string is: " << dest2 << std::endl;

    // std::strcpy: Copying strings
    std::cout << "\nstd::strcpy:" << std::endl;
    const char* source3 = "C++ is a multipurpose programming language.";
    char* dest3 = new char[std::strlen(source3) + 1]; // +1 for the null character
    
    std::strcpy(dest3, source3);
    std::cout << "dest3: " << dest3 << std::endl;

    // Clean up dynamic memory
    delete[] dest3;

    // std::strncpy: Copying n characters from src to dest
    std::cout << "\nstd::strncpy:" << std::endl;
    const char* source4 = "Hello";
    char dest4[10] = "abcdef"; // Initialize with some data

    std::cout << "Before strncpy, dest4: " << dest4 << std::endl;
    std::strncpy(dest4, source4, 5);
    dest4[5] = '\0'; // Ensure null termination

    std::cout << "After strncpy, dest4: " << dest4 << std::endl;

//////////////////////////////////////////////
    // String initialization
    std::string greeting{"Hello, "};
    std::string name{"World!"};
    
    // Concatenation
    std::string message1112 = greeting + name;
    std::cout << message1112 << std::endl; // Hello, World!

    // Modifying strings
    message1112[7] = 'C'; // Change 'W' to 'C'
    std::cout << message1112 << std::endl; // Hello, Corld!

    // Clearing the string
    message1112.clear();
    std::cout << "Cleared message: " << message1112 << " (size: " << message1112.size() << ")" << std::endl;

    // Inserting text
    message1112.insert(0, "Hello, World!");
    std::cout << "Inserted message: " << message1112 << std::endl; // Hello, World!



    //Use a raw array
    std::string planet {"Earth. Where the sky is blue"};//Initialize with string literal    
    planet = "Earth. Where the sky is blue Earth. Where the sky is blue Earth. Where ";    
    const char * planet1 {"Earth. Where the sky is blue Earth."};
    /*
Here, planet1 is a pointer to a constant character array (string literal)
 that is initialized with "Earth. Where the sky is blue Earth.".
  The const char* type indicates that the string literal cannot be modified.    
     */
    planet1 = "Earth. Where the sky is blue Earth. Where the sky is blue Earth. Where ";
    /*
This line attempts to reassign the pointer planet1 to point to a different string literal. 
This is valid because planet1 is a pointer to a constant character array, allowing it 
to point to different string literals.    
    */
    std::cout << "planet1 : " << planet1 << std::endl;
///////////////////////////////////////////////////////////////////////

    using namespace std::string_literals; // For 's' suffix
    std::cout << "str8: " << "Hello"s + " World" << std::endl;
        // Using append method
    std::string st{"hello"};
    std::string st3 = st.append(" world");
    // Advanced append
    std::string str16{"The world is our shared home."};
    std::cout << "Direct output: " << st3.append(str16, 4, 5) << std::endl;   
    const char* message13423 = "World"; 
    std::cout << "\nAppending C-Strings: " << std::string{"Hello "} + message13423 << std::endl;
    // Concatenating std::strings and numbers
    std::string str26{"Hello"};
    str26 += std::to_string(67.5f);
    std::cout << "str26: " << str26 << std::endl;
///////////////////////////////////////////////////////////////////////////////////
    // Initialize string
    std::string str1{"Hello there"};

    // Size of the string
    std::cout << "str1.size(): " << str1.size() << std::endl;

    // Reading characters using a for loop
    std::cout << "\nUsing for loop: ";
    for (size_t i = 0; i < str1.size(); ++i) {
        std::cout << str1[i] << " ";
    }
    std::cout << std::endl;

    // Reading characters using a range-based for loop
    std::cout << "Using range-based for loop: ";
    for (char value : str1) {
        std::cout << value << " ";
    }
    std::cout << std::endl;

    // Using at() method to read characters
    std::cout << "\nUsing std::string::at(): ";
    for (size_t i = 0; i < str1.size(); ++i) {
        std::cout << str1.at(i) << " ";
    }
    std::cout << std::endl;

    // Modifying characters using operator[] and at()
    str1[0] = 'B';
    str1.at(1) = 'a';
    std::cout << "Modified str1: " << str1 << std::endl;

    // Getting front and back characters
    std::string str2{"The Phoenix King"};
    char& front_char = str2.front();
    char& back_char = str2.back();
    std::cout << "\nFront char in str2: " << front_char << ", Back char in str2: " << back_char << std::endl;

    front_char = 'r';
    back_char = 'd';
    std::cout << "Modified str2: " << str2 << std::endl;

    // Using c_str() method
    const char* wrapped_c_string = str2.c_str();
    std::cout << "\nWrapped C string: " << wrapped_c_string << std::endl;
    
    
  std::string greeting213 = "Hello, World!";

    // Using std::cout to print the std::string directly
    std::cout << "Using std::cout: " << greeting213 << std::endl;


    // Using c_str() to get a C-style string
    const char* cStrGreeting = greeting213.c_str();
    // Using printf to print the C-style string
    printf("Using printf: %s\n", cStrGreeting);



    // Using data() method
    std::string str3{"Hello World"};
    char* data = str3.data();
    std::cout << "\nWrapped C string: " << data << std::endl;

    // Modifying using data()
    data[0] = 'B';
    std::cout << "Wrapped C string (after modification): " << data << std::endl;
    std::cout << "Original string (after modification): " << str3 << std::endl;




    return 0;
}
