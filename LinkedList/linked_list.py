from node import Node


class LinkedList:
    def __init__(self):
        # A lista encadeada é uma sequecia de nos, onde um sab onde o outro esta, então sabendo um no, podemos acessar os outros. O atribuito Head é a referencia para esse primeiro nó, como a lista se inicia vazia, head é None.
        self.head = None
        # Atributo para armazenarmos o tamanho da lista
        self._size = 0

    def insere_final_lista(self, elemento):
        # Se isso é verdade, temos elementos na lista, e seguimos a seguinte logica para inserir o elemento no final da lista:
        if self.head:
            # Usamos a variavel auxiliar ponteiro que aponta para Head (Proximo elemento da lista)
            ponteiro = self.head
            # Enquanto o ponteiro.next não for None (ou seja, não tiver chegado no final da lista), continuamos percorrendo a lista
            while ponteiro.next:
                ponteiro = ponteiro.next
            # Quando chegamos no final da lista, o ponteiro.next é None, e podemos inserir o novo nó com o elemento no final da lista
            ponteiro.next = Node(elemento)
        # Se não tivermos elementos na lista, então o head é None, e devemos criar o primeiro nó.
        else:
            # aqui estamos pássando o 'elemento' para o construtor do nó como oparametro 'data' da classe Node, realizando assim a primeira inserção:
            self.head = Node(elemento)
        self._size = self._size + 1

    def tamanho_lista(self):
        return self._size

    def _getnode(self, index):
        ponteiro = self.head
        for i in range(index):
            if ponteiro:
                ponteiro = ponteiro.next
            else:
                raise IndexError("list index out of range")  # return None
        return ponteiro

    # usamos metoddos especiais __getitem__ e __setitem__ para permitir o acesso e modificação de elementos da lista usando a notação de colchetes, como em listas normais. Com sobre carga de operadores: a = lista[6]. Sem sobrecarga de operadores: a = lista.get(6).
    def __getitem__(self, index):
        ponteiro = self._getnode(index)
        if ponteiro:
            return ponteiro.data
        else:
            raise IndexError("list index out of range")

    def __setitem__(self, index, elemento):
        # lista[5] = 9
        ponteiro = self._getnode(index)
        if ponteiro:
            ponteiro.data = elemento
        else:
            raise IndexError("list index out of range")

    def index(self, elemento):
        """Retorna o índice do elemento na lista"""
        ponteiro = self.head
        i = 0
        while ponteiro:
            if ponteiro.data == elemento:
                return i
            ponteiro = ponteiro.next
            i = i + 1
        raise ValueError("{} is not in list".format(elemento))

    def insert(self, index, elemento):
        node = Node(elemento)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            ponteiro = self._getnode(index - 1)
            node.next = ponteiro.next
            ponteiro.next = node
        self._size = self._size + 1

    def remove(self, elemento):
        if self.head == None:
            raise ValueError("{} is not in list".format(elemento))
        elif self.head.data == elemento:
            self.head = self.head.next
            self._size = self._size - 1
            return True
        else:
            ancestor = self.head
            ponteiro = self.head.next
            while ponteiro:
                if ponteiro.data == elemento:
                    ancestor.next = ponteiro.next
                    ponteiro.next = None
                    self._size = self._size - 1
                    return True
                ancestor = ponteiro
                ponteiro = ponteiro.next
        raise ValueError("{} is not in list".format(elemento))

    def __repr__(self):
        r = ""
        ponteiro = self.head
        while ponteiro:
            r = r + str(ponteiro.data) + "->"
            ponteiro = ponteiro.next
        return r

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    # sequencial = []
    # sequencial.insere_final_lista(7)
    lista = LinkedList()
    lista.insere_final_lista(7)
    lista.insere_final_lista(80)
    lista.insere_final_lista(56)
    lista.insere_final_lista(32)
    lista.insere_final_lista(17)
