dic1 = { '0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6': 6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15, 'G':16, 'H':17, 
            'I':18, 'J':19, 'K':20, 'L':21, 'M':22, 'N':23, 'O':24, 'P':25, 'Q':26, 'R':27, 'S':28, 'T':29, 'U':30, 'V':31, 'W':32, 'X':33, 'Y':34, 'Z':35}
#dicionário para atribuir valores para cada item da variavel "valor" 

dic2 = {10:'A',11:'B', 12:'C', 13:'D', 14:'E', 15:'F', 16:'G', 17:'H', 18:'I', 19:'J', 20:'K', 21:'L', 22:'M', 23:'N', 24:'O', 25:'P', 26:'Q',
        27:'R', 28:'S', 29:'T', 30:'U', 31:'V', 32:'W', 33:'X', 34:'Y', 35:'Z'} 
#dicionario para converter valores maiores que 9 para letras

def decimal(valor, bOrigem): #função para transformar números de qualquer base para base decimal
    valorIn = valor[::-1]    #inverter a ordem do número
    novoValor = 0            #contador para resultado do novo valor
    for i in range(len(valorIn)):
        novoValor +=  (dic1[valorIn[i]]) * (bOrigem**i) #calculo de conversão de qualquer base para base decimal

    return novoValor

def qualquerBase(valor, bDestino): #função para transformar números da base decimal para qualquer base
    valor = int(valor)             #transforma a string valor em inteiro
    novoValor = []                 #lista para adicionar o resto das divisões sucessivas
    while valor > 0:               #loop para controlar quando parar a divisão
        resto = valor % bDestino   #variável para guardar o resto da divisão
        valor = valor // bDestino  #atualizar o valor da váriavel com a parte inteira da divisão
        if resto > 9:              #condição para mudar números para letras com o auxilio do dic2
            novoValor.append(dic2[resto])
        else:
            novoValor.append(resto)
    novoValor = reversed(novoValor) #inverter a ordem da lista criada com os restos das divisões
    resultado = "".join(str(elemento) for elemento in novoValor) #transforma a lista em uma string sem vírgulas
    return resultado

valor = str(input("Quantidade a ser convertida:")) #váriaveis para armazenar valores que o usuário irá fornecer
bOrigem = int(input("Base de Origem:"))
bDestino = int(input("Base de Destino:"))

if bDestino == 10: #condição para determinar qual função usar
    print("Resultado:", decimal(valor,bOrigem))
else:
    valorDec = decimal(valor, bOrigem) #transforma o valor para decimal
    print("Resultado:", qualquerBase(valorDec, bDestino)) 
    if bOrigem != 10:
        print("Equivalente em Decimal:", valorDec)
