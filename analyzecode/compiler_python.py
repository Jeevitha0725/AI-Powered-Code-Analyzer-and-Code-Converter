import subprocess

def run_python_script(script_path):
    try:
        # Run the Python script
        result = subprocess.run(['python', script_path], capture_output=True, text=True, check=True)
        
        # Print the output of the script
        print("Output:")
        # print(result.stdout)
        with open("uploaded_result.txt", 'w') as file:
                file.write(result.stdout)
        
        # Print any errors
        if result.stderr:
            print("Errors:")
            # print(result.stderr)
            with open("uploaded_result.txt", 'w') as file:
                file.write("Error")
            
    except subprocess.CalledProcessError as e:
        print(f"Error running script: {e}")
        print(f"Error output: {e.stderr}")

if __name__ == "__main__":
    script_path = 'py_sample1.py'  # Path to the Python script you want to run
    run_python_script(script_path)
