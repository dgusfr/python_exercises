from node import Node


class LinkedList:
    def __init__(self):
        # A lista encadeada é uma sequecia de nos, onde um sab onde o outro esta, então sabendo um no, podemos acessar os outros. O atribuito Head é a referencia para esse primeiro nó, como a lista se inicia vazia, head é None.
        self.head = None
        # Atributo para armazenarmos o tamanho da lista
        self._size = 0

    def insere_final_lista(self, elemento):
        # Se isso é verdade, temos elementos na lista:
        if self.head:
            # inserção quando a lista já possui elementoentos
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(elemento)
        # Se não tivermos elementos na lista, então o head é None, e devemos criar o primeiro nó.
        else:
            # aqui estamos pássando o 'elemento' para o construtor do nó como oparametro 'data' da classe Node, realizando assim a primeira inserção:
            self.head = Node(elemento)
        self._size = self._size + 1

    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size

    def _getnode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")  # return None
        return pointer

    def set(self, index, elemento):
        # lista.set(5, 9)
        pass

    def __getitem__(self, index):
        # a = lista[6]
        pointer = self._getnode(index)
        if pointer:
            return pointer.data
        else:
            raise IndexError("list index out of range")

    def __setitem__(self, index, elemento):
        # lista[5] = 9
        pointer = self._getnode(index)
        if pointer:
            pointer.data = elemento
        else:
            raise IndexError("list index out of range")

    def index(self, elemento):
        """Retorna o índice do elemento na lista"""
        pointer = self.head
        i = 0
        while pointer:
            if pointer.data == elemento:
                return i
            pointer = pointer.next
            i = i + 1
        raise ValueError("{} is not in list".format(elemento))

    def insert(self, index, elemento):
        node = Node(elemento)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getnode(index - 1)
            node.next = pointer.next
            pointer.next = node
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
            pointer = self.head.next
            while pointer:
                if pointer.data == elemento:
                    ancestor.next = pointer.next
                    pointer.next = None
                    self._size = self._size - 1
                    return True
                ancestor = pointer
                pointer = pointer.next
        raise ValueError("{} is not in list".format(elemento))

    def __repr__(self):
        r = ""
        pointer = self.head
        while pointer:
            r = r + str(pointer.data) + "->"
            pointer = pointer.next
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
