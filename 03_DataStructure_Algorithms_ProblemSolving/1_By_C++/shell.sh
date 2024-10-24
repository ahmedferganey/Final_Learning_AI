#!/bin/bash

# Array of algorithms and data structures
algorithms=("BinarySearch" "MergeSort" "QuickSort" "LinkedList" "BinaryTree" "GraphTraversal")

# Base directory path
base_dir="/media/ferganey/Data/00_Main_Folder/03_DataStructure_Algorithms_ProblemSolving/1_By_C++"

# Path to the existing tasks.json in the .vscode folder
tasks_json="$base_dir/.vscode/tasks.json"

# Initialize tasks.json if it doesn't exist
if [ ! -f "$tasks_json" ]; then
    mkdir -p "$(dirname "$tasks_json")"
    echo '{
    "version": "2.0.0",
    "tasks": []
}' > "$tasks_json"
fi

# Clear previous tasks to avoid duplicates
jq '.tasks = []' "$tasks_json" > temp.json && mv temp.json "$tasks_json"

# Create subdirectories, files, and prepare tasks for tasks.json
for algorithm in "${algorithms[@]}"; do
    # Create subdirectory
    sub_dir="$base_dir/$algorithm"
    mkdir -p "$sub_dir"
    
    # Create C++ file
    cpp_file="$sub_dir/$algorithm.cpp"
    
    # Add basic C++ template to the .cpp file
    cat > "$cpp_file" <<EOL
#include <iostream>

using namespace std;

int main() {
    // Your code for $algorithm goes here.
    cout << "Running $algorithm algorithm." << endl;
    return 0;
}
EOL

    # Make the C++ file executable (optional)
    chmod +x "$cpp_file"

    # Append tasks to the .vscode/tasks.json file
    jq --arg algorithm "$algorithm" --arg base_dir "$base_dir" --arg cpp_file "$cpp_file" \
    '.tasks += [{
        "label": "\($algorithm) Task",
        "type": "shell",
        "command": "echo Running \($algorithm)"
    },
    {
        "type": "cppbuild",
        "label": "\($algorithm).cpp",
        "command": "/usr/bin/g++-13",
        "args": [
            "-fdiagnostics-color=always",
            "-g",
            "-std=c++20",
            "\($cpp_file)",
            "-o",
            "\($base_dir)/\($algorithm)/\($algorithm)",
            "2>&1",
            "|",
            "tee",
            "\($base_dir)/\($algorithm)/\($algorithm).txt"
        ],
        "options": {
            "cwd": "\($base_dir)/\($algorithm)"
        },
        "problemMatcher": [
            "$gcc"
        ],
        "group": "build",
        "detail": "compiler: /usr/bin/g++-13"
    }]' "$tasks_json" > temp.json && mv temp.json "$tasks_json"

done

echo "Subdirectories, C++ files, and tasks have been created successfully in tasks.json."
