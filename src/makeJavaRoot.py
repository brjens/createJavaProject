#!/usr/bin/env python3
import os
import sys
import shutil

def create_project_structure():
    # Create main directories
    os.makedirs("src")
    os.makedirs("test")
    os.makedirs("lib")

    # Create initial files
    open(".gitignore", "w").close()
    open("src/Main.java", "w").write(get_sample_java_code())
    open("README.md", "w").write(get_readme_content())

    # Initialize Git repository
    os.system("git init")

    print("Project structure created successfully!")

def undo_project_structure():
    # Remove Git repository
    shutil.rmtree(".git")

    # Remove initial files
    os.remove(".gitignore")
    os.remove("src/Main.java")
    os.remove("README.md")

    # Remove main directories
    shutil.rmtree("src")
    shutil.rmtree("test")
    shutil.rmtree("lib")

    print("Project structure undone successfully!")

def get_sample_java_code():
    return """
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, world!");
    }
}
"""

def get_readme_content():
    return """
# My Java Project

This is a basic Java project created using the project structure script.

## Getting Started

1. Clone the repository
2. Open the project in your favorite Java IDE
3. Run the `Main` class to see the output "Hello, world!"

Feel free to customize this README with your own project-specific details.
"""

if __name__ == "__main__":
    if len(sys.argv) > 1:
        option = sys.argv[1]
        if option == "-r":
            undo_project_structure()
            sys.exit()
    create_project_structure()
