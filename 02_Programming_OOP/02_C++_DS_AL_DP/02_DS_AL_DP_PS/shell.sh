#!/bin/bash

# Set the specific base directory
BASE_DIR="/media/ferganey/Data/00_Main_Folder/02_Programming_OOP/02_C++_DS_AL_DP/02_DS_AL_DP_PS"

# Define the JSON templates
FILES_ASSOCIATIONS='{
    "files.associations": {
        "array": "cpp",
        "atomic": "cpp",
        "bit": "cpp",
        "*.tcc": "cpp",
        "cctype": "cpp",
        "clocale": "cpp",
        "cmath": "cpp",
        "compare": "cpp",
        "concepts": "cpp",
        "cstdarg": "cpp",
        "cstddef": "cpp",
        "cstdint": "cpp",
        "cstdio": "cpp",
        "cstdlib": "cpp",
        "cwchar": "cpp",
        "cwctype": "cpp",
        "deque": "cpp",
        "string": "cpp",
        "unordered_map": "cpp",
        "vector": "cpp",
        "exception": "cpp",
        "algorithm": "cpp",
        "functional": "cpp",
        "iterator": "cpp",
        "memory": "cpp",
        "memory_resource": "cpp",
        "numeric": "cpp",
        "optional": "cpp",
        "random": "cpp",
        "string_view": "cpp",
        "system_error": "cpp",
        "tuple": "cpp",
        "type_traits": "cpp",
        "utility": "cpp",
        "initializer_list": "cpp",
        "iosfwd": "cpp",
        "iostream": "cpp",
        "istream": "cpp",
        "limits": "cpp",
        "new": "cpp",
        "numbers": "cpp",
        "ostream": "cpp",
        "stdexcept": "cpp",
        "streambuf": "cpp",
        "typeinfo": "cpp",
        "ctime": "cpp",
        "iomanip": "cpp",
        "sstream": "cpp",
        "charconv": "cpp",
        "chrono": "cpp",
        "ratio": "cpp",
        "format": "cpp",
        "semaphore": "cpp",
        "span": "cpp",
        "stop_token": "cpp",
        "thread": "cpp",
        "variant": "cpp"
    }
}'

TASKS_TEMPLATE='{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "C++ Projects SubDirs",
            "type": "shell",
            "command": "echo Hello"
        },
        // Add build tasks here
    ]
}'

# Find the specific directory and create settings.json and tasks.json
find "$BASE_DIR" -type d | while read -r dir; do
    echo "$FILES_ASSOCIATIONS" > "$dir/settings.json"
    echo "$TASKS_TEMPLATE" > "$dir/tasks.json"

    # Add build tasks for .cpp files in the directory
    for cpp_file in "$dir"/*.cpp; do
        if [[ -f $cpp_file ]]; then
            file_name=$(basename "$cpp_file")
            base_name="${file_name%.*}"

            # Append a new build task to the tasks.json
            jq --arg label "build $base_name" --arg file "$cpp_file" --arg dir "$dir" \
                '.tasks += [{
                    "type": "cppbuild",
                    "label": $label,
                    "command": "/usr/bin/g++-13",
                    "args": [
                        "-fdiagnostics-color=always",
                        "-g",
                        "-std=c++20",
                        $file,
                        "-o",
                        "$dir/$base_name"
                    ],
                    "options": {
                        "cwd": "$dir"
                    },
                    "problemMatcher": [
                        "$gcc"
                    ],
                    "group": "build",
                    "detail": "compiler: /usr/bin/g++-13"
                }]' "$dir/tasks.json" > "$dir/tasks_tmp.json" && mv "$dir/tasks_tmp.json" "$dir/tasks.json"
        done
    done
done
