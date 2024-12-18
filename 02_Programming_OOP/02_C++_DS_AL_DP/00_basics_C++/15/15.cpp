#include <iostream>
#include <string>
#include <array>
#include <vector>
using namespace std;
/* Sensor data managememt application*/

// define enum class for different sensor types
enum class SensorType{
        LIDAR,
        CAMERA,
        RADAR,
        UNKNOWN
};

// structure to hold sensor data
struct SensorData{
    SensorType type;
    array<unsigned int, 10> readings; // use unsigned for distance measurement

    // constructor initializes readings to zero
    SensorData(SensorType SensorType) : type(SensorType){
        readings.fill(0); // initilize readings to zero
    }
};

// class to manage multiple sensors
class SensorManager{
    private:
        vector<SensorData> sensors; // store multiple sensors
    
    public:
        // method to add new sesnor
        void addSensor(SensorType type){
            sensors.emplace_back(type); // Add new sesnor data
        }

        // method to update sensor data using const ref to ensure no modifications
        void updateSensorData(size_t sensorIndex, const array<unsigned int, 10>& newReadings){
            if (sensorIndex < sensors.size()){
                sensors[sensorIndex].readings = newReadings;
            }else{
                cerr << "Error: invalid sensor index" <<endl;
            }
        }
        // method to process sensor sensor data and check for obstacles
        void processSensorData(const unsigned int threshold) const {
            for (const auto& sensor : sensors){
                cout << "sensor type: " << static_cast<int>(sensor.type) << endl;
                for (const auto& reading : sensor.readings){
                    if (reading < threshold){
                        cout << "Obstacle detected at distance: " << reading << "meters" << endl;
                    } else{
                        cout << "No obstacles within range." << endl;
                    }
                }
                cout << endl;
            
            }
        }
};

int main(){
    SensorManager manager;

    manager.addSensor(SensorType::LIDAR);
    manager.addSensor(SensorType::CAMERA);
    manager.addSensor(SensorType::RADAR);

    // sample readings using unsigned integers for distances
    std::array<unsigned int, 10> lidarReadings = {5, 3, 2, 8, 1, 6, 10, 4, 2, 0};
    std::array<unsigned int, 10> cameraReadings = {15, 12, 1, 8, 0, 20, 14, 7, 10, 2};
    std::array<unsigned int, 10> radarReadings = {7, 9, 4, 11, 3, 2, 12, 6, 5, 8};
    // Updating sensor data using const reference
    manager.updateSensorData(0, lidarReadings);
    manager.updateSensorData(1, cameraReadings);
    manager.updateSensorData(2, radarReadings);

    // Process sensor data with a threshold of 4 meters
    manager.processSensorData(4);
    return 0;
}
