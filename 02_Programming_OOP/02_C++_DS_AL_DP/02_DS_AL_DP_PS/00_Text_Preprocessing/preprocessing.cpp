#include <iostream>
#include <string>
#include <cstring>
#include <cctype>
#include <regex>
#include <vector>


/*

This example is a basic text preprocessing pipeline typically used in AI or NLP tasks such as sentiment analysis, machine translation, or text classification.

*/



// Function declarations
std::string tolowercase(const std::string& input);
std::string removepunctuation(const std::string& input);
std::vector<std::string> tokenize(const std::string& input);
std::string findandreplace(std::string input, const std::string& tofind, const std::string& toreplace);


std::string sentence = "Hello, World! This is a test sentence. AI is the future!";


int main(){


    // Step 1: Convert to lowercase
    sentence = tolowercase(sentence);
    std::cout << "Lowercase: " << sentence << std::endl;

    // Step 2: Remove punctuation
    sentence = removepunctuation(sentence);
    std::cout << "No punctuation: " << sentence << std::endl;

    // Step 3: Tokenize the sentence
    std::vector<std::string> tokens = tokenize(sentence);
    std::cout << "Tokens: ";
    for (const std::string& token : tokens) {
        std::cout << token << " ";
    }
    std::cout << std::endl;

    // Step 4: Find and replace a word (e.g., "test" -> "sample")
    sentence = findandreplace(sentence, "test", "sample");
    std::cout << "Replaced: " << sentence << std::endl;


    return 0;

}


// Function to convert string to lowercase
std::string tolowercase(const std::string& input){
    std::string result = input;
    for (char& ch :result){
        ch = std::tolower(ch);
    }
    return result;
}

// Function to remove punctuation using regex
std::string removepunctuation(const std::string& input){
    // This line creates a regex object named punctuation.
    //The double backslash (\\) is used to escape the dot 
    //in C++ strings because a single backslash is treated 
    //as an escape character in string literals.
    // '\\.' matches a literal dot (.).
    std::regex punctuation("[\\.,!?;:]");
    return std::regex_replace(input, punctuation, "");
}

// Function to tokenize a string
std::vector<std::string> tokenize(const std::string& input){
    //The function is declared to return a std::vector<std::string>, 
    //which is a dynamic array that will store the tokens.
    std::vector<std::string> tokens; // Initially, this vector is empty and will dynamically resize as tokens are added.
    std::istringstream stream(input); // An std::istringstream object named stream is created and initialized with the input string.
    std::string token; // A string variable named token is declared to temporarily hold each token as it is extracted from the stream.
    while (stream >> token){ // Read tokens separated by whitespace

        /*
        >> The >> operator is overloaded for std::istringstream (and other input streams) to facilitate reading data.
When using stream >> token, the extraction operator works as follows:
        It skips any leading whitespace characters (spaces, tabs, newlines).
        It reads characters from the stream until it encounters the next whitespace character, which indicates the end of the current token.
The characters read are then stored in the token variable as a std::string.        
        */

        tokens.push_back(token);
    }
    return tokens;
}

// Function to find and replace a word in a string
std::string findandreplace (std::string input, const std::string& tofind, const std::string& toreplace){
    /*
The function returns a std::string.
It takes three parameters:
        input: The original string where the search and replace will occur. It is passed by value, so a copy is made, allowing for modifications without affecting the original string.
        const std::string& toFind: A constant reference to the substring that needs to be found in the input string. This avoids unnecessary copying.
        const std::string& toReplace: A constant reference to the substring that will replace occurrences of toFind.    
    */
   size_t pos = input.find(tofind);
   /*
find returns the index of the first character of the found substring, or std::string::npos if it is not found. size_t is an unsigned integer type suitable for indexing.   
   */
   while(pos != std::string::npos){
    /*
std::string::npos is defined as static const size_t npos = -1;. Since size_t is an unsigned integer type, using -1 effectively sets all bits to 1, giving the maximum possible value for that type.
This value is used to indicate "not found" when searching within a string.    
    */
        input.replace(pos, tofind.length(), toreplace);  // Step 3: Replace the found substring and update pos
        pos = input.find(tofind, pos + toreplace.length()); // Step 4: Search for the next occurrence
// when It does not find "tofind" anymore, so pos is set to std::string::npos ---> -1.

   }
   return input;

}