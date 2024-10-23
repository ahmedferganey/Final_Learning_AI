#!/bin/bash

# Base directory where the directories will be created
base_dir="/media/ferganey/Data/00_Main_Folder/02_Programming_OOP/02_C++_DS_AL_DP/01_OOP_C++"

# Array of OOP-related topics for C++ with numbering
oop_topics=("00_Classes" "01_Inheritance" "02_Polymorphism" "03_Encapsulation" "04_Abstraction" "05_Constructors" "06_Destructors" "07_Operator_Overloading" "08_Templates" "09_Virtual_Functions")

# Number of subdirectories to create inside each topic directory
num_subdirs=5

# Loop through each OOP topic
for topic in "${oop_topics[@]}"; do
    # Create the main topic directory
    topic_dir="${base_dir}/${topic}"
    mkdir -p "$topic_dir"
    
    # Loop to create subdirectories and .cpp files
    for i in $(seq 1 $num_subdirs); do
        subdir_name="Example_${i}"
        subdir="${topic_dir}/${subdir_name}"
        
        # Create subdirectory
        mkdir -p "$subdir"
        
        # Create .cpp file with the same name as the subdirectory
        cpp_file="${subdir}/${subdir_name}.cpp"
        touch "$cpp_file"
        
        # Add a simple template inside the .cpp file
        echo "// ${subdir_name}.cpp - Example code for ${topic}" > "$cpp_file"
        echo "#include <iostream>" >> "$cpp_file"
        echo "" >> "$cpp_file"
        echo "int main() {" >> "$cpp_file"
        echo "    std::cout << \"${subdir_name} example for ${topic}\" << std::endl;" >> "$cpp_file"
        echo "    return 0;" >> "$cpp_file"
        echo "}" >> "$cpp_file"
    done
done

echo "Directories and files created successfully!"
