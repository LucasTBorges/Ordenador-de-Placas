#Método que possui a implementação do algoritmo Radix Sort e os sub-algoritmos nos quais ele se baseia, adaptados para funcionar com placas no padrão Mercosul, que possui letras e números.

def countingSort(lista, indice):
    #Iteração do algoritmo de ordenação counting sort se baseando no dígito do índice especificado no parâmetro indice.
    #Utiliza o dígito em questão e ordena a lista se baseando nele e utilizando como critério de desempate a posição dele na lista.

    if(indice == 3 or indice == 5 or indice == 6):
        #Verifica se o dígito no qual essa iteração do counting sort vai se basear é um número. Nesse caso, trabalha no intervalo de 0 a 9.
        ocorrencias = [0]*10
        contador = 0
        tamanho = 0
        for i in lista:
            #loop para contar o número ocorrências de um determinado algarismo
            ocorrencias[i[indice]] += 1
            tamanho += 1
        ocorrenciasCopy=ocorrencias.copy()
        for i in range(10):
            #Modificação da lista de ocorrências adicionando os valores anteriores da lista
            contador += ocorrencias[i]
            ocorrencias[i] = contador
        lista_ordenada = [0] * tamanho
        for i in reversed(lista):
            #Posicionamento de acordo com o número de ocorrências de cada algarismo na posição do dígito na lista.
            #É importante utilizar o iterador reverso pois por padrão o counting sort coloca na lista num índice maior aquelas que vieram primeiro, e nós queremos o contrário.
            lista_ordenada[ocorrencias[i[indice]]-1] = i
            ocorrencias[i[indice]] -= 1
    else:
        #No caso do dígito ser uma letra, trabalha no intervalo de 0 a 25 (representando as letras do alfabeto de A a Z)
        ocorrencias = [0]*26
        contador = 0
        tamanho = 0
        for i in lista:
            #loop para contar o número ocorrências de uma determinada letra
            ocorrencias[i[indice]] += 1
            tamanho += 1
        ocorrenciasCopy=ocorrencias.copy()
        for i in range(26):
            #Modificação da lista de ocorrências adicionando os valores anteriores da lista
            contador += ocorrencias[i]
            ocorrencias[i] = contador
        lista_ordenada = [0] * tamanho
        for i in reversed(lista):
            #Posicionamento de acordo com o número de ocorrências de cada letra na posição do dígito na lista
            #É importante utilizar o iterador reverso pois por padrão o counting sort coloca na lista num índice maior aquelas que vieram primeiro, e nós queremos o contrário.
            lista_ordenada[ocorrencias[i[indice]]-1] = i
            ocorrencias[i[indice]] -= 1
    return lista_ordenada
                  
def radixSort(lista):
    #Algoritmo de ordenação que utiliza o Counting Sort como sub-algoritmo para ordenar um vetor.
    for i in range(6,-1,-1):
        #loop que aplica o counting sort pra cada dígito dos itens da lista, do dígito menos significativo para o mais significativo.
        lista = countingSort(lista, i)
    return(lista)
