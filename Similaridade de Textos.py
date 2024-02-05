import re

# FUNÇÕES DISPONIBILIZADAS PELO IDEALIZADOR DO PROJETO
def le_assinatura():
    '''A função lê os valores dos traços linguísticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho médio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    '''A função lê todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    '''A função recebe um texto e devolve uma lista das sentenças dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A função recebe uma sentença e devolve uma lista das frases dentro da sentença'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A função recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa função recebe uma lista de palavras e devolve o número de palavras que aparecem uma única vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa função recebe uma lista de palavras e devolve o número de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


# MINHAS FUNÇÕES
def separa_palavras_de_um_texto(texto):
    # Recebe um texto e devolve uma lista com palavras do texto
    palavras = []

    # Verifica palavras dentro de um texto
    for sentença in separa_sentencas(texto):
        for frase in separa_frases(sentença):
            for palavra in separa_palavras(frase):
                palavras.append(palavra)

    return palavras


def tamanho_medio_palavra(texto):
    # Tamanho médio de palavra é a soma dos tamanhos das palavras dividida pelo número total de palavras.
    palavras = separa_palavras_de_um_texto(texto)

    soma_caracteres = 0

    for palavra in palavras:
        soma_caracteres += len(palavra)

    tamanho_medio_palavra = soma_caracteres / len(palavras)

    return tamanho_medio_palavra


def type_token(texto):
    # Relação Type-Token é o número de palavras diferentes dividido pelo número total de palavras.
    # Por exemplo, na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 4 diferentes
    # (o, gato, caçava, rato)

    texto_em_list = separa_palavras_de_um_texto(texto)

    relação_TypeToken = n_palavras_diferentes(texto_em_list) / len(texto_em_list)

    return relação_TypeToken


def hapax_legomana(texto):
    # Razão Hapax Legomana é o número de palavras que aparecem uma única vez dividido pelo total de palavras.
    # Por exemplo, na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente
    # que aparecem só uma vez (gato, caçava, rato)

    texto_em_list = separa_palavras_de_um_texto(texto)

    razao_hapax_legomana = n_palavras_unicas(texto_em_list) / len(texto_em_list)

    return razao_hapax_legomana


def complex_sentença(texto):
    # Complexidade de sentença é o número total de frases divido pelo número de sentenças.
    quantidade_frases = 0

    for sentenca in separa_sentencas(texto):
        frases_da_sentença = separa_frases(sentenca)
        quantidade_frases += len(frases_da_sentença)  # somar quantidade de frases

    complex_sentença = quantidade_frases / len(separa_sentencas(texto))

    return complex_sentença


def tamanho_medio_sentença(texto):
    # Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças dividida pelo número de
    # sentenças (os caracteres que separam uma sentença da outra não devem ser contabilizados como parte da sentença
    soma_caracteres_sentença = 0

    for sentenca in separa_sentencas(texto):
        soma_caracteres_sentença += len(sentenca)

    tamanho_médio_sentença = soma_caracteres_sentença / len(separa_sentencas(texto))

    return tamanho_médio_sentença


def tamanho_medio_frase(texto):
    # Tamanho médio de frase é a soma do número de caracteres em cada frase dividida pelo número de frases no texto
    # (os caracteres que separam uma frase da outra não devem ser contabilizados como parte da frase).
    # Numero de caracteres em cada frase
    soma_caracteres_frase = 0
    for setença in separa_sentencas(texto):
        for frase in separa_frases(setença):
            soma_caracteres_frase += len(frase)

    # Frases no texto
    frases_no_texto = 0
    for setença in separa_sentencas(texto):
        frases = len(separa_frases(setença))
        frases_no_texto += frases

    tamanho_médio_frase = soma_caracteres_frase / frases_no_texto
    return tamanho_médio_frase


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa função recebe um texto e deve devolver a assinatura do texto.'''
    assinatura = [tamanho_medio_palavra(texto), type_token(texto), hapax_legomana(texto), tamanho_medio_sentença(texto),
                  complex_sentença(texto), tamanho_medio_frase(texto)]
    return assinatura


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa função recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    i = 0
    soma_traço_linguisticos_AeB = 0

    for traço_linguistico in as_a:
        dif = abs(traço_linguistico - as_b[i])
        soma_traço_linguisticos_AeB += dif
        i += 1

    similaridade = soma_traço_linguisticos_AeB / 6

    return similaridade 


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa função recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n)
    do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    i = 0
    similaridades = []

    for texto in textos:
        assinatura_texto = calcula_assinatura(texto)
        similaridade_entre_textos = compara_assinatura(assinatura_texto, ass_cp)
        similaridades.append(similaridade_entre_textos)

    maior_similaridade = min(similaridades)  # Quanto menor o valor dessa variavel, maior a similaridade. Por isso usei min() invés de max()

    texto_com_maior_simili = similaridades.index(maior_similaridade) + 1

    return texto_com_maior_simili


ass_cp = le_assinatura()  # recebe a assinatura que iremos usar como comparação
textos = le_textos()  # realiza a leitura dos texos

avalia_textos(textos, ass_cp)  # avalia os textos e compara com a assinatura recebida
