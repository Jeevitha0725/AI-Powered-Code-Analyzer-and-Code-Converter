
import subprocess
import os

def run_command(command):
    """Run a command in the shell and print its output."""
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    print("Output:", result.stdout)
    if result.stderr:
            print("Errors:")
            print(result.stderr)
    return result.returncode

def create_and_run_dotnet_app():
    # Create a new .NET console application
    create_command = "dotnet new console -o cs_sample1"
    print("Creating .NET application...")
    return_code = run_command(create_command)
    if return_code != 0:
        print("Failed to create .NET application.")
        return

    # Navigate into the application directory
    # os.chdir("cs_sample1")

    # Run the .NET application
    run_command("dotnet run")

if __name__ == "__main__":
    create_and_run_dotnet_app()
