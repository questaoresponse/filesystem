import os
import subprocess

# Get the path to the repository
repository_path = os.path.dirname(os.path.realpath(__file__))

# # Get the path to the build directory
# build_directory = os.path.join(repository_path, "build")
# # Create the build directory if it does not exist
# if not os.path.exists(build_directory):
#     os.makedirs(build_directory)

# # Change the current directory to the build directory
# os.chdir(build_directory)

# Run the build command
subprocess.call(["python","-m","install","--upgrade","pip"])
subprocess.call(["pip","install","-r","requirements.txt"])
subprocess.call(["gunicorn", "app:app", "--workers", "3"])
#teste
# Copy the built artifacts to the output directory
# output_directory = os.path.join(repository_path, "output")
# if not os.path.exists(output_directory):
#     os.makedirs(output_directory)

# subprocess.call(["cp", "-r", "./*", repository_path])