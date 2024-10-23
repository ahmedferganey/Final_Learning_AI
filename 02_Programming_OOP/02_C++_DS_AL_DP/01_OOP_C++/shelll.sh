#!/bin/bash

# Define the main directory containing your C++ examples
MAIN_DIR="/media/ferganey/Data/00_Main_Folder/02_Programming_OOP/02_C++_DS_AL_DP/01_OOP_C++"

# Define the output tasks.json file location
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
)

# Loop through each directory and subdirectory
for dir in "${dirs[@]}"; do
    for i in {1..5}; do
        subdir="Example_$i"
        example_cpp="$MAIN_DIR/$dir/$subdir/$subdir.cpp"
        example_out="$MAIN_DIR/$dir/$subdir/$subdir"
        output_log="$MAIN_DIR/$dir/$subdir/build_output.txt"

        # Append a new task for each Example_1.cpp in each directory
        cat << EOF >> "$TASKS_FILE"
        {
            "type": "cppbuild",
            "label": "build $dir/$subdir/$subdir.cpp",
            "command": "/usr/bin/g++-13",
            "args": [
                "-fdiagnostics-color=always",
                "-g",
                "-std=c++20",
                "$example_cpp",
                "-o",
                "$example_out",
                "2>&1",
                "|",
                "tee",
                "$output_log"
            ],
            "options": {
                "cwd": "$MAIN_DIR/$dir/$subdir"
            },
            "problemMatcher": [
                "\$gcc"
            ],
            "group": "build",
            "detail": "compiler: /usr/bin/g++-13"
        },
EOF
    done
done

# Remove the trailing comma from the last task and close the JSON structure
sed -i '$ s/},/}/' "$TASKS_FILE"

cat << EOF >> "$TASKS_FILE"
    ]
}
EOF

echo "tasks.json has been updated at $TASKS_FILE"
