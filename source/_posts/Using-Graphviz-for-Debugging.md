title: Visualizing Graphs in Program Output
date: 2016-03-08 15:46:44
tags:
---

Many computer science problems utilize [graph][1]-based data structures.  Their use can range from explicit inclusion in an algorithm-centric problem (like path-finding) to a more "behind-the-scenes" presence in Bayesian networks or descriptions of finite automata.  Unfortunately, visualizing large graphs can be difficult to do, especially for debugging.  Unlike lists or dictionaries, which can be represented clearly by plain text printing, depicting a graph tends to require more graphics overhead than is reasonable for most programmers to write simply for debugging purposes.  I've found that [Graphviz][2], a free graph visualization utility, can be quite useful in debugging graph-related programs.

Installing Graphviz
-------------------

If you're on a Debian-based Linux OS (e.g. Ubuntu), you can install Graphviz using `apt-get`.  Just run `$ sudo apt-get install graphviz` and you'll have everything you need to complete the steps in this blog post.  Mac OS X users can use `brew` equivalently.

Windows users should install using a binary downloaded from the [Graphviz Windows page][3], but there might be some issues with setting the `PATH` variable for running in the commandline.

Making a basic graph
--------------------

Once you've installed, the next thing you'll want to do is create a basic graph to ensure the installation succeeded and to gain practice using Graphviz tools.  We do this by creating a `*.dot` file that describes the graph we wish to display.  If you're the type of person who likes to jump right in and experiment first before reading too much, or if you love formal language specification, the [DOT grammar][4] is fairly readable and can give a quick introduction to creating DOT files.

The below is a fairly representative DOT file to demonstrate some of the capabilities of Graphviz. Open your favorite text editor, copy/paste it in, and save it as `firstgraph.dot`:

```
```

Examples
--------



[1]: https://en.wikipedia.org/wiki/Graph_%28discrete_mathematics%29
[2]: http://graphviz.org/
[3]: http://graphviz.org/Download_windows.php
[4]: http://www.graphviz.org/content/dot-language
