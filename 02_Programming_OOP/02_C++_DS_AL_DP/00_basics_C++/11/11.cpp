#include <iostream>

#include </media/ferganey/Data/00_Main_Folder/02_Programming_OOP/02_C++_DS_AL_DP/00_basics_C++/11/FileOrganizer.h>

constexpr int add(int a, int b){return a+b;}
constexpr int subtract(int a, int b) { return a - b; }
constexpr int multiply(int a, int b) { return a * b; }
constexpr int divide(int a, int b){return (b != 0)? a/b : 0;}








int main(){
    int x, y;
    char op;

    std::cout << "Enter operation (e.g., 4 + 5): ";
    std::cin >> x >> op >> y;

    int result = 0;
    switch (op) {
        case '+': result = add(x, y); break;
        case '-': result = subtract(x, y); break;
        case '*': result = multiply(x, y); break;
        case '/': result = divide(x, y); break;
        default: std::cout << "Invalid operation\n"; return 1;
    }

    std::cout << "Result: " << result << "\n";
    
////////////////////////////////////////////////////////////    
    FileOrganizer organizer;
    organizer.organizeFiles("/media/ferganey/Data/00_Main_Folder/02_Programming_OOP/02_C++_DS_AL_DP/00_basics_C++/11");

    return 0;

}
