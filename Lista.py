from No import No

class Lista: 

    def __init__(self):
        self.inicio = None
        self.tamanho = 0
        self.final = None


    def __len__(self):
        return self.tamanho 

    def adicionar(self, valor ):
        if self.inicio: 
            aux = self.inicio
            while( aux.proximo ):
                aux = aux.proximo
            aux.proximo = No( valor )
        else:
            self.inicio = No( valor )
        self.tamanho = self.tamanho + 1   

    def imprimir(self):
        if self.inicio == None:
            print("Lista Vazia")

        aux = self.inicio
        while( aux ):
            print( aux.dado , "\n" )
            aux = aux.proximo
        print( "Tamanho da Lista: " + str(self.tamanho ))

    def reversed(self, valor):
        no = No(valor)
        print("chegou!")
        self.inicio = self.fim = no
        aux = self.inicio
        while( aux ):
            print( aux.dado , "\n" )
            aux = aux.proximo

            
        print( "Tamanho da Lista: " + str(self.tamanho ))
        
