---
tags: tips
---
# How to generate a list of tables for replication packages

The [README template for Replication packages](https://social-science-data-editors.github.io/template_README/) 
recommends including a list of tables and programs identifying the tables and figures as they appear in the manuscript, by number,
and the line of code that generated them. 

The following instructions should help generate this table starting from a LaTeX file. The code works for figure floats but should be easily 
adaptable for tables 

### 1. Get figure numbers and figure filenames form your LaTeX. 

Include this code in the preamble of your latex file to generate a nice list (you need to adapt it for the list of tables but it should be intuitive)
(hat tip: https://stackoverflow.com/questions/66551105/lazy-quantifier-for-an-exact-word-in-large-text-with-newlines/66555601#66555601)

```
\newwrite\myfile
\immediate\openout\myfile=\jobname.foo
\def\figurestring{figure}

\usepackage{xpatch}
\makeatletter
\xapptocmd{\label}{ %
  \@ifundefined{@captype}{}{ %
  \ifx\@captype\figurestring%
    \immediate\write\myfile{#1} %
  \fi%
  }%
}{}{}
\xapptocmd{\Gin@ii}{ %
  \@ifundefined{@captype}{}{ %
  \ifx\@captype\figurestring%
    \immediate\write\myfile{l.\the\inputlineno\space\thefigure\space #2}%
  \fi%
  }%
}{}{}
\makeatother
```

### 2. Prepare the file for parsing
Take your output from step 1 [LaTeXfilename].foo. The file  It will look like this. 

![figure filenames]({{ site.url }}/blog/assets/images/imgnames.png)

The goal is to get a clean list of filenames, therefore remove the first 2columns (latex file line # and figure #). 
You also may need to do some editing to ensure filenames can be found in your code. I had to remove the directory since I 
code it programmatically, and I also remove the .pdf extension

### 3. Parse the file

To find where your code generates that code, you need to pass this file to a grep command. Long story short:  
open your terminal and shoot this command:
```
while read line; do grep -n "$line" *; done < [LaTeXfilename].foo
```
You'll get something like this, i.e. filename : line # : matched string, which you can then easily combine with the figure numbers generate above and turn into a table for your README. Double-check since it produces no output if it doesn't find any match. That's it hope it helps.

![code locations]({{ site.url }}/blog/assets/images/codelocs.png)

I suppose if you have a better process this may be automagically done but I don't. 
I change figure names all the time! Feel free to send me your own tips
