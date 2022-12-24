from string import digits

operadores = '*/+-'

def refinar_expressao(expressao_bruta : str) -> str:
    """
    Transformar a entrada do usuário para facilitar a leitura do Bot

    Args:
        expressao_bruta (str): Entrada do usuário

    Returns:
        str: Expressão formatada, caso errado, retornar 'erro'
    """

    expressao = expressao_bruta

    for caractere in expressao:
        if caractere not in str(digits + operadores):
            expressao = expressao.replace(caractere, '')

    for operador in operadores:
        if operador in expressao:
            expressao = expressao.replace(operador, f' {operador} ')

    if len(expressao) != 0 and '  ' not in expressao:
        return expressao
    else:
        return 'erro'



def verificar_expressao(expressao_bruta : str) -> bool:
    """
    Verificar se a expressão é possível de ser calculada pelo Bot

    Args:
        expressao_bruta (str): Entrada do usuário

    Returns:
        bool: Verdadeiro ou Falso
    """

    expressao = refinar_expressao(expressao_bruta)

    primeiro_elemento = expressao[0] in digits
    ultimo_elemento = expressao[-1] in digits

    if primeiro_elemento and ultimo_elemento:
        return True
    else:
        return False


def calcular(expressao_bruta : str) -> str:
    """
    Função que sintetiza a ação de calcular do Bot

    Args:
        expressao_bruta (str): Entrada do usuário

    Returns:
        str: Resposta do calculo
    """

    expressao = refinar_expressao(expressao_bruta).split()

    for operador in operadores:
        while operador in expressao:
            expressao = operacao(expressao, operador)

    return expressao[0]


def operacao(expressao : list, operador : str) -> list:
    """
    Função que criar um modelo genérico de operação

    Args:
        expressao (list): Expressão em andamento
        operador (str): Operação a ser realizada

    Returns:
        list: Expressão reduzida
    """

    index = expressao.index(operador)

    match operador:
        case '*':
            resultado = float(expressao[index - 1]) * float(expressao[index + 1])
        case '/':
            resultado = float(expressao[index - 1]) / float(expressao[index + 1])
        case '+':
            resultado = float(expressao[index - 1]) + float(expressao[index + 1])
        case '-':
            resultado = float(expressao[index - 1]) - float(expressao[index + 1])
        case _:
            resultado = float(expressao[index - 1] + expressao[index + 1])

    del expressao[index - 1 : index + 2]

    expressao.insert(index - 1, resultado)

    return expressao