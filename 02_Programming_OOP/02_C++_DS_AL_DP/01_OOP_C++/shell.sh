#!/bin/bash

# Define the main directory containing your C++ examples
MAIN_DIR="/media/ferganey/Data/00_Main_Folder/02_Programming_OOP/02_C++_DS_AL_DP/01_OOP_C++"
TASKS_FILE="$MAIN_DIR/.vscode/tasks.json"

# Create or overwrite the tasks.json file
cat << EOF > "$TASKS_FILE"
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "OOP_C++",
            "type": "shell",
            "command": "echo Hello"
        },
EOF

# Array of directories in the main folder
dirs=(
    "00_Classes"
    "01_Inheritance"
    "02_Polymorphism"
    "03_Encapsulation"
    "04_Abstraction"
    "05_Constructors"
    "06_Destructors"
    "07_Operator_Overloading"
    "08_Templates"
    "09_Virtual_Functions"
    "10_OOP_Projects"  # Added to include your new project folder
)

# Loop through each directory and its subdirectories
for dir in "${dirs[@]}"; do
    for subdir in "$MAIN_DIR/$dir"/*/; do
        # Check if the directory contains any .cpp files
        for cpp_file in "$subdir"*.cpp; do
            if [ -f "$cpp_file" ]; then
                # Get the base name of the file and the output executable name
                base_name=$(basename "$cpp_file" .cpp)
                output_executable="$subdir$base_name"
                output_log="$subdir/build_output.txt"

                # Append a new task for each .cpp file in tasks.json
                cat << EOF >> "$TASKS_FILE"
        {
            "type": "cppbuild",
            "label": "build $dir/$base_name",
            "command": "/usr/bin/g++-13",
            "args": [
                "-fdiagnostics-color=always",
                "-g",
                "-std=c++20",
                "$cpp_file",
                "-o",
                "$output_executable",
                "2>&1",
                "|",
                "tee",
                "$output_log"
            ],
            "options": {
                "cwd": "$subdir"
            },
            "problemMatcher": [
                "\$gcc"
            ],
            "group": "build",
            "detail": "compiler: /usr/bin/g++-13"
        },
EOF
            fi
        done
    done
done

# Remove the trailing comma from the last task and close the JSON structure
sed -i '$ s/},/}/' "$TASKS_FILE"

cat << EOF >> "$TASKS_FILE"
    ]
}
EOF

echo "tasks.json has been updated at $TASKS_FILE"
