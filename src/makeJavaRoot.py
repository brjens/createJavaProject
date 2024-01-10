#!/usr/bin/env python3
import os
import sys
import shutil

def create_project_structure(directory="."):
    # Create main directories
    os.makedirs(os.path.join(directory, "src"))
    os.makedirs(os.path.join(directory, "test"))
    os.makedirs(os.path.join(directory, "lib"))

    # Create initial files
    open(os.path.join(directory, ".gitignore"), "w").write(get_gitignore_content())
    open(os.path.join(directory, "src/Main.java"), "w").write(get_sample_java_code())
    open(os.path.join(directory, "README.md"), "w").write(get_readme_content())

    # Initialize Git repository
    os.chdir(directory)
    os.system("git init")

    print("Project structure created successfully!")

def undo_project_structure(directory="."):
    # Remove Git repository
    os.chdir(directory)
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

def get_gitignore_content():
    return """
# Ignore compiled Java class files
*.class

# Ignore JAR files
*.jar

# Ignore .gitignore
.gitignore
"""

if __name__ == "__main__":
    if len(sys.argv) > 1:
        option = sys.argv[1]
        if option == "-r":
            undo_project_structure()
            sys.exit()
        elif option == "-n" and len(sys.argv) > 2:
            directory = sys.argv[2]
            create_project_structure(directory)
            sys.exit()
    create_project_structure()
