---
layout: post
tags: tips
---

# How to run intel fortran on MacOS using docker containers

Note: these commands are to be entered in a terminal shell, if you don't know what a terminal is and how to access it on MacOS, you need to figure that out first

1- Set up the container

  - Install Docker
  - Create a basic intel oneapi fortran image by typing on your shell (will take a few minutes)
    ```
    docker pull intel/oneapi-hpckit 
    ```
    
2- Run your first container
     
     docker run --name firstcontainer -it intel/oneapi-hpckit 
     
3- Make changes you need to your container (e.g. customize .bash_profile, aliases, etc.. at your pleasure), for example,

    apt-get update
    apt-get install -y byobu curl git htop man unzip vim wget
    apt-get clean     

(since I make use of python I also need to)

    pip install tornado
    pip install --upgrade matplotlib  
    
Then, exit the container
    
4- Create an image with your changes (named "myimage")

     docker commit firstcontainer myimage

5- Here is how to run a container mounting a local directory to the system

    docker run -it --name secondcontainer -v /path/to/directory/to/mount:/root/path/to/somewhere/inside/container myimage  

6- Here is to bash (not really, but good enough) into an existing container

      docker exec -it secondcontainer bash

7- Other useful commands i keep forgetting

      docker container prune

Note: I recommend starting containers afresh and pruning them frequently. In my experience, things start to act funny after a while. 
