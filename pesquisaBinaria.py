def pesquisa_binaria(lista, item):
	# baixo e alto acompanham a parte da lista que você está procurando.
	baixo = 0
	alto = len(lista) -1

	# enquanto ainda não conseguiu chegar a um único elemento...
	while baixo <= alto:
		#... verifica o elemento central.
		meio = (baixo + alto)//2
		chute = lista[meio]

		# acha o item
		if chute == item:
			return meio
    # o chute foi muito alto
		if chute > item:
			alto = meio -1
    # o chute foi muito baixo
		else:
			baixo = meio + 1
  # o item não existe
	return None

# vamos testar o algoritmo
minha_lista = [1, 3, 5, 7, 9]

# lembre-se, as listas começam com 0. O elemento 7 está no indice 3.
print (pesquisa_binaria(minha_lista, 7)) # => 1
# "None" significa nulo em Python. Ele indica que o item não foi encontrado.
print (pesquisa_binaria(minha_lista, -1)) # => None