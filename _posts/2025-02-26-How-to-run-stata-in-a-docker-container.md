---
tags: tips
---
# How to run Stata inside a Docker container

Lars Vilhuber, the AEA data editor, has made available a set of Docker images for Stata at [this github repository](https://github.com/AEADataEditor/docker-stata?tab=readme-ov-file). I decided to give it a try with the purpose of streamlining the grading of my PhD class computer homework. As I should have expected, it took me the good part of a day to make it work. 

Lars's instructions are more comprehensive (and didn't work for me, I'm sure it's my fault),  I am posting a quick solution reference that worked for me on my IMac with OS Sequoia 15.3. I assume you have Docker installed, and you are somewhat familiar with opening a terminal in your computer and typing into it, navigating directories, etc... (but not a lot more really). 

It goes like this:

1. Figure out where your Stata license file is. Just google if you have no idea. Copy it into your working directory.
2. If you don't need to install any packages, or intend to do it inside your do files, just type this from the root of your project. The part ```stata18-se:2024-12-18``` can and should be changed according to your license and preferences. The full list of images:tags is available [at the dataeditors docker hub](https://hub.docker.com/u/dataeditors)

	``` 
	docker run --init -it --rm \
			--mount "type=bind,source=${PWD}/stata.lic,target=/usr/local/stata/stata.lic" \
				-v "${PWD}/my_project_do_files":/project dataeditors/stata18-se:2024-12-18
	```
		
2. If you want to install packages inside your image, you need some more work. First, copy your license file into the directory where the Dockerfile will be saved. I usually have an "Environment" directory for it. Inside it, create a setup.do file that installs them. E.g. ```ssc install regdhfe``` etc... 
3. Create a Dockerfile with the following content (with filename: Dockerfile, no extension). Most of it shoudl be self-explanatory. Note that you cannot place your license and setup.do files elsewhere. They must be in the same directory as the Dockerfile. You can avoid copying the stata.lic file but then you'll have to mount it upon container execution as in the previous step. This may be something you want to do if you intend to distribute the image. 

	```
	FROM dataeditors/stata18-se:2024-12-18

	#copy the stata license
	COPY stata.lic /usr/local/stata/stata.lic 
	USER statauser:stata
	ENV PATH "$PATH:/usr/local/stata" 

	# create a working directory for setup
	# and execute the setup.do file
	WORKDIR /setup
	COPY setup.do setup.do
	RUN stata-se -b setup.do 

	# mount your project root directory here when you create a container (see below) 
	WORKDIR /project
	```

4. Build the image from the directory where all these files are (substitute . for the directory where you placed the Dockerfile, if elsewhere than your working directory). However, keep in mind that files copied into the image (previous step) my be in the same dir. 

	```
	docker build -t stataimg .
	``` 

3. Change directory to the root of your project. Run the following to open up an interactive stata interface. The -v flag is mounting a local directory into the container's tree ($PWD stands for present-working-directory, you have to indicate the entire path from the root if you don't want to use the variable). The directory after the colon is where your local path will be mounted into the container - it should be consistent with the WORKDIR indicated in the Dockerfile. My solution assumes your do files are in a subdirectory of the present working directory called my_project_do_files. That's where output/dta files/etc... will be saved by your stata scripts. If you want a more complex directory structure, make sure its root is mounted to /project, which is defined as the working directory inside the Dockerfile

	``` 
	docker run --init -it --rm \
				-v "${PWD}/my_project_do_files":/project \
				stataimg
	```
You can also batch-run a do file by adding after ```stataimg``` ```-b dofile.do``` where dofile.do is inside the directory you mount with the -v flag above. This is what you should do when preparing a replication package, to minimize replicator's typing. 

That's all. Let me know if it does not work for you. 