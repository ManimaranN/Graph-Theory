from graphviz import Graph

dot = Graph(comment='Graph')


n = input("Enter no.of Edges : ")

temp = []

for i in range(0,n):
    edge = raw_input().split(' ')
    if(edge[0] == edge[1]):
    	print "Self Loops are not Accepted"
    	continue
    if((edge[1],edge[0]) in temp):
    	print "Parallel Edges are not Accepted"
    	continue
    temp.append((edge[0],edge[1]))
    dot.edge(edge[0],edge[1],label=edge[2])

print(dot.source)  # doctest: +NORMALIZE_WHITESPACE
dot.save('file.gv')
dot.render('file.gv', view=True)

