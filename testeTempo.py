#Programa feito pra testar a correlação entre o número de placas a serem ordenadas e o tempo de execução da função de ordenação

import cPlaca
import mercoSort
import random
import time

def randPlaca():
    #Retorna um objeto cPlaca aleatório
    placa = []
    for i in range(7):
        #Gera 7 dígitos aleatórios no padrão LLLNLNN (L = Letra; N = Número)
        if i < 3 or i == 4:
            #Gera uma letra aleatória
            placa.append(str(chr(random.randint(65,90))))
        else:
            #Gera um algarismo decimal aleatório
            placa.append(str(random.randint(0,9)))
    return cPlaca.cPlaca(''.join(placa))

def randLista(n):
    #Gera uma lista de n objetos cPlacas aleatórios
    lista = []
    for i in range(n):
        lista.append(randPlaca())
    return lista

def testeMercoSort(lista):
    #Retorna o tempo que levou para ordenar a lista de placas inserida.
    inicio = time.time()
    lista = mercoSort.radixSort(lista)
    final = time.time()
    return final - inicio

casos = input("Insira o número de placas que você quer utilizar em cada teste, separados por espaço:").split()
for i in range(len(casos)):
    #Conversão dos números inseridos de string para inteiros
    casos[i] = int(casos[i])

casosResultado = []
for i in range(len(casos)):
    #O resultado salvo pra cada teste é uma média aritmética entre dois testes com o caso em questão, para maior precisão dos resultados
    print(f'Testando caso {i+1}...')
    casosResultado.append(round(testeMercoSort(randLista(casos[i]))+round(testeMercoSort(randLista(casos[i]))))/2)

relatorio = ""
for i in range(len(casos)):
    #Geração do relatório com os resultados
    relatorio += f'O caso com {casos[i]} placas levou uma média de {casosResultado[i]} segundos para ser ordenado. Dois testes foram realizados.\n'
relatorioFile = open("resultados.txt",'a')
relatorioFile.write(relatorio)
relatorioFile.close()

print("Resultados salvos em resultados.txt. Conteúdo do arquivo:")
print(relatorio)
