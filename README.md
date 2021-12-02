# PL-Project
PL Project 
#Read me file

Hi! We are group U, and our group consists of Ivanelyz Rivera, Gloriel Soto and Haniel Cordero for the  ICOM4036 / CIIC4030 class. 

We present #Infrastructure as a service (IaaS), this is a type of cloud computing service that offers essential compute, storage and networking resources that are on demand! 

We wanted to create a language that lets users create servers by coding repetitive tasks and automate the virtual server creations! Therefore, the project will be in the memory management branch of coding.

There's going to be a Lexical Analyzer, that is the first phase of the compiler. It breaks the syntax into a series of tokens, by removing any whitespace or comments that are in our code. 
Also, our Syntax Analyzer is going to take the input from a lexical analyzer and analyzes the source code. 
And, finally our intermediate code is where the droplets and main functions of the code are going to be.
The Droplets are a linux based VMs that are used to run on top of virtualized hardware.
Each Droplet that we create, is a new server you can use and part of the cloud based infrastructure.


------------------------------- INSTRUCTIONS -------------------------------

1. Download the latest stable version of Python. 
-> https://www.python.org/downloads/ 
 
2. Download the latest version of VSCode or the editor of your preference such as pycharm. 
-> https://code.visualstudio.com/download

3. To access this project, go to the command prompt and write git clone and paste the repository https://github.com/Ivanelyzrivera/PL-Project.git

--- Recommended ---

-> within VSCode, install Python extensions that help run the code. 
In the terminal type: pip install -U python-digitalocean

4. In the terminal enter the PL-Project/main.py
5. In the terminal type: -1 droplets 
6. In the terminal type: -I img and -I loc , this should run the code. 
7. If not you can enter in the terminal python3 main.py and it's going to run the code.
8. In the terminal type: main -l droplets to see the list of the availables Virtual Machines 
9. In the terminal type: main -i to create a new Virtual Machine
10. In the terminal type: main -rm <dropletId> to delete the Virtual Machine

 -------------EXAMPLES ON HOW IT SHOULD LOOK: --------------------------------
 ![image](https://user-images.githubusercontent.com/70592721/144349836-252ff7a2-6cca-4371-a990-2a76c9af00b0.png)
 Menu to choose:
 
 ![image](https://user-images.githubusercontent.com/70592721/144349901-9fdd581c-d698-468e-ba2f-097bac049dba.png)
 ![image](https://user-images.githubusercontent.com/70592721/144349927-e6112d32-2c52-4136-89d0-4f35b3f24226.png)
 ![image](https://user-images.githubusercontent.com/70592721/144349961-3fff976c-4cda-4cde-8449-dcc2ac49de3f.png)
 
 Creating Droplet: 
![image](https://user-images.githubusercontent.com/70592721/144349998-4ea92eb8-2717-4783-aa0f-01cb12a39376.png)
 
 Choosing region:
 ![image](https://user-images.githubusercontent.com/70592721/144350068-86f37f7e-e2b4-4db0-b017-7352f76fe678.png)
 
 Choosing the base image: "rockylinux-8-x64
 ![image](https://user-images.githubusercontent.com/70592721/144350111-9f0d98ff-347c-4933-93fe-51b4424c5348.png)
 
 Creating of the droplet1:
![image](https://user-images.githubusercontent.com/70592721/144350141-6e51a488-5f7c-42b1-b64b-e13d7f2d67e9.png)
 
 Delete the droplet: 
 ![image](https://user-images.githubusercontent.com/70592721/144350228-97a1f2b6-b1a5-4575-9061-456aaf0dae2b.png)
 
Confirmed: 
 ![image](https://user-images.githubusercontent.com/70592721/144350254-e32107d3-c13f-4348-bf25-4ea0d479f72f.png)

 
Note: When a droplet is created we get an alert via email indicating the droplet name, ip address, username and password. 
 ![image](https://user-images.githubusercontent.com/70592721/144350388-73737785-5533-4e61-820a-6dd883648a2f.png)





 
 
 
 
 
