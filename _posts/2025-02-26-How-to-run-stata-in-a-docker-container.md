---
tags: tips
---
# How to run Stata inside a Docker container

Lars Vilhuber, the AEA data editor, has made available a set of Docker images for Stata at [this github repository](https://github.com/AEADataEditor/docker-stata?tab=readme-ov-file). I decided to give it a try with the purpose of streamlining the grading of my PhD class computer homework. As I should have expected, it took me the good part of a day to make it work. 

Lars's instructions are more comprehensive (and didn't work for me, I'm sure it's my fault),  I am posting a quick solution reference that works for me, with a plan to fix it later. It goes like this:

1. Figure out where your Stata license file is. Just google if you have no idea. Copy it into your working directory.
2. Use this Dockerfile. The part stata18-se-i:2024-12-18 can and should be changed according to your license and preferences. The full list of images:tags is available [here](https://hub.docker.com/u/dataeditors)

	```
	FROM dataeditors/stata18-se-i:2024-12-18

	# create a working directory (not necessary but keeps things tidy)
	WORKDIR /project/
	```

2. Build the image (substitute . for the directory where you placed the Dockerfile)

	```
	docker build -t stataimg .
	``` 

3. Run the following to open up an interactive stata interface. The -v part assumes your do files are in a subdirectory of the current working directory called my_project_do_files. That's where output/dta files/etc... will be saved. If you want a more complex structure, make sure its root is mounted to /project, which is defined as the working directory inside the Dockerfile

	``` 
	docker run --init -it --rm \
				--mount "type=bind,source=${PWD}/stata.lic,target=/usr/local/stata/stata.lic" \
				-v "${PWD}/my_project_do_files":/project \
				stataimg
	```

You can also batch-run a do file by adding after ```stataimg``` ```-b dofile.do``` where dofile.do is inside the directory you mount with the -v flag above. 

