class Node(object):
    def __init__(self, key):
        self.key = key
        self.children = None
        self.dad = ''

    def BFS(self, key):
        print('\n-----------Busca-----------')
        return _BFS([self], key)


def _BFS(nodes, key):
    filhos = []
    if nodes:
        for item in nodes:
            print(item.key)
            if item.key == key:
                print('-----------Fim da Busca-----------')
                return item
            elif item.children:
                i = 0
                while i < len(item.children):
                    item.children[i].dad = item.key
                    i += 1
                filhos += item.children
        print('Proxima camada')
        return _BFS(filhos, key)
    else:
        return None
