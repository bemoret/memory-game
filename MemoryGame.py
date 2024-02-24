import random
import sys

def montaTabuleiro(simbolo:str, qtdeValores:int=16) -> list:
    '''Retorna um tabuleiro preenchido com uma quantidade(qtdeValores) de
    símbolos'''
    '''int, str -> list[str]'''
    #Criando uma lista vazia para abrigar a quantidade de simbolos requisitada
    listaTabuleiro=[]
    
    #Criando uma repeticao de colocacoes dos simbolos na lista vazia
    for iTab in range(qtdeValores):

        #Colocando um simbolo no fim da lista a cada repeticao
        listaTabuleiro.append(str(simbolo))

    #Retornando o Tabuleiro preenchido com os simbolos desejados
    return listaTabuleiro

def obtemCoordenadas(coordenadas:str, separador:str=',') -> list:
    '''Identifica e adapta as coordenadas recebidas pelo usuario para melhor
    interpretação na leitura dos codigos'''
    '''str, str -> list[int]'''
    #Verificando se nao foi inserido algum caracter indesejado no inicio
    #da coordenada
    if coordenadas[0] in '()[]{}\/|*':

        #Retirando o caracter indesejado
        coordenadas = coordenadas.lstrip('()[]{}\/|*')

    #Verificando se nao foi inserido algum caracter indesejado no final
    #da coordenada
    if coordenadas[-1] in '()[]{}\/|*':

        #Retirando o caracter indesejado
        coordenadas = coordenadas.rstrip('()[]{}\/|*')
        
    #Criando uma lista vazia para abrigar as coordenadas
    listaCoordenadas=[]

    #Criando um laco de repeticao para investigar cada elemento da string
    #fornecida
    for x in range(len(coordenadas)):

        #Pulando casos onde o elemento analisado seja o separador
        if coordenadas[x] == separador:
            None

        #Analisando caso o termo da string seja um numero valido
        elif int(coordenadas[x]) in range(0,10):

            #Adicionando o valor subtraido a lista inicialmente vazia
            #Retira-se 1 de seu valor, para melhorcompreensao das
            #coordenadas por parte dos codigos
            listaCoordenadas.append(int(coordenadas[x])-1)

        #Caso nenhum dos casos seja atendidos, nao fazer nada
        else:
            None

    #Verificando se a lista possui tamanho par, ja que as coordenadas
    #precisam de um par de numeros para serem analisadas
    if (len(listaCoordenadas))%2 == 0:

        #Tamanho de lista correto, retornando-o
        return listaCoordenadas

    #Verificando caso o tamnho da lista seja impar
    else:
        
        #Deletando o ultimo termo da lista para que reste apenas pares
        #de numeros que serao usados como coordenadas
        del listaCoordenadas[-1]

        #Retornando a lista, agora consertada
        return listaCoordenadas

def validaFormato(coordenadas:str) -> bool:
    '''Verifica se as coordenadas passadas pelo usuário é valida ou nao'''
    '''str -> bool'''
    #Verificando se nao foi inserido algum caracter indesejado no inicio
    #da coordenada
    if coordenadas[0] in '()[]{}\/|*':

        #Retirando o caracter indesejado
        coordenadas = coordenadas.lstrip('()[]{}\/|*')

    #Verificando se nao foi inserido algum caracter indesejado no final
    #da coordenada
    if coordenadas[-1] in '()[]{}\/|*':

        #Retirando o caracter indesejado
        coordenadas = coordenadas.rstrip('()[]{}\/|*')

    #Verificando se ou o valor inserido no inicio ou no fim da coordenada
    #sao invalidos
    if int(coordenadas[0]) == 0 or int(coordenadas[2]) == 0:

        #Retornando Falso caso exista a presenca do 0 na coordenada avaliada
        return False

    #Verificando se os valores identificados sao plausiveis ou nao
    elif len(coordenadas) == 3 and int(coordenadas[0]) <= 4 and int(coordenadas[2]) <=4:
        #Retornando Verdadeiro caso os valores coincidam com o que se deseja
        return True

        #Retornando Falso caso a condicao acima nao seja atendida
    else:
        return False
    
