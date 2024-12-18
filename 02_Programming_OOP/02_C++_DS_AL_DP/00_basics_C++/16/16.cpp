#include <iostream>
#include <array>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <optional>
#include <filesystem>
#include <fstream>
using namespace std;

/* 7. Autonomous Vehicle Path Planning and Traffic Light Recognition */

// constants for grid size and traffic light states
constexpr int GRID_SIZE =5; // grid size for path planning
constexpr array TRAFFIC_LIGHT_STATES = {"RED", "YELLOW", "GREEN"};

// structure to represent the vehicle state
struct VehicleState{
    float speed; // meters per second
    float batteryLevel; // as a percentage

    // constructor to initilize vehicle state
    VehicleState(float s, float b) : speed(s), batteryLevel(b){} 
};



// class for path planning and traffic ligh recognition
class AutonomousVehicle{
    private:
        array<array<int, GRID_SIZE>, GRID_SIZE> grid;
        VehicleState state;
        optional<filesystem::path> logFilePath; // Optional log file path
    
        // Helper to enumerate container indices
        template<typename T>
        auto enumerate(const T& container) const {
            std::vector<std::pair<size_t, typename T::value_type>> indexed;
            size_t index = 0;
            for (const auto& value : container) {
                indexed.emplace_back(index++, value);
            }
            return indexed;
        }
    public:
        // Constructor initializes state and grid, with an optional log file
        AutonomousVehicle(float speed, float batteryLevel, std::optional<std::filesystem::path> logPath = {})
            : state(speed, batteryLevel), logFilePath(logPath) 
        {
            for (int i = 0; i < GRID_SIZE; ++i)
                for (int j = 0; j < GRID_SIZE; ++j)
                    grid[i][j] = (i + j) % 2; // Simple path setup
        }

        // Display vehicle state
        void displayState() const {
            std::cout << "Vehicle Speed: " << state.speed << " m/s\n";
            std::cout << "Battery Level: " << state.batteryLevel << "%\n";
        }

        // Find optimal path (returns a string representation of the path)
        std::string findOptimalPath() const {
            std::ostringstream pathLog;
            for (const auto& [i, row] : enumerate(grid)) {
                for (const auto& [j, cell] : enumerate(row)) {
                    if (cell == 0) { // Free path
                        pathLog << "(" << i << ", " << j << ") -> ";
                    }
                }
            }
            string path = pathLog.str(); // convert the accumulated path to a standard string (path).
            if (!path.empty()) {
                path.erase(path.end() - 4); // Removeremoves the last four characters from the path string.
            /*
            1 0 1 0 1
            0 1 1 1 0
            1 1 0 1 1
            0 1 1 0 1
            1 0 1 1 1

"(0, 1) -> (0, 3) -> (1, 0) -> (1, 4) -> (2, 2) -> (3, 0) -> (3, 3) -> (4, 1)"
            
            */
            }
            return path;
        }
    // Traffic light recognition
        void recognizeTrafficLights(const std::array<std::string, 3>& lights) const {
            std::string trafficReport;
            for (const auto& light : lights) {
                if (light == TRAFFIC_LIGHT_STATES[0]) {
                    trafficReport += "Traffic Light: RED - Stop!\n";
                } else if (light == TRAFFIC_LIGHT_STATES[1]) {
                    trafficReport += "Traffic Light: YELLOW - Prepare to stop.\n";
                } else if (light == TRAFFIC_LIGHT_STATES[2]) {
                    trafficReport += "Traffic Light: GREEN - Go!\n";
                } else {
                    trafficReport += "Unknown traffic light state!\n";
                }
            }
            std::cout << trafficReport;
        }
        // Generate a detailed vehicle report and log it
        string generateVehicleReport() const {
            ostringstream report;
            report << "Vehicle State Report:\n";
            report << "Speed: " << state.speed << " m/s\n";
            report << "Battery Level: " << state.batteryLevel << "%\n";
            report << "Optimal Path: " << findOptimalPath() << "\n";            

            if (logFilePath){
                ofstream logfile(logFilePath.value(), ios::app);
                logfile << report.str();
            }
            return report.str();
        }

};

int main(){
    optional<filesystem::path> logPath{"/media/ferganey/Data/00_Main_Folder/02_Programming_OOP/02_C++_DS_AL_DP/00_basics_C++/16/vehicle_log.txt"};
    AutonomousVehicle vehicle(20.5f, 75.0f, logPath);

    // Display the vehicle's current state
    vehicle.displayState();

    // Generate and display a detailed vehicle report
    std::string report = vehicle.generateVehicleReport();
    std::cout << report;

    // Simulate recognizing traffic lights
    std::array<std::string, 3> trafficLights = {"GREEN", "RED", "YELLOW"};
    vehicle.recognizeTrafficLights(trafficLights);

}
