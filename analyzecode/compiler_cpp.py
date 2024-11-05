import subprocess
import os

def compile_cpp_in_wsl(source_file, output_executable):
    # Compile command for WSL
    compile_command = f"wsl g++ {source_file} -o {output_executable}"
    try:
        print(f"Compiling {source_file} in WSL...")
        subprocess.run(compile_command, check=True, shell=True)
        print(f"Compilation successful. Executable created: {output_executable}")
    except subprocess.CalledProcessError as e:
        print(f"Compilation failed with error: {e}")
        return None

    return output_executable

def run_executable_in_wsl(executable):
    # Execute the program in WSL and capture output
    run_command = f"wsl ./{executable}"
    try:
        print(f"Running {executable} in WSL...")
        result = subprocess.run(run_command, check=True, capture_output=True, text=True, shell=True)
        
        # Store the output in a variable
        output = result.stdout
        error_output = result.stderr
        
        # Print the output
        print("Output:")
        print(output)
        
        # Return the output for further processing if needed
        return output, error_output
    except subprocess.CalledProcessError as e:
        print(f"Execution failed with error: {e}")
        return None, e.stderr

if __name__ == "__main__":
    # Define the C++ source file and the output executable name
    source_file = "cpp_sample1.cpp"  # Change to your actual C++ file
    output_executable = "program"

    # Check if the source file exists
    if not os.path.exists(source_file):
        print(f"Error: {source_file} not found!")
    else:
        # Compile the C++ program
        executable = compile_cpp_in_wsl(source_file, output_executable)
        # Run the executable if compilation was successful
        if executable:
            output, error_output = run_executable_in_wsl(executable)
            # Handle the output as needed
            if output:
                print("Captured Output:")
                # print(output)
                with open("uploaded_result.txt", 'w') as file:
                    file.write(output)
            if error_output:
                print("Captured Error Output:")
                # print(error_output)
                with open("uploaded_result.txt", 'w') as file:
                    file.write("Error")
        else:
            print("Failed to compile the program.")