def sorteiaNumeros(qtdeNumeros:int, a:int=1, b:int=8) -> list:
    '''Calcula e retorna uma lista com quantidade(qtdeNumeros) inteiros
    aleatorios, nao repetidos, que estejam entre a e b, considerando-os tambem'''
    '''int, int, int -> list[int]'''
    #Criando inicialmente uma lista vazia que abrigara a lista com os valores
    #originados por essa funcao
    listaNumeros=[]

    #Criando um loop e alcance com base nos parametros a e b
    for x in range(a,b):

        #Registrando cada um dos indices, exceto b, no fim da lista listaNumeros
        listaNumeros.append(x)

    #Adcionando b ao final da lista, terminando de adicionar todos os valores
    listaNumeros.append(b)

    #Retornando uma lista com a quantidade de numeros nao repetidos entre a e b
    #desejada
    #Nao estao necessariamente em ordem
    return random.sample(listaNumeros,qtdeNumeros)

def montaExibicao(tabuleiro:list[list[int]]) -> str:
    '''Cria uma string formada a partir dos elementos da lista fornecida que
    sera impressa ao usuario'''
    '''list[list[int]] -> str'''
    #Criando uma string vazia para abrigar os termos da lista indicada
    tabuleiroVisivel = ''

    #Criando um laço de repeticao para acessar todos os termos da lista
    for x in range(len(tabuleiro)):

        #Adicionando a string vazia cada termo da lista acompanhado de um
        #espaco em branco
        tabuleiroVisivel += str(tabuleiro[x]) + ' '

    #Removendo o ultimo termo da string que eh um espaco em branco indesejado
    tabuleiroVisivel = tabuleiroVisivel[0:len(tabuleiroVisivel)-1]

    #Retornando a string com os elementos da lista
    return tabuleiroVisivel

def formaMatriz(lista:list, n:int=4, m: int=4) -> list:
    '''Gera uma matriz n x m, com padrao 4x4 a partir dos elementos
    da lista fornecida'''
    '''list, int, int -> list'''
    #Criando uma lista vazia que abrigara as outras listas formando uma matriz
    matrizFormada = []

    #Criando um laco de repeticao para n que corresponde ao numero de linhas
    for i in range(n):

        #Criacao de uma linha, sendo lista vazia
        linhaFormada =[]

        #Criando um indice que correspondera a uma atualizacao da lista
        #fornecida levando em conta apenas os termos nao utilizados
        i=0

        #Criando um laco de repeticao para a criacao dos termos de cada
        #linha levando em consideracao a lista originalmente fornecida
        for j in range(m):
            linhaFormada.append(lista[j]) #Adicionando o termo a lista da linha

        #Atualizando o indice de corte da lista original
        i+=m

        #Realizando o corte de termos da lista ja usados na formacao da matriz
        lista=lista[i:]

        #Adicionando cada linha ja preenchida na matriz
        matrizFormada.append(linhaFormada)

    #Retornando a matriz(lista de listas) desejada
    return matrizFormada

def validaPosicaoAberta(tabuleiro:list[list[str,int]], linha:int, coluna:int,
                        simbolo:str='-') -> bool:
    '''Calcula e verifica se as coordenadas informadas correspondem a uma
    posicao que ja havia sido aberta'''
    '''list, int, int, str -> bool'''
    #Verificando se o elemento da matriz esta entre os numeros de uma casa
    #unitaria (0 ate 10)
    if tabuleiro[linha][coluna] in range(0,10):
        return True

    #Checando se o elemento selecionado corresponde a um simbolo, ou seja,
    #uma escolha valida
    elif tabuleiro[linha][coluna] == simbolo:
        return False

    #Retornando nada, caso ambas falhem
    else:
        return None

def validaPosicaoRaio(tabuleiro:list[list[str,int]], linha:int,
                      coluna:int) -> bool:
    '''Verifica se as coordenadas fornecidas se encontram dentro das limitacoes
    espaciais da matriz'''
    '''list, int, int -> bool'''
    #Verificando se o valor fornecidos na linha e na coluna sao compativeis com
    #o tamanho maximo das linhas e colunas da matriz
    if linha in range(len(tabuleiro)) and coluna in range(len(tabuleiro[linha])): 
        return True

    #Retornando Falso caso a condicao acima falhe
    else:
        return False

