import subprocess
import os

def compile_java(java_file_path):
    try:
        # Check if the file exists
        if not os.path.exists(java_file_path):
            print(f"Error: File {java_file_path} not found!")
            return
        
        # Compile the Java file using javac
        compile_command = ['javac', java_file_path]
        print(f"Compiling {java_file_path}...")
        result = subprocess.run(compile_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Check for errors during compilation
        if result.returncode != 0:
            print("Compilation failed!")
            print(result.stderr)  # Display compilation errors
        else:
            print("Compilation successful!")
            print(result.stdout)  # Display any relevant output
            
            # Get the base name of the file (without extension) to run the class
            class_name = os.path.splitext(os.path.basename(java_file_path))[0]
            run_java(class_name)

    except Exception as e:
        print(f"An error occurred: {str(e)}")


def run_java(class_name):
    try:
        # Run the compiled Java class using java command
        run_command = ['java', class_name]
        print(f"Running {class_name}.class...")
        result = subprocess.run(run_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Check for runtime errors
        if result.returncode != 0:
            print("Execution failed!")
            print(result.stderr)  # Display runtime errors
        else:
            print("Execution successful!")
            print(result.stdout)  # Display program output

    except Exception as e:
        print(f"An error occurred during execution: {str(e)}")


# Example usage
java_file = "javademo.java"  # Replace with your Java file path
compile_java(java_file)
