
nomes = ["Adriano",	"Adrian", "Adão", "Adam", "Ana", "Ann", "Anne", "Anna", "Antônio", "Anthony", 
"Beatriz", "Beatrice", "Brigite","Bridget", "Carlos", "Charles", "Davi", "David", "Eduardo", "Edward",
"Estêvão", "Steve", "Eva", "Eve", "Guilherme", "William", "Jorge", "George", "José", "Joseph", "João",
"John", "Leonardo",	"Leonard", "Luiz", "Luis", "Louis", "Marcos", "Marc", "Mark", "Maria", "Mary",
"Mateus", "Matthew", "Miguel", "Michael", "Nicolau", "Nicholas", "Noé",	"Noah", "Paulo", "Paul", "Pedro",
"Peter", "Raimundo", "Raymond", "Raquel", "Rachel", "Ricardo", "Richard", "Rick", "Roberto", "Robert",
"Rosa", "Rose", "Sara", "Sarah", "Suzana", "Susan", "Tiago", "James", "Tomás", "Thomas"]

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

#print (pesquisa_binaria(nomes, "Luis"))

token = 0
for word in nomes:
	print (token + 1, word)
	token += 1

print (len(nomes))