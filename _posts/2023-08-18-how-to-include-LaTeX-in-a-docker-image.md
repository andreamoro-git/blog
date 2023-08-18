---
tags: tips
---
# How to include a LaTeX distribution inside a docker image

I needed to include LaTeX in a docker image to compile a latex file from within a python script, but
instructions on how to include LaTeX in a docker image are scarce. One of the issues with running LaTeX 
inside a docker container is that standard 
LaTeX distributions are huge, and I have read some reports of docker not working with them.
The solution is to use a minimal LaTeX distribution, such as [TinyTeX](https://yihui.org/tinytex/). 
To do so you need to add the following lines to your Dockerfile:

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
In this case, run ```tlmgr search --global --file "type1cm.sty"``` which will output something like this:
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

For some reason, in my image (based on python:3.9-slim) the dvipng installation needed to be done *after* the TinyTeX installation, otherwise some misterious version conflict would appear.

My full Dockerfile can be found [here](https://github.com/andreamoro-git/JurySelection-Replication_Package/blob/main/Environment/Dockerfile)
