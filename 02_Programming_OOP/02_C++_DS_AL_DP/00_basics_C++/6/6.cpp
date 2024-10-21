#include <iostream>
#include <vector>

const int Pen{ 10 };
const int Marker{ 20 };
const int Eraser{ 30 };
const int Rectangle{ 40 };
const int Circle{ 50 };
const int Ellipse{ 60 };


int main(){
   int tool {Eraser};

    switch (tool)
    {
        case Pen : {
             std::cout << "Active tool is Pen" << std::endl;
        }
        break;

        case Marker : {
             std::cout << "Active tool is Marker" << std::endl;
        }
        break;


        case Eraser :{
             std::cout << "Eraser" << std::endl;
        }
        case Rectangle : 
        case Circle : {
             std::cout << "Drawing Shapes" << std::endl;
        }
        break;

        case Ellipse : {
             std::cout << "Active tool is Ellipse" << std::endl;
        }
        break;
    
        default: {
            std::cout << "No match found" << std::endl;
        }
            break;
    }

    std::cout << "Moving on" << std::endl;

/////////////////////////////////////////////////////////////
int max = (1 < 5)? true : false;
            std::cout << max << std::endl;
bool fast = true;
int speed{fast? true:false};
            std::cout << fast << std::endl;
            std::cout << speed << std::endl;
//////////////////////////////////////////////////////////////////
for (unsigned int i{1}; i<10; i++){
    std::cout << "i love mariam" << std::endl;
}

    std::vector<int> numbers = {1, 2, 3, 4, 5};

    // Using size_t
    for (size_t i{}; i < numbers.size(); ++i) {
        std::cout << "size_t index: " << i << " value: " << numbers[i] << std::endl;
    }

    // Using unsigned int
    unsigned int count = 5;
    for (unsigned int i = count; i > 0; --i) {
        // This works fine, but let's see what happens if we go too far
        std::cout << "unsigned int index: " << i << " value: " << numbers[i - 1] << std::endl;
    }

    // Example of potential issue with unsigned int
    unsigned int negativeIndex = -1; // This wraps around to a large positive number
    std::cout << "Wrap around with unsigned int: " << negativeIndex << std::endl;




}
