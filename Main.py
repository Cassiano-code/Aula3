from Lista import Lista


lista = Lista()


lista.adicionar( 1 )
lista.adicionar( 2 )
lista.adicionar( 3 )
print( "Tamanho da Lista: " + str( lista.tamanho ))
lista.imprimir()

valor = input("Digite um valor: ")
lista.adicionar( valor )
lista.imprimir()


resp= int(input("Deseja imprimir a lista de forma inversa? 1- Sim 2- Não"))
if resp == 1:
    lista.reversed()
else:
    print("Imprimindo de forma normal: ")
    lista.imprimir()
