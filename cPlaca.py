#Este é o módulo que possui a classe cPlaca, cuja instância é capaz de armazenar o código de identificação de veículo de uma placa de carro no padrão Mercosul.

class cPlaca:
	
	#Função construtora: inicializa a instância da classe com 8 atributos, um para cada caractere no código de identificação e converte todas as letras para letras maiúsculas.
	#Cada atributo é nomeado com uma letra correspondente ao tipo de dígito (L para letra, N para número) + um número correspondente ao índice do caractere na string (0 a 6).
	#Os dígitos do tipo letra são armazenados como inteiros que correspondem ao índice da letra em questão no alfabeto.
	def __init__(self, codigo):
		codigoUpper = codigo.upper()
		self.L0 = ord(codigoUpper[0]) - 65
		self.L1 = ord(codigoUpper[1]) - 65
		self.L2 = ord(codigoUpper[2]) - 65
		self.N3 = int(codigoUpper[3])
		self.L4 = ord(codigoUpper[4]) - 65
		self.N5 = int(codigoUpper[5])
		self.N6 = int(codigoUpper[6])

	#Sobrescrição da função __iter__: Permite que um objeto da classe cPlaca seja iterável, possibilitando o uso de funções como list()
	def __iter__(self):
		return iter([self.L0, self.L1, self.L2, self.N3, self.L4, self.N5, self.N6])

	#Sobrescrição da função __str__: Estipula que, ao ser convertida em string, a instância de cPlaca irá retornar uma string contendo o código de identificação da placa (com letras maiúsculas).
	def __str__(self):
		strOutput = ""
		strOutput += str(chr(self.L0 + 65)) + str(chr(self.L1 + 65)) + str(chr(self.L2 + 65)) + str(self.N3) + str(chr(self.L4 + 65)) + str(self.N5) + str(self.N6)
		return strOutput

	#Sobrescrição da função __getitem__: Permite que um atributo da classe seja acessado pelo índice através da notação indexadora (placa[x]).
	def __getitem__(self, indice):
		return(list(self)[indice])