import subprocess


def run_bash_command(command):
    result = subprocess.run(f"wsl {command}", shell=True, text=True, capture_output=True)
    
    stdout = result.stdout.strip()
    stderr = result.stderr.strip()
    
    if stdout:
        # print("Output:", stdout)
        with open("uploaded_result.txt", 'w') as file:
                file.write(stdout)
        
    if stderr:
        # print("Errors:", stderr)
        with open("uploaded_result.txt", 'w') as file:
                file.write("Error")
    
    return result.returncode

if __name__ == "__main__":

    compile_command = f"cobc -x cobol_sample1.cob"
    compile_return_code = run_bash_command(compile_command)
    
    if compile_return_code == 0:
        print("Compilation successful.")
        run_command = f"./cobol_sample1"
        run_return_code = run_bash_command(run_command)
        
        if run_return_code == 0:
            print("Program executed successfully.")
        else:
            print(f"Program failed with return code: {run_return_code}")
    else:
        print(f"Compilation failed with return code: {compile_return_code}")
