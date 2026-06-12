---
tags: tips
---
# How to prettify and get a more efficient output from ``git log``

I am not satisfied with the output of git log and any of its optional arguments: too much information or too little, and hard to read. I created a simple alias that outputs
one line per commit with, in order: hastag, day and time of commit, (branch, tag info), and commit message. This is all one needs 99% of the times.

<pre>
<span style="color:yellow;">173ab88</span><span style="color:cyan;"> 2026-06-12 17:13:14 +0200</span><span style="color:yellow;"> (</span><span style="font-weight:bold;color:cyan;">HEAD</span><span style="color:yellow;"> -> </span><span style="font-weight:bold;color:green;">main</span><span style="color:yellow;">, </span><span style="font-weight:bold;color:red;">origin/main</span><span style="color:yellow;">, </span><span style="font-weight:bold;color:red;">origin/HEAD</span><span style="color:yellow;">)</span> sorting of roster <span style="color:#88ccaa;">andrea-bigair
</span><span style="color:yellow;">66506ee</span><span style="color:cyan;"> 2026-06-12 08:03:31 -0500</span> corruption fix <span style="color:#88ccaa;">moroa ACCRE
</span><span style="color:yellow;">3d1a7b2</span><span style="color:cyan;"> 2026-06-12 07:59:22 -0500</span> easier reinstall <span style="color:#88ccaa;">moroa ACCRE
</span><span style="color:yellow;">4894226</span><span style="color:cyan;"> 2026-06-12 14:45:40 +0200</span> fixed reassignmet status <span style="color:#88ccaa;">andrea-bigair
</span>
</pre>


The alias also colorizes the columns, outputs the last 20 commits by default but accepts an optional -xxx argument at the end to output a different number of commits (xxx is such number).
The command to store it globally is the following:

```
git config --global alias.logs "log -20 --pretty='%C(yellow)%h%C(cyan) %ai%C(auto)%d %Creset%s %C(#88ccaa)%aN'"
```

Type ``git logs`` and enjoy!
