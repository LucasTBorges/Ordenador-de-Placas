import cPlaca
import mercoSort
from pathlib import Path


def jaExiste(arquivo, n=2):
    #Função para checar se já existe um arquivo com o nome "PIVsOrd.piv" e utilizar um nome PIVsOrd(x).piv se for necessário, para não
    #misturar diferentes bancos de dados de placas ordenadas que, por ventura, estejam armazenados no mesmo diretório, frutos de usos prévios deste programa.
    if Path(arquivo).is_file():
        if not Path("PIVsOrd(1).piv").is_file():
            #Caso não haja nenhum PIVsOrd(x).piv, um "PIVsOrd(1).piv" será criado.
            return "PIVsOrd(1).piv"
        else:
            #Caso já exista um PIVsOrd(x).piv, será testado se já existe um PIVsOrd(x+1).piv, e mantê-lo se o nome estiver disponível.
            if Path(f'PIVsOrd({n}).piv').is_file():
                return jaExiste(arquivo, n+1)
            else:
                return f'PIVsOrd({n}).piv'
    else:
        #Caso o nome de arquivo testado esteja disponível, retorna o próprio nome testado.
        return arquivo

def getArquivoNome():
    #Função para buscar o nome do arquivo
    print("Insira o nome do arquivo a ser lido (com a extensão)")
    print("Obs: Se campo for deixado em branco, o arquivo PIVs.piv será procurado por padrão")
    nome = input("Insira o nome do arquivo: ")
    if nome == "" or nome == "\n" or nome == None:
        return "PIVs.piv"
    if Path(nome).is_file():
        return nome
    else:
        print(f'Arquivo {nome} não encontrado, verifique se o nome foi digitado corretamente e se a extensão foi incluída, então tente novamente.\n')
        return getArquivoNome()

def OrdenarArquivo(nome, lista):
    #Função para ordenar o arquivo inserido pelo usuário.
    print(f'Abrindo arquivo {nome}')
    try:
        with open(nome,'r') as pivs:
            #Lendo o arquivo
            placa = pivs.readline()
            while placa != '' and placa != '\n':
                #Adicionando os elementos do arquivo em uma lista como objetos cPlaca
                lista.append(cPlaca.cPlaca(placa))
                placa = pivs.readline()
        print("Ordenando a lista. Por favor, aguarde.")
        lista = mercoSort.radixSort(lista)
        novoArquivo_Nome = jaExiste("PIVsOrd.piv")
        novoArquivo = open(novoArquivo_Nome, 'a')
        for i in lista:
        #Escrita dos elementos em ordem no novo arquivo.
            novoArquivo.write(str(i) + '\n')
        novoArquivo.close()
        print(f'Novo arquivo com a base de dados de nome {novoArquivo_Nome} criado com sucesso.')
    except:
        print("Esse arquivo não parece estar formatado corretamente (Uma placa no padrão mercosul por linha). Tente novamente\n")
        OrdenarArquivo(getArquivoNome(), lista)

lista = []
OrdenarArquivo(getArquivoNome(), lista)


