from arvore import *

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g1 = Node('g')
g2 = Node('g')
h = Node('h')

c.children = [Node('i')]
d.children = [Node('i')]
b.children = [c, d]
g1.children = [Node('i')]
g2.children = [Node('i')]
f.children = [g1]
e.children = [f, g2]
h.children = [Node('i')]
a.children = [h, e, b]

#  a
# / |  \
# h e   b
# | |\  |\
# i f g c d
# | | | |
# g i i i
# |
# i

result = a.BFS('i')

print('Resultado: ' + result.key)
print('Pai: ' + result.dad)
