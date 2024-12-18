#include </media/ferganey/Data/00_Main_Folder/02_Programming_OOP/02_C++_DS_AL_DP/00_basics_C++/11/FileOrganizer.h>
#include <filesystem>
#include <iostream>


using namespace std;


void FileOrganizer::organizeFiles(const string& directorPath){
    for (const auto& entry : filesystem::directory_iterator(directorPath)){
        // logic here 
        cout << "Processing files" << entry.path() << "\n";
    }

 }

