### Create a directory named "project_files". Inside this directory, create three empty files: "config.yaml", "scripts.py", and "readme.md". Before creating each file, check if it already exists to avoid overwriting any existing files. If a file already exists, print a message indicating that the file exists.
import os
os.mkdir("project_files")   
files=["config.yaml","scripts.py","readme.md"]   
  for file in files:   
      if (os.path.exists(os.path.join("project_files",file))):  
        print("file exists")  
      else:  
        with open(os.path.join("project_files",file), "w") as newfile:
        newfile.write("")
        
        
### Write a Python function that takes a file name and a string as arguments. The function should create a new file with the given name, write the provided string into the file, and then return the absolute path of the newly created file.
import os
def ops(file_name,text):
  with open(file_name, "w") as file:
    file.write(text)
  curr = os.getcwd()
  return os.path.join(curr,file_name)



### Write a Python script that creates a directory named "data". Inside this directory, create 100 text files named "file1.txt" to "file100.txt". Each file should contain the text "This is file X", where X is the file number. After creating all the files, print the total number of files created in the "data" directory.
import os
os.mkdir("data")
for i in range(1,101):
  with open(os.path.join("data",f"file{i}.txt"),"w") as file:
    file.write(f"This is file {i}")
    
### Connect to a remote server using SSH and create a directory named "remote_project". Inside this directory, create an empty file named "info.txt". Use the `fabric` library to accomplish this task.
import os
from fabric import Connection
conn=Connection("remote_server")
conn.run("mkdir remote_project")
conn.run("touch remote_project/info.txt")


### Using the `fabric` library, write a Python script that connects to a remote server via SSH, retrieves the file "info.txt" from the "remote_project" directory, and saves it to the current local directory.
from fabric import Connection,scp
conn=Connection("hostname")
cwd=os.getcwd()
conn.get('remote_project/info.txt', cwd)


from fabric import Connection

import os

password=os.environ.get("password")


### Write a Python function that connects to a list of remote servers via SSH using the `fabric` library. The function should take a list of hostnames and a password as arguments. For each server, it should execute a command to check if a specific directory (e.g., "remote_project") exists. If the directory exists, print a success message; if not, print an error message.
def run_remote_commands(hostname,password):
  try:
    conn=Connection(hostname,password)
    result=conn.run("some command") 
    if result.return_code == 0:
      print("command executed successfully")
    else: 
      print("Error occurred", result.stderr)
  except Exception as e:
    print("Exception occurred", e)

servers=["server1.com","server2.com","server3.com"]
for server in servers:
  run_remote_commands(server,password)