def validaPosicao(tabuleiro:list[list[str,int]], linha:int, coluna:int,
                  simbolo:str='*') -> bool:
    '''Verifica se as coordenadas informadas estao de acordo com as outras
    duas avaliacoes sobre validade da jogada'''
    '''list, int, int, str -> bool'''
    #Checando o caso das coordenadas estarem dentro das limitacoes da matriz e
    #do elemento em questao ser um simbolo, ou seja, um valor nao revelado
    #nessa jogada
    if validaPosicaoRaio(tabuleiro,linha,coluna) == True and validaPosicaoAberta(tabuleiro,linha,coluna,simbolo) == False:
        return True

    #Retornando Falso caso a condicao acima falhe
    else:
        return False
    
def verificaAcerto(gabarito:list[list[int]], posicao1:tuple[int], posicao2:tuple[int]) -> bool:
    '''Verifica se houve acerto, ou seja, formacao de um par nos valores
    a partir das coordenadas indicadas'''
    '''list, tuple, tuple -> bool'''
    #Comparando a possibilidade das duas posicoes indicadas serem compativeis
    #umas com as outras
    if gabarito[int(posicao1[0])][int(posicao1[1])] == gabarito[int(posicao2[0])][int(posicao2[1])]:
        return True

    #Retornando Falso caso a condicao falhe
    else:
        return False

def copiaMatriz(matriz:list[list]) -> list[list]:
    '''Copia e retorna uma matriz por completo'''
    '''list -> list'''

    #Criando uma matriz de referencia pra copia e realizando-a diretamente
    matrizCopia = matriz[:][:]

    #Retornando a copia
    return matrizCopia

def atualizaTabuleiro(tabuleiro:list[list[str,int]], gabarito:list[list[int]],
                      linha:int, coluna:int)-> list[list[int]]:
    '''Retorna uma copia do tabuleiro que esta sendo usado com uma atualizacao
    da coordenada indicada pelo respectivo valor da matriz gabarito'''
    '''list, list, int, int -> list'''
    #Copiando o tabuleiro que foi usado, utilizando a funcao copiaMatriz que
    #copia uma matriz
    novoTabuleiro = copiaMatriz(tabuleiro)

    #Atualizando a copia do tabuleiro para o valor indicado pelas coordenadas
    #tendo como referencia a matriz gabarito
    novoTabuleiro[linha][coluna] = gabarito[linha][coluna]
    
    #Retornando a copia do tabuleiro informado, com sua atualizacao na posicao
    #indicada com base no gabarito
    return novoTabuleiro

def main():
    #Criando valores para numero de acertos e jogadas, respectivamente
    numeroAcertos = 0
    numeroJogadas = 0

    #Recepcionando o Jogador com boas-vindas
    print(f'='*60,
          f'Boas-vindas ao Jogo da Memoria!',
          f'='*60,
          sep = '\n'
          )

    #Gerando o gabarito formado por um conjunto de pares de numeros de 1 ate 8
    gabarito = sorteiaNumeros(8)+sorteiaNumeros(8)

    #Randomizando a posicao de cada numero na lista
    random.shuffle(gabarito)

    #Transformando a lista gabarito em uma matriz
    gabarito = formaMatriz(gabarito)

    #Criando a lista do tabuleiro preenchido com as mascaras
    mascarasIniciais = montaTabuleiro('*')

    #Transformando o tabuleiro em uma matriz
    tabuleiro = formaMatriz(mascarasIniciais)

    #Criando o loop principal do jogo com base no numero de acertos
    while numeroAcertos < 8:

        #Imprimindo ao Jogador o tabuleiro antes de uma jogada
        print(f'='*40,
              f'Seu tabuleiro:',
              str(montaExibicao(tabuleiro[0][:])), #Exibindo primeira linha
              str(montaExibicao(tabuleiro[1][:])), #Exibindo segunda linha
              str(montaExibicao(tabuleiro[2][:])), #Exibindo terceira linha
              str(montaExibicao(tabuleiro[3][:])), #Exibindo quarta linha
              f'='*40,
              sep = '\n'
              )

        #Criando as coordenadas para a posicao1 como uma tupla inicialmente vazia
        posicao1 = ()

        #Criando repeticao enquanto a tupla da posicao1 nao estiver preenchida
        #corretamente
        while len(posicao1) < 2:

            #Recebendo as coordenadas da posicao1 pelo usuario
            coordenadas1 = str(input('Insira aqui os valores para a linha e coluna,RESPECTIVAMENTE,que deseja para sua primeira jogada, separe-os por virgula('',''):'))

            #Criando um caso para quando a validacao das coordenadas1 derem falsas
            while validaFormato(coordenadas1) == False:

                #Requisitando novamente ao usuario um valor, dessa vez indicando o erro no alcance da matriz
                coordenadas1 = str(input('Desculpe, entrada invalida, tente novamente. Valor(es) fora do alcance da matriz (Exemplo->3,1):'))

            #Apos validacao do seu formato, as coordenadas sao colocadas em uma lista
            coordenadas1Final = obtemCoordenadas(coordenadas1)

            #Os 2 primeiros valores sao recebidos e associados a tupla correspondente a coordenada
            posicao1 += (coordenadas1Final[0], coordenadas1Final[1])

        #Criando um loop para caso a posicao indicada nao seja valida
        while validaPosicao(tabuleiro, coordenadas1Final[0], coordenadas1Final[1], '*') == False:

            #Indicando erro ao Jogador e pedindo um novo valor de coordenada
            print('Coordenadas nao disponiveis. Favor inserir valores de linha e coluna compativeis', file=sys.stderr)

            #Repeticao do mesmo processo de obtencao da tupla da coordenada da posicao 1
            posicao1 = ()
            while len(posicao1) < 2:
                coordenadas1 = str(input('Insira aqui os valores para a linha e coluna,RESPECTIVAMENTE,que deseja para sua primeira jogada, separe-os por virgula('',''):'))
                while validaFormato(coordenadas1) == False:
                    coordenadas1 = str(input('Desculpe, entrada invalida, tente novamente. Valor(es) fora do alcance da matriz (Exemplo->3,1):'))
                coordenadas1Final = obtemCoordenadas(coordenadas1)
                posicao1 += (coordenadas1Final[0], coordenadas1Final[1])

        #Atualizando o tabuleiro para um candidato a tabuleiro com substituicao da posicao 1
        tabuleiroCandidato = atualizaTabuleiro(tabuleiro, gabarito, coordenadas1Final[0], coordenadas1Final[1])
        
        #Imprimindo ao Jogador o candidato a tabuleiro com a alteracao da posicao 1 ja realizada
        print(f'='*40,
              f'Seu tabuleiro:',
              str(montaExibicao(tabuleiroCandidato[0][:])), #Exibindo primeira linha
              str(montaExibicao(tabuleiroCandidato[1][:])), #Exibindo segunda linha
              str(montaExibicao(tabuleiroCandidato[2][:])), #Exibindo terceira linha
              str(montaExibicao(tabuleiroCandidato[3][:])), #Exibindo quarta linha
              f'='*40,
              sep = '\n'
              )

        #Criando uma tupla vazia para recepcao das coordenadas da posicao2
        posicao2 = ()

        #Criando um laco de repeticao enquanto a tupla nao for preenchida pelos 2 elementos de coordenada
        while len(posicao2) < 2:

            #Requisitando ao usuario valores para a coordenada da posicao 2
            coordenadas2 = str(input('Insira aqui os valores para a linha e coluna,RESPECTIVAMENTE,que deseja para sua segunda jogada, separe-os por virgula('',''):'))

            #Verificando se o formato fornecido indica falso
            while validaFormato(coordenadas2) == False:

                #Pedindo ao usuario que insira um valor valido
                coordenadas2 = str(input('Desculpe, entrada invalida, tente novamente. Valor(es) fora do alcance da matriz (Exemplo->3,1):'))

            #Obtendo uma lista com os valores da tupla pela funcao obtemCoordenadas
            coordenadas2Final = obtemCoordenadas(coordenadas2)

            #Adicionando cada um dos 2 valores a tupla responsavel pela posicao 2
            posicao2 += (coordenadas2Final[0], coordenadas2Final[1])

        #Criando loop para caso a posicao indicada com as coordenadas da posicao 2 sejam invalidas
        while validaPosicao(tabuleiro, coordenadas2Final[0], coordenadas2Final[1],'*') == False:

            #Requerindo ao Jogador, valores de linha e de coluna viaveis para o andamento do jogo
            print('Coordenadas nao disponiveis. Favor inserir valores de linha e coluna compativeis', file=sys.stderr)

            #Repeticao da criacao de uma tupla e adicao de termos a ela sobre a posicao 2
            posicao2 = ()
            while len(posicao2) < 2:
                coordenadas2 = str(input('Insira aqui os valores para a linha e coluna,RESPECTIVAMENTE,que deseja para sua segunda jogada, separe-os por virgula('',''):'))
                while validaFormato(coordenadas2) == False:
                    coordenadas2 = str(input('Desculpe, entrada invalida, tente novamente. Valor(es) fora do alcance da matriz (Exemplo->1,4):'))
                coordenadas2Final = obtemCoordenadas(coordenadas2)
                posicao2 += (coordenadas2Final[0], coordenadas2Final[1])

        #Atualizando o candidato a tabuleiro, dessa vez levanto em conta tambem as coordenadas da posicao 2
        tabuleiroCandidato = atualizaTabuleiro(tabuleiroCandidato, gabarito, coordenadas2Final[0], coordenadas2Final[1])
        print(f'='*40,
              f'Seu tabuleiro:',
              str(montaExibicao(tabuleiroCandidato[0][:])), #Exibindo primeira linha
              str(montaExibicao(tabuleiroCandidato[1][:])), #Exibindo segunda linha
              str(montaExibicao(tabuleiroCandidato[2][:])), #Exibindo terceira linha
              str(montaExibicao(tabuleiroCandidato[3][:])), #Exibindo quarta linha
              f'='*40,
              sep = '\n'
              )

        #Verificando se as 2 posicoes representam o mesmo valor, ou seja, se sao pares
        #No caso de nao ser
        if verificaAcerto(gabarito, (coordenadas1Final[0],coordenadas1Final[1]), (coordenadas2Final[0],coordenadas2Final[1])) == False:

            #Informando ao Jogador que suas posicoes nao formam um par
            print(f'Que pena! Voce errou! Tente novamente',file=sys.stderr)

            #Retornando as posicoes 1 e 2 com as mascaras '*'
            tabuleiroCandidato[coordenadas1Final[0]][coordenadas1Final[1]] = '*'
            tabuleiroCandidato[coordenadas2Final[0]][coordenadas2Final[1]] = '*'

            #Fazendo com que o tabuleiro seja interpretando com a adicao das mascaras
            #nas posicoes 1 e 2 indicadas como nao sendo pares
            tabuleiro = tabuleiroCandidato

        #No caso de serem pares
        elif verificaAcerto(gabarito, (coordenadas1Final[0],coordenadas1Final[1]), (coordenadas2Final[0],coordenadas2Final[1])) == True:

            #Informando ao Jogador que as posicoes propostas indicam pares
            print(f'Parabens! Voce encontrou um par!!')

            #Somando 1 ao contador de numero de acertos
            numeroAcertos += 1

            #Fazendo com que o candidato a tabuleiro seja admitido como verdadeiro
            tabuleiro = tabuleiroCandidato
            
        #Somando 1 ao contador de jogadas independentemente se houve erro ou acerto
        numeroJogadas += 1

    #Sinalizando ao Jogador seu numero total de jogadas ate terminar o jogo
    print(f'='*40,
          f'Seu numero de jogadas totais foram: ' + (str(numeroJogadas)),
          f'='*40,
          sep = '\n')

    #Anunciando o final do jogo e indicando possibilidade de rejogar
    print(f'Fim de jogo! Obrigado por jogar! Caso queira jogar novamente, por favor, reinicie o codigo')

main()
