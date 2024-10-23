#include <iostream>
#include <vector>
#include <cmath> 
#include <algorithm>
#include <numeric>

using namespace std;

/*******************************   Classes    ***************************8888 */
//base class for all classes
class Sensor{
    public:
        virtual void detect(){
        std::cout << "Detecting with generic sensor." << std::endl;
        }
        // method to process raw sensor data
        virtual void processData(const vector<int>& data){
        std::cout << "Processing generic sensor data." << std::endl;
        }
        // method to process filtered data
        virtual void processData(const vector<double>& filteredData){
            std::cout << "Processing filtered data." << std::endl;
        }
        virtual ~Sensor() = default; // virtual destructor for proper cleanup
};


// derived class for camera
class Camera : public Sensor{
    public:
        void detect() override{
            cout << "detecting objects with camera" << endl;
        }

        void processData(const vector<int>& imageData) override{
            cout << "processing camera data starting" << endl;
            for (size_t i = 1; i < imageData.size(); ++i){
                int edge = std::abs(imageData[i] - imageData[i-1]);
                if (edge > 10){ // threshold for detection
                    cout << "Edge detected between pixel" << i-1 << " and "  << i << std::endl;
                }
            }
        }
        // overriden method to process filtered camera data
        void processData(const vector<double>& filteredData) override{
            cout << "processing filtered camera data" << endl;
            if (filteredData.empty()){
                cout << "no data to process" << endl;
                return;
            }
            //  histogram simulation
            const int histogramSize = 256; // for pixel intensities from 0 to 256
            vector<int> histogram(histogramSize, 0);
            for (double value : filteredData){
                if(value >= 0 && value < histogramSize){
                    histogram[static_cast<int>(value)]++;
                }
            }
            // calculate mean and standard deviation
            double sum  = accumulate(filteredData.begin(), filteredData.end(), 0.0); 
            double mean = sum / filteredData.size();
            double sq_sum = inner_product(filteredData.begin(), filteredData.end(), filteredData.begin(), 0.0); //x^2 not x^2 - Mean
            double stdev = sqrt(sq_sum / filteredData.size() - mean*mean);

            // output histogram and statistics 
            cout << "histogram of pixels intensities" << endl;
            for (int i =0; i < histogramSize; ++i){
                if (histogram[i] > 0){
                    std::cout << "Intensity " << i << ": " << histogram[i] << std::endl;
                }
            }

            std::cout << "Mean pixel intensity: " << mean << std::endl;
            std::cout << "Standard deviation: " << stdev << std::endl;            
        }

};

// derived class for lidar
class lidar : public Sensor{
    public: 
        double calibrationoffset = 0.5; // calibration offset in meters
        double noiseThreshold = 0.1;    // noise threshold in meters

        void detect() override {
            std::cout << "Detecting distance with Lidar." << std::endl;
        }

        void processData(const vector<double>& distanceData) override {
            std::cout << "Processing Lidar data for distance measurement." << std::endl;

            // check if distance data is empty
            if (distanceData.empty()){
                cout << "no distance data to process" << endl;
                return;
            }
            vector<double> filteredDistance;

            // filter and calibration distances
            for (size_t i=0; i < distanceData.size(); ++i){
                double calibratedDistnace = distanceData[i] + calibrationoffset;

                // simple noise filter: ignore values that are withinh the noise threshold
                if (fabs(calibratedDistnace) > noiseThreshold && calibratedDistnace < 100){
                    // If both conditions are satisfied, the calibrated distance is considered
                    // valid and is added to the filteredDistances vector for further processing.
                    filteredDistance.push_back(calibratedDistnace);
                } else {
                    std::cout << "Ignored noisy or invalid measurement at index " << i << ": " << distanceData[i] << " meters" << std::endl;
                }
            }
            // if no valid distances after filtering, return 
            if (filteredDistance.empty()){
                std::cout << "No valid distances after filtering." << std::endl;
                return;
            }
            // Output the valid distance measurements
            for (size_t i = 0; i < filteredDistance.size(); ++i) {
                std::cout << "Filtered distance measurement " << i + 1 << ": " << filteredDistance[i] << " meters" << std::endl;
            }
        }

};

// derived class for ultrasonic
class ultrasonic : public Sensor{
    public:
        void detect() override {
            std::cout << "Detecting proximity with Ultrasonic sensor." << std::endl;
        }
        void processData(const vector<double>& distanceData) override {
            std::cout << "Processing Ultrasonic data for obstacle detection." << std::endl;
            for (size_t i = 0; i < distanceData.size(); ++i){
                if (distanceData[i] < 5){ // threshold for obstacle detection
                    std::cout << "Obstacle detected at index " << i << " within " << distanceData[i] << " meters!" << std::endl;
                }
            }
        }      
};

int main() {
    cout << "Hello from Project_1!" << endl;
/*

    // Step 1: Simulate image data capture (e.g., pixel intensity values) // gotten via CAN Bus
    vector<int> imageData = {100, 102, 98, 120, 110, 95, 115, 125, 130, 140};

    // Step 2: Instantiate the Camera object
    Camera camera;

    // Step 3: Detect objects (edges) in the image data
    camera.detect();

    // Step 4: Process the raw image data
    camera.processData(imageData);

    // Step 5: Simulate filtered data for further processing
    vector<double> filteredData = {100.5, 101.5, 98.0, 119.0, 109.5, 94.5, 114.0, 124.0, 129.0, 139.0};

    // Step 6: Process the filtered camera data
    camera.processData(filteredData);


    lidar lidar;
    lidar.detect();

    // Simulated distance data
    std::vector<double> distanceData = {10, 12, 15, 200, -5, 8, 25, 120, 50};

    // Process the distance data
    lidar.processData(distanceData);
*/

    Sensor* sensors[3];
    sensors[0] = new Camera();
    sensors[1] = new lidar();
    sensors[2] = new ultrasonic();

        // Simulated sensor data
    vector<double> imageData = {100, 102, 90, 115, 120}; // Simulated pixel values for camera
    vector<double> lidarData = {5, 6, 3, 200, 10}; // Distance measurements for lidar
    vector<double> ultrasonicData = {6, 3, 4, 2, 1}; // Proximity measurements for ultrasonic

    // Simulate detection and data processing
    for (int i =0; i < 3; ++i){
        sensors[i]->detect();
        switch(i){
            case 0:
                    sensors[i]->processData(imageData); // process camera data
                    break;
            case 1:  
                    sensors[i]->processData(lidarData); // process lidar Data
                    break;
            case 2: 
                    sensors[i]->processData(ultrasonicData); // process ultrasonic Data
                    break;
        }
    }

    for (int i=0; i<3; ++i){
        delete sensors[i];
    }

    return 0;
}
