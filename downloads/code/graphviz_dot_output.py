##
# export_graph()
#   Saves the graph to a dot file
#   graph : a mapping of vertices to sets of vertices
#           (adjacency map form)
##
def export_graph(graph, color=None):
  # Map integer colorings to graphviz colors
  cmap = {  
           0 : 'brown',
           1 : 'maroon2', 
           2 : 'orangered', 
           3 : 'crimson',
           4 : 'lightseagreen',
           5 : 'gold', 
           6 : 'cyan', 
           7 : 'plum',
           8 : 'salmon'
         }

  with open('rig.dot', 'w') as f:
    f.write('graph G {\n')

    # For each vertex u in the graph
    for u in graph.keys():
      # Add coloring information
      if color: 
        f.write('  "%s" [color=%s, style=filled];\n' % (u, cmap[color[u]]));

      # For each neighbor v of u, add the edge
      for v in graph[u]: 
        if (u < v):
          f.write('  "%s" -- "%s";\n' % (u, v))

    f.write('}\n')
