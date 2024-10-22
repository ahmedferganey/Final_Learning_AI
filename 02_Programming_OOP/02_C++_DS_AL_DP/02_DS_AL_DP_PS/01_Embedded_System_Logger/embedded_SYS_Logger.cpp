#include <iostream>
#include <string>
#include <array>
#include <sstream>  // For std::ostringstream


/*
This application simulates a basic logger for an embedded system where strings are processed in a memory-efficient manner, using C-style functions for character manipulation.
*/


// Function declarations
void logMessage(std::ostringstream& buffer, const std::string& logType, int errorCode);
void copyLogMessage(std::string& dest, const std::string& source);
void searchKeyword(const std::string& log, const std::string& keyword);


std::ostringstream buffer;  // Use ostringstream for logging
std::string logCopy;        // Use std::string for log copy

int main(){

    // Log an error message
    logMessage(buffer, "ERROR", 404);

    // Copy the log message to another string
    copyLogMessage(logCopy, buffer.str());

    // Search for a keyword in the log
    searchKeyword(logCopy, "404");    

    return 0;

}

// Function to log a message with dynamic content using std::ostringstream
void logMessage(std::ostringstream& buffer, const std::string& logType, int errorCode) {
    buffer << "[" << logType << "] Error Code: " << errorCode;
    std::cout << buffer.str() << std::endl;
    // Removed clearing the buffer logic
    // buffer.str("");        // Clear the content of the buffer
    // buffer.clear();        // Reset the stream state   
}

// Function to safely copy a message into a buffer using std::string
void copyLogMessage(std::string& dest, const std::string& source) {
    dest = source; // Direct assignment is safe with std::string
    std::cout << "Log copied: " << dest << std::endl;
}

// Function to search for a specific keyword in log messages
void searchKeyword(const std::string& log, const std::string& keyword){
    if(log.find(keyword) != std::string::npos){
        std::cout << "Keyword '" << keyword << "' found in log!" << std::endl;
    }
    else{
        std::cout << "Keyword '" << keyword << "' not found in log." << std::endl;
    }
}