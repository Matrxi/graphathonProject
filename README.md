# graphathonProject
Project for graphathon
 
Steps to run the web-app in Linux
 
Step 1: clone the repository : git clone https://github.com/Matrxi/graphathonProject.git

Step 2: install pip3
        $ sudo apt-get install pip3
        
Step 3: Run the following command to satisfy the requirements
        $ pip install -r requirements.txt
        
Step 4: Perform migrations
        $ python3 manage.py migrate
      
Step 5: Start the server
        $ python3 manage.py runserver
        
 Now go to 127.0.0.0:8000 if you didn't specify port number explicitly
 
You will be logged in as super user if you follow the above commands
A super user is already created : 
   username = root
   password = root
   
   dob = none
       
 
Two files have been already uploaded by superuser. 
Only superuser has the permissions to delete files.

A normal user has permissions to either upload a file or download files.

