#include <iostream>

#include <string>
#include <cstring>
int main(){
    // Initialize strings
    std::string greeting{"Hello World"};
    std::string emptyStr; // Empty string
    std::string defaultStr{}; // Default-constructed empty string

    // Check if strings are empty
    std::cout << std::boolalpha; // To print bool as true/false
    std::cout << "\nEmpty status:\n";
    std::cout << "greeting is empty: " << greeting.empty() << "\n";
    std::cout << "emptyStr is empty: " << emptyStr.empty() << "\n";
    std::cout << "defaultStr is empty: " << defaultStr.empty() << "\n";

    // Size and length of strings
    std::cout << "\nSize and Length:\n";
    std::cout << "greeting contains " << greeting.size() << " characters\n";
    std::cout << "emptyStr contains " << emptyStr.size() << " characters\n";
    std::cout << "defaultStr contains " << defaultStr.size() << " characters\n";
    std::cout << "greeting length: " << greeting.length() << "\n";

    // Max size of string
    std::cout << "\nMax size:\n";
    std::cout << "std::string can hold " << greeting.max_size() << " characters\n";

    // Capacity of strings
    std::cout << "\nCapacity:\n";
    std::cout << "greeting capacity: " << greeting.capacity() << "\n";
    std::cout << "emptyStr capacity: " << emptyStr.capacity() << "\n";

    greeting = "The sky is so blue, the grass is green. Kids are running all over the place";
    std::cout << "Updated greeting size: " << greeting.size() << ", capacity: " << greeting.capacity() << "\n";

    // Reserve and shrink_to_fit
    greeting.reserve(100);
    std::cout << "\nAfter reserve:\n";
    std::cout << "greeting capacity: " << greeting.capacity() << ", size: " << greeting.size() << "\n";

    greeting.shrink_to_fit();
    std::cout << "After shrink_to_fit:\n";
    std::cout << "greeting capacity: " << greeting.capacity() << ", size: " << greeting.size() << "\n";
/////////////////////////////////////////////////////////////////////
   // Clear: Removes all characters from the string.
    std::string sentence {"The Lion Dad"};
    sentence.clear();

    // Insert (1)
    std::string numString {"122"};
    numString.insert(1, 4, '3'); // Count can be 1, 2, 5, ..

    // Insert (2)
    std::string greetingg {"Hello!"};
    const char* addition {" World"};
    greetingg.insert(5, addition);

    // Insert (3)
    std::string phrase {"Hello!"};
    const char* extraText {" World Health Organization"};
    phrase.insert(5, extraText, 6);

    // Insert (4)
    std::string additional {" World"};
    std::string salutation {"Hello!"};
    salutation.insert(5, additional);

    // Insert (5)
    std::string initial {"Hello!"};
    std::string analysis {"Statistical Analysis of the World Population."};
    initial.insert(5, analysis, 27, 6);

    // Erase
    std::string message {"Hello World is a message used to start off things when learning programming!"};
    message.erase(11, message.size() - 12);
    
    // Reset message.
    message = "Hello World is a message used to start off things when learning programming!";
    message.erase(11, message.size() - 12);

    // push_back
    std::string exclamation {"Hello World"};
    exclamation.push_back('!');

    // pop_back
    std::string doubleExclamation {"Hello World!!"};
    doubleExclamation.pop_back();

    // Print statements
    std::cout << "sentence: " << sentence << std::endl;
    std::cout << "numString: " << numString << std::endl; // 1322
    std::cout << "greeting: " << greeting << std::endl; // Hello World!
    std::cout << "phrase: " << phrase << std::endl; // Hello World!
    std::cout << "initial: " << initial << std::endl; // Hello Statistical
    std::cout << "message: " << message << std::endl; // Hello World
    std::cout << "exclamation: " << exclamation << std::endl; // Hello World!
    std::cout << "doubleExclamation: " << doubleExclamation << std::endl; // Hello World!
////////////////////////////////////////////////////////////////////////////
   std::string hello_str{"Hello"};
    std::string bello_str{"Bello"};
    
    // Variables for storing comparison results
    bool cmp_eq = (hello_str == bello_str);
    bool cmp_neq = (hello_str != bello_str);
    bool cmp_gt = (hello_str > bello_str);
    bool cmp_ge = (hello_str >= bello_str);
    bool cmp_lt = (hello_str < bello_str);
    bool cmp_le = (hello_str <= bello_str);

    const char* c_string1 {"Bello"};
    hello_str = "Hello";
    
    size_t hello_size = hello_str.size();
    size_t c_string_size = std::strlen(c_string1);
    bool c_str_cmp_eq = (hello_str == c_string1);
    bool c_str_cmp_neq = (c_string1 == hello_str);
    bool c_str_cmp_ge = (c_string1 >= hello_str);
    bool c_str_cmp_lt = (c_string1 < hello_str);

    hello_str = "hello";
    const char hello_char_array[] {'h','e','l','l','o','\0'};
    bool char_array_cmp = (hello_str == hello_char_array);

    // Print all results at the end
    std::cout << std::endl;
    std::cout << "Comparing with comparison operators : " << std::endl;
    std::cout << std::boolalpha;
    std::cout << hello_str << "==" << bello_str << " : " << cmp_eq << std::endl; // false
    std::cout << hello_str << "!=" << bello_str << " : " << cmp_neq << std::endl; // true
    std::cout << hello_str << ">" << bello_str << " : " << cmp_gt << std::endl; // true
    std::cout << hello_str << ">=" << bello_str << " : " << cmp_ge << std::endl; // true
    std::cout << hello_str << "<" << bello_str << " : " << cmp_lt << std::endl; // false
    std::cout << hello_str << "<=" << bello_str << " : " << cmp_le << std::endl; // false

    std::cout << "hello_str.size() : " << hello_size << std::endl;
    std::cout << "std::strlen(c_string1) : " << c_string_size << std::endl;
    std::cout << hello_str << "==" << c_string1 << " (C-String) : " << c_str_cmp_eq << std::endl; // false
    std::cout << c_string1 << " (C-String) ==" << hello_str << " : " << c_str_cmp_neq << std::endl; // false
    std::cout << c_string1 << " (C-String) >=" << hello_str << " : " << c_str_cmp_ge << std::endl; // false
    std::cout << c_string1 << " (C-String) <" << hello_str << " : " << c_str_cmp_lt << std::endl; // true

    std::cout << hello_str << "== hello_char_array : " << char_array_cmp << std::endl;

///////////////////////////////////////////////////////
   // Replacing (1)
    std::string str1{"Finding Nemo"}; // Replace Finding with 'Searching For'
    std::string str1_2{"Searching For"};
    
    std::cout << "Original str1: " << str1 << std::endl; // Output: Finding Nemo
    str1.replace(0, 7, str1_2);
    std::cout << "After replacement str1: " << str1 << std::endl; // Output: Searching For Nemo

    // Copying
    std::string str4{"Climbing Kirimanjaro"};
    char txt4[15]{}; // Initialized with zero equivalent for characters which is '\0'
    
    std::cout << "Copying..." << std::endl;
    str4.copy(txt4, 11, 9);
    std::cout << "txt4 (copied text): " << txt4 << std::endl; // Output: Kirimanj

    // Swapping
    std::string str_a{"This is a string stored in A"};
    std::string str_b{"This is a string stored in B and it's really great to be able to do that."};
    
    std::cout << "Before swap str_a: " << str_a << std::endl; // Output: This is a string stored in A
    std::cout << "Before swap str_b: " << str_b << std::endl; // Output: This is a string stored in B and it's really great to be able to do that.
    
    str_a.swap(str_b);
    
    std::cout << "After swap str_a: " << str_a << std::endl; // Output: This is a string stored in B and it's really great to be able to do that.
    std::cout << "After swap str_b: " << str_b << std::endl; // Output: This is a string stored in A
////////////////////////////////////

}
