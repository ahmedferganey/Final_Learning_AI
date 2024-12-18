#include <iostream>
#include <string>
#include <cstdlib>
#include <filesystem>
#include <memory>
#include <cstdio>
#include <array>

using namespace std;

class FileOrganizer {
public:
    void organizeFiles(const string& directoryPath) {
        if (!std::filesystem::exists(directoryPath) || !std::filesystem::is_directory(directoryPath)) {
            std::cerr << "Directory does not exist: " << directoryPath << std::endl;
            return;
        }

        for (const auto& entry : std::filesystem::directory_iterator(directoryPath)) {
            // Logic for organizing files based on extension
            std::cout << "Processing file: " << entry.path() << "\n";
        }
    }

    void executeCommand(const std::string& command) {
        std::array<char, 128> buffer;
        std::string result;

        // Open the command for reading
        std::unique_ptr<FILE, decltype(&pclose)> pipe(popen(command.c_str(), "r"), pclose);
        if (!pipe) {
            std::cerr << "Failed to open pipe for command: " << command << std::endl;
            return;
        }

        // Read the output a line at a time
        while (fgets(buffer.data(), buffer.size(), pipe.get()) != nullptr) {
            result += buffer.data();
        }

        std::cout << "Command Output:\n" << result;
    }
};


int main(){

    FileOrganizer organizer;

    organizer.organizeFiles("/media/ferganey/Data/00_Main_Folder/02_Programming_OOP/02_C++_DS_AL_DP/00_basics_C++/12");
    string commandLine;
    cout << "Enter a command to execute (or 'exit' to quit): ";
    while (std::getline(std::cin, commandLine)) {
        if (commandLine == "exit") {
            break; // Exit the loop if the user types 'exit'
        }
        organizer.executeCommand(commandLine);
        std::cout << "\nEnter another command to execute (or 'exit' to quit): ";
    }

//////////////////////////////////////////////////////////////////////////////////////
    string command;
    std::cout << "Enter a command to get help (or 'exit' to quit): ";
/*
This function reads a line of text from std::cin (standard input) 
until it encounters a newline character (\n), or until the end of 
input (EOF) is reached.
The entire line of text (without the newline) is stored in the 
command variable, which is typically of type std::string.
std::getline returns true if a line was successfully read and 
false if the end of input is reached or an error occurs.
*/
    while (getline(cin, command)){
        if (command == "exit") break;

        string tldrcommand = "tldr " + command;
        system(tldrcommand.c_str()); // execute the command constructed in the previous step.
        std::cout << "\nEnter another command or 'exit': ";

    }
//////////////////////////////////////////////////////////////////////////////////////    
    return 0;

}
