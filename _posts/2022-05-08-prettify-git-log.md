---
tags: tips
---
# How to prettify and get a more efficient output from ```git log```

I am not satisfied with the output of git log and any of its optional arguments: too much information or too little, and hard to read. I created a simple alias that outputs 
one line per commit with, in order: hastag, day and time of commit, (branch, tag info), and commit message. This is all one needs 99% of the times. 

```
d09e1b8 2021-08-19 17:59:20 -0500 added code
e470a9e 2021-08-19 15:57:26 -0500 added data
c6b5de1 2021-08-19 04:29:36 -0500 Initial commit
```

The alias also colorizes the columns, outputs the last 20 commits by default but accepts an optional -n argument at the end.
The command to store it globally is the following:

```
git config --global alias.logs "log -20 --pretty='%C(yellow)%h%C(cyan) %ai%C(auto)%d %Creset%s'"
```

Type ```git logs``` and enjoy!
