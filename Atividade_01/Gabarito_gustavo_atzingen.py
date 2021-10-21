'''
Informações sobre o como fazer a atividade:

* O script deverá ter o formato: seunome_sobrenome.py (sem espaços)
  Para pessoas com multiplos sobrenomes, colocar apenas o ultimo.
  Caracteres com acentos devem ser substituidos pelo equivalente sem acento.
  
* Não adicione nada no script fora dos locais onde está escrito :
    ### Seu código inicia aqui ###	
    print("Olá mundo!")
    ### Seu código termina aqui ###
    
'''

### Seu código inicia aqui ###

nome = 'gustavo_voltani_von_atzingen' # # coloque aqui o nome completo sem espaços (colocar '_' entre as palavras e.g. gustavo_voltani_von_atzingen) no formato de uma string
CPF = 3141592653  # Coloque seu CPF no formato int (sem pontos, traços ou espaços) ex: Se '123.456.789.7':  CPF = 1234567897
data_nascimento = '12/12/1999' # Coloque sua data de nascimento no formato 'dd/mm/aaaa' (string)

### Seu código termina aqui ###


def progressao_aritmetica(a1, r, n):
    '''
    Crie uma função que recebe um número inteiro a1, a razão de progressão aritmética r 
    e um número inteiro n > 1 e retorna uma lista com os n primeiros termos da progressão aritmética
    
    PA: https://pt.wikipedia.org/wiki/Progress%C3%A3o_aritm%C3%A9tica 
    
    Test
    -----------
    >>> progressao_aritmetica(1, 2, 4)
    [1, 3, 5, 7]
    ''' 
    lista_pa = []
    ### Seu código inicia aqui ###	
    lista_pa.append(a1)
    for i in range(n-1):
        lista_pa.append(lista_pa[-1] + r)
    ### Seu código termina aqui ###
    return lista_pa

def soma_pa(a1, r, n):
    '''
    Crie uma função que recebe um número inteiro a1, a razão de progressão aritmética r 
    e um número inteiro n > 1 e retorna a soma dos n primeiros termos da progressão aritmética
    
    PA: https://pt.wikipedia.org/wiki/Progress%C3%A3o_aritm%C3%A9tica 
    
    Return
    -----------
    soma: int
    
    Test
    -----------
    >>> soma_pa(1, 2, 4)
    16
    '''
    soma = 0
    ### Seu código inicia aqui ###	
    a = a1
    for i in range(n):
        soma += a
        a += r
    ### Seu código termina aqui ###
    return soma

def progressao_geometrica(a1, q, n):
    '''
    Crie uma função que recebe um número inteiro a1, a razão de progressão geométrica q 
    e um número inteiro n e retorna uma lista com os n primeiros termos da progressão geométrica
    
    https://pt.wikipedia.org/wiki/Progress%C3%A3o_geom%C3%A9trica 
    
    Test
    -----------
    >>> progressao_geometrica(1, 2, 4)
    [1, 2, 4, 8]
    >>> progressao_geometrica(1, 2, 3)
    [1, 2, 4]
    '''
    lista_pg = []
    ### Seu código inicia aqui ###	
    lista_pg.append(a1)
    for i in range(n-1):
        lista_pg.append(lista_pg[-1] * q)
    ### Seu código termina aqui ###
    return lista_pg

def soma_pg(a1, q, n):
    '''
    Crie uma função que recebe um número inteiro a1, a razão de progressão geométrica q > 1
    e um número inteiro n e retorna a soma dos n primeiros termos da progressão geométrica
    
    https://pt.wikipedia.org/wiki/Progress%C3%A3o_geom%C3%A9trica
    
    Test
    -----------
    >>> soma_pg(1, 2, 3)
    7
    >>> soma_pg(1, 2, 4)
    15
    '''
    soma = 0
    ### Seu código inicia aqui ###	
    lista_pg = progressao_geometrica(a1, q, n)
    for item in lista_pg:
        soma += item
    ### Seu código termina aqui ###
    return soma

def fibonacci(n):
    '''
    Crie uma função que recebe um número inteiro n e retorna uma lista com os n primeiros termos da sequência de Fibonacci
    
    https://pt.wikipedia.org/wiki/Sequ%C3%AAncia_de_Fibonacci  0, 1, 1, 2, 3, 5, 8, ...
    
    Test
    -----------
    >>> fibonacci(4)
    [0, 1, 1, 2]
    >>> fibonacci(2)
    [0, 1]
    '''
    fib = []
    ### Seu código inicia aqui ###	
    
    ### Seu código termina aqui ###
    return fib

def soma_fibonacci(n):
    '''
    Crie uma função que recebe um número inteiro n e retorna a soma dos n primeiros termos da sequência de Fibonacci
    
    https://pt.wikipedia.org/wiki/Sequ%C3%AAncia_de_Fibonacci 0, 1, 1, 2, 3, 5, 8, ...
    
    Test
    -----------
    >>> soma_fibonacci(4)
    4
    >>> soma_fibonacci(5)
    7
    >>> soma_fibonacci(1)
    0
    >>> soma_fibonacci(2)
    1
    '''
    soma = 0
    ### Seu código inicia aqui ###
    a, b = 0, 1
    if n == 0:
        soma = 0
    elif n > 0:
        for i in range(n):
            soma += a
            a, b = b, a + b
    ### Seu código termina aqui ###
    return soma

def primo(n):
    '''
    Crie uma função que recebe um número inteiro n e retorna True se ele é primo e False caso contrário
    Test
    -----------
    >>> primo(7)
    True
    >>> primo(8)
    False
    '''
    resultado = False
    ### Seu código inicia aqui ###	
    for i in range(2, int(n/2)):
        if n % i == 0:
            resultado = False
            break
    else:
        resultado = True
    ### Seu código termina aqui ###
    return resultado

def fit_linear(x, y):
    '''
    Crie uma função que recebe duas listas de números x e y e retorna uma lista com os coeficientes da 
    equação linear [A, B], considerando que y = A + B*x
    
    Test
    -----------
    >>> fit_linear([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
    [0, 1]
    
    >>> fit_linear([1, 2, 3, 4, 5], [11, 21, 31, 41, 51])
    [1, 10]
    '''
    A, B = 0, 0
    ### Seu código inicia aqui ###	
    x_sum, y_sum = sum(x), sum(y)
    n = len(x)
    x_media = x_sum/len(x)
    y_media = y_sum/len(y)
    x2_sum, xy_sum = 0, 0     # iniciando variável para somar x quadrados e xy
    for i in range(n):
        x2_sum += x[i]**2
        xy_sum += x[i]*y[i]
    B = (n*xy_sum - x_sum*y_sum)/(n*x2_sum - x_sum**2)
    A = (y_sum - B*x_sum)/n
    ### Seu código termina aqui ###
    return A, B

if __name__ == '__main__':
    print(progressao_aritmetica(1, 2, 4))