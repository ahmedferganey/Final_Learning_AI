#include <iostream>
#include <string>
#include <optional>
#include <map>

using namespace std;

// Enumeration for vehicle commands
enum class Command {
    Start,
    Stop,
    Accelerate,
    Decelerate,
    Quit,
    Invalid
};

// Function to map user input strings to Command enum values
Command getCommandFromInput(const std::string& input) {
    static const std::map<std::string, Command> commandMap = {
        {"start", Command::Start},
        {"stop", Command::Stop},
        {"accelerate", Command::Accelerate},
        {"decelerate", Command::Decelerate},
        {"quit", Command::Quit}
    };
    auto it = commandMap.find(input);
    return (it != commandMap.end()) ? it->second : Command::Invalid;
    /*
            it != commandMap.end()
If it is not equal to commandMap.end(), it indicates that the input 
string was found in the map.    
                it->second 
refers to the value in the map corresponding to the found key.
    */
}

// Class representing the vehicle's control interface
class VehicleControlInterface {
private:
    bool isRunning = false;       // Track vehicle state
    float speed = 0.0f;           // Vehicle speed in m/s

public:
    // Display available commands to the user
    void displayCommands() const {
        std::cout << "\nAvailable Commands:\n"
                  << "  start      - Start the vehicle\n"
                  << "  stop       - Stop the vehicle\n"
                  << "  accelerate - Increase speed by 5 m/s\n"
                  << "  decelerate - Decrease speed by 5 m/s\n"
                  << "  quit       - Exit the interface\n"
                  << "Enter command: ";
    }
    // Process commands based on user input
    void processCommand(const Command& command) {
        if (command == Command::Start && !isRunning) {
            isRunning = true;
            std::cout << "Vehicle started. Current speed: " << speed << " m/s\n";
        } else if (command == Command::Stop && isRunning) {
            isRunning = false;
            speed = 0;
            std::cout << "Vehicle stopped.\n";
        } else if (command == Command::Accelerate && isRunning) {
            speed += 5.0f;
            std::cout << "Accelerating. Current speed: " << speed << " m/s\n";
        } else if (command == Command::Decelerate && isRunning && speed > 0) {
            speed -= 5.0f;
            std::cout << "Decelerating. Current speed: " << speed << " m/s\n";
            if (speed <= 0) {
                speed = 0;
                std::cout << "Vehicle has come to a stop.\n";
            }
        } else if (command == Command::Quit) {
            std::cout << "Exiting vehicle control interface.\n";
        } else if (command == Command::Invalid) {
            std::cout << "Invalid command. Please try again.\n";
        } else {
            std::cout << "Command not available in the current state.\n";
        }
    }
};

int main(){
    VehicleControlInterface vehicleControl;
    string input;

    cout << "Welcome to the Autonomous Vehicle Control Interface!\n";
    while(true){
        vehicleControl.displayCommands();

        getline(cin, input);

        Command command = getCommandFromInput(input);

        if (command == Command::Quit){
            vehicleControl.processCommand(command);
            break;
        }
        vehicleControl.processCommand(command);
    }

    return 0;
}
