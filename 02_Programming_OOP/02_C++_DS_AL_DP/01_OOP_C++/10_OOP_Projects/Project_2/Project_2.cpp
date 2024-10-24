// #include <opencv2/opencv.hpp>
// #include <opencv2/dnn.hpp>
// #include <iostream>
// #include <vector>

// // Include OpenCV and TensorFlow libraries for AI processing
// using namespace cv;
// using namespace cv::dnn;

// class Camera : public Sensor {
// public:
//     bool obstacleDetected = false;

//     // Load a pre-trained object detection model
//     Net net = readNetFromTensorflow("frozen_inference_graph.pb", "graph.pbtxt");

//     void detect() override {
//         std::cout << "Detecting objects with camera using AI" << std::endl;

//         // Simulated image for AI processing
//         Mat image = imread("input_image.jpg");

//         // Preprocess the image for AI model
//         Mat blob = blobFromImage(image, 1.0, Size(300, 300), Scalar(127.5, 127.5, 127.5), true, false);
//         net.setInput(blob);

//         // Run the AI model
//         Mat detections = net.forward();

//         // Process the AI detections
//         for (int i = 0; i < detections.rows; ++i) {
//             float confidence = detections.at<float>(i, 2);

//             if (confidence > 0.5) {  // Threshold for detection
//                 int objectClass = detections.at<float>(i, 1);
//                 int xLeftBottom = static_cast<int>(detections.at<float>(i, 3) * image.cols);
//                 int yLeftBottom = static_cast<int>(detections.at<float>(i, 4) * image.rows);
//                 int xRightTop = static_cast<int>(detections.at<float>(i, 5) * image.cols);
//                 int yRightTop = static_cast<int>(detections.at<float>(i, 6) * image.rows);

//                 rectangle(image, Point(xLeftBottom, yLeftBottom), Point(xRightTop, yRightTop), Scalar(0, 255, 0));

//                 // Set flag if obstacle is detected
//                 obstacleDetected = true;
//             }
//         }

//         // Show image with detections
//         imshow("Detected Objects", image);
//         waitKey(0);
//     }

//     bool checkForObstacles() override {
//         return obstacleDetected;
//     }
// };
