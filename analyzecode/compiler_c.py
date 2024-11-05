import subprocess
import os

def compile_c(c_file_path):
    try:
        # Check if the C file exists
        if not os.path.exists(c_file_path):
            print(f"Error: File {c_file_path} not found!")
            return

        # Compile the C file using gcc
        output_file = "output_executable"  # Name of the output executable
        compile_command = ['gcc', c_file_path, '-o', output_file]
        # print(f"Compiling {c_file_path}...")
        result = subprocess.run(compile_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Check for errors during compilation
        if result.returncode != 0:
            print("Compilation failed!")
            print(result.stderr)  # Display compilation errors
        else:
            print("Compilation successful!")
            print(result.stdout)  # Display any relevant output
            
            # Run the compiled executable
            run_c(output_file)

    except Exception as e:
        print(f"An error occurred: {str(e)}")


def run_c(executable_path):
    try:
        # Run the compiled C executable
        run_command = [f"./{executable_path}"]
        print(f"Running {executable_path}...")
        result = subprocess.run(run_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Check for runtime errors
        if result.returncode != 0:
            print("Execution failed!")
            print(result.stderr)  # Display runtime errors
            with open("uploaded_result.txt", 'w') as file:
                file.write("Error")
        else:
            print("Execution successful!")
            print(result.stdout)  # Display program output
            with open("uploaded_result.txt", 'w') as file:
                file.write(result.stdout)

    except Exception as e:
        print(f"An error occurred during execution: {str(e)}")



c_file = "c_sample1.c"  # Replace with your C file path
compile_c(c_file)
