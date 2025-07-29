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

    # usamos metoddos especiais __getitem__ e __setitem__ para permitir o acesso e modificação de elementos da lista usando a notação de colchetes, como em listas normais. Com sobre carga de operadores: a = lista[6]. Sem sobrecarga de operadores: a = lista.get(6).
    def __getitem__(self, posicao_desejada):
        ponteiro = self.head
        # percorremos a lista até o índice desejado
        for i in range(posicao_desejada):
            # se o ponteiro não for None, seguimos para o próximo nó
            if ponteiro:
                ponteiro = ponteiro.next
            else:
                raise IndexError("list index out of range")
        # se o ponteiro não for None, retornamos o dado do nó
        if ponteiro:
            return ponteiro.data
        raise IndexError("list index out of range")

    def __setitem__(self, posicao_desejada, elem):
        ponteiro = self.head
        for i in range(posicao_desejada):
            if ponteiro:
                ponteiro = ponteiro.next
            else:
                raise IndexError("list index out of range")
        if ponteiro:
            # se o ponteiro não for None, atualizamos o dado do nó
            ponteiro.data = elem
        else:
            raise IndexError("list index out of range")

    def index(self, elemento):
        # Retorna o índice do elem na lista
        pointer = self.head
        indice = 0
        # Percorremos a lista até encontrarmos o elemento ou chegarmos ao final da lista
        while pointer:
            # Se o dado do nó atual for igual ao elemento procurado, retornamos o índice
            if pointer.data == elemento:
                return indice
            pointer = pointer.next
            indice = indice + 1
        raise ValueError("{} is not in list".format(elemento))
