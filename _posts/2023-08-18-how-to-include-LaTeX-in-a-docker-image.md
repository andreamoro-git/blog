---
tags: tips
---
# How to include a LaTeX distribution inside a docker image

I recently had to prepare a replication package for a paper I wrote. The replication package included a Python script that generated some figures using matplotlib with some LaTeX formatting. I wanted to use docker to ensure that the script would run on any machine without the need to install any dependencies (see [this recommendation from AEA's data editor](https://aeadataeditor.github.io/posts/2021-11-16-docker)). 

Instructions on how to include LaTeX inside a docker image are scarce. One of the challenges of running LaTeX inside a Docker container is that standard LaTeX distributions are large, and there have been reports of Docker not working well with them. However, a solution is to use a minimal LaTeX distribution like [TinyTeX](https://yihui.org/tinytex/). To add TinyTeX to your Dockerfile, simply include the following lines:

```
# install perl and wget if you don't have them already
# my debian distribution had perl but was missing some libraries. This fixed it.  
RUN apt-get update
RUN apt-get install perl wget -y  

# fetch TinyTeX installer and run it
RUN wget -qO- "https://yihui.org/tinytex/install-bin-unix.sh" | sh 

# add TinyTeX to PATH variable
ENV PATH="$PATH:/root/.TinyTeX/bin/x86_64-linux"
```

From here, run bash in your container, compile your latex file, and check what packages are missing. For example, you may get a message such as ```! LaTeX Error: File `type1cm.sty' not found.```
In this case, from inside a container run ```tlmgr search --global --file "type1cm.sty"``` which will output something like this:
```
tlmgr: package repository https://ctan.mirror.garr.it/mirrors/ctan/systems/texlive/tlnet (not verified: gpg unavailable)
type1cm:
	texmf-dist/tex/latex/type1cm/type1cm.sty
```
then, add the following line to your Dockerfile:
```
RUN tlmgr install type1cm
```

Repeat this process until you have all the packages you need. In my case also needed to add dvipng, required by Python's matplotlib package:
```
RUN apt-get install dvipng -y
```

For some reason, in my image (based on python:3.9-slim) the dvipng installation needed to be done *after* the TinyTeX installation, otherwise some misterious version conflict would appear which I didn't really have time to investigate further.

My full Dockerfile is [here](https://github.com/andreamoro-git/JurySelection-Replication_Package/blob/main/Environment/Dockerfile)
