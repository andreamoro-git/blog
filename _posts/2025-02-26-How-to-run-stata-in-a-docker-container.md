---
tags: tips
---
# How to run Stata inside a Docker container

Lars Vilhuber, the AEA data editor, has made available a set of Docker images for Stata at [this github repository](https://github.com/AEADataEditor/docker-stata?tab=readme-ov-file). I decided to give it a try with the purpose of streamlining the grading of my PhD class computer homework. As I should have expected, it took me the good part of a day to make it work. 

Lars's instructions are more comprehensive (and didn't work for me, I'm sure it's my fault),  I am posting a quick solution reference that worked for me on my IMac with OS Sequoia 15.3. I assume you have Docker installed, and you are somewhat familiar with opening a terminal in your computer and typing into it, navigating directories, etc... (but not a lot more really). 

It goes like this:

1. Figure out where your Stata license file is. Just google if you have no idea. Copy it into your working directory.
2. Create this Dockerfile (with filename: Dockerfile, no extension). The part ```stata18-se-i:2024-12-18``` can and should be changed according to your license and preferences. The full list of images:tags is available [at the dataeditors docker hub](https://hub.docker.com/u/dataeditors)

	```
	FROM dataeditors/stata18-se-i:2024-12-18

	# create a working directory (not necessary but keeps things tidy)
	WORKDIR /project/
	```

2. Build the image (substitute . for the directory where you placed the Dockerfile, if elsewhere than your working directory)

	```
	docker build -t stataimg .
	``` 

3. Run the following to open up an interactive stata interface. The -v flag is mounting a local directory into the container's tree ($PWD stands for present-working-directory, you have to indicate the entire path from the root if you don't want to use the variable). The directory after the colon is where your local path will be mounted into the container - it should be consistent with the WORKDIR indicated in the Dockerfile. My solution assumes your do files are in a subdirectory of the present working directory called my_project_do_files. That's where output/dta files/etc... will be saved by your stata scripts. If you want a more complex directory structure, make sure its root is mounted to /project, which is defined as the working directory inside the Dockerfile

	``` 
	docker run --init -it --rm \
				--mount "type=bind,source=${PWD}/stata.lic,target=/usr/local/stata/stata.lic" \
				-v "${PWD}/my_project_do_files":/project \
				stataimg
	```
You can also batch-run a do file by adding after ```stataimg``` ```-b dofile.do``` where dofile.do is inside the directory you mount with the -v flag above. This is what you should do when preparing a replication package, to minimize replicator's typing. 

That's all. Let me know if it does not work for you. 