import os
import json

base_dir = os.getcwd()
task_list = []

# Loop through each directory (0 to 30)
for i in range(51):  # Adjust this range based on your directories
    dir_path = os.path.join(base_dir, str(i))
    cpp_files = [f for f in os.listdir(dir_path) if f.endswith('.cpp')]  # List all .cpp files in the directory
    for cpp_file in cpp_files:
        task = {
            "type": "cppbuild",
            "label": f"build {i}/{cpp_file}",
            "command": "/usr/bin/g++-13",
            "args": [
                "-fdiagnostics-color=always",
                "-g",
                "-std=c++20",
                f"{os.path.join(dir_path, cpp_file)}",  # Full path to the current cpp file
                "-o",
                f"{os.path.join(dir_path, cpp_file[:-4])}"  # Output file without the .cpp extension
            ],
            "options": {
                "cwd": dir_path  # Set the current working directory to the directory of the cpp file
            },
            "problemMatcher": [
                "$gcc"
            ],
            "group": "build",
            "detail": "compiler: /usr/bin/g++-13"
        }
        task_list.append(task)

# Include the echo task
task_list.insert(0, {
    "label": "echo",
    "type": "shell",
    "command": "echo Hello"
})

# Write to tasks.json
tasks_json = {
    "version": "2.0.0",
    "tasks": task_list
}

with open('.vscode/tasks.json', 'w') as f:
    json.dump(tasks_json, f, indent=4)

print("tasks.json created successfully.")
