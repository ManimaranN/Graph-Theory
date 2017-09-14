from graphviz import Graph

dot = Graph(comment='Graph')

n = input("Enter no.of Edges : ")
for i in range(0,n):
    edge = raw_input().split(' ')
    dot.edge(edge[0],edge[1],label=edge[2])

print(dot.source)
dot.save('file.gv')
dot.render('file.gv', view=True)