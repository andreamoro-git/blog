---
tags: tips
---

# How to generate a list of tables indicating the code line numbers where they are generated

The [README template for Replication packages](https://social-science-data-editors.github.io/template_README/) 
recommends including a list of tables and programs identifying the tables and figures as they appear in the manuscript, by number,
and the line of code that generated them. 

The following instructions should help generate this table starting from a LaTeX file. The code works for figure floats but should be easily 
adaptable for tables 

### Get figure numbers and figure filenames form your LaTeX. 

Include this code in the preamble of your latex file to generate a nice list (you need to adapt it for the list of tables but it should be intuitive)
(hat tip: https://stackoverflow.com/questions/66551105/lazy-quantifier-for-an-exact-word-in-large-text-with-newlines/66555601#66555601)
```
\newwrite\myfile
\immediate\openout\myfile=\jobname.foo
\def\figurestring{figure}

\usepackage{xpatch}
\makeatletter
\xapptocmd{\label}{%
  \@ifundefined{@captype}{}{%
  \ifx\@captype\figurestring%
    \immediate\write\myfile{#1}%
  \fi%
  }%
}{}{}
\xapptocmd{\Gin@ii}{%
  \@ifundefined{@captype}{}{%
  \ifx\@captype\figurestring%
    \immediate\write\myfile{l.\the\inputlineno\space\thefigure\space #2}%
  \fi%
  }%
}{}{}
\makeatother

```

### Prepare the file for parsing
Take your output from step 1 [LaTeXfilename].foo. The file  It will look like this. 

!(https://pbs.twimg.com/media/E3D1h2ZWYAIMWWM?format=jpg&name=large)
The goal is to get a clean list of filenames, therefore remove the first 2columns (latex file line # and figure #). 
You also may need to do some editing to ensure filenames can be found in your code. I had to remove the directory since I 
code it programmatically, and I also remove the .pdf extension

### Parse the file

To find where your code generates that code, you need to pass this file to a grep command. Long story short:  
open your terminal and shoot this command:
```
while read line; do grep -n "$line" *; done < [LaTeXfilename].foo
```

!(https://pbs.twimg.com/media/E3D1P1kX0AAG-N1?format=jpg&name=large)
