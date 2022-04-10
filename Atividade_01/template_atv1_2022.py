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
import numpy as np

### Seu código inicia aqui ###

nome = 'gustavo_voltani_von_atzingen' # # coloque aqui o nome completo sem espaços (colocar '_' entre as palavras e.g. gustavo_voltani_von_atzingen) no formato de uma string
email = 'gustavo.von.atzingen@gmail.com' # Coloque o seu email aqui no formato string como no exemplo

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
    pg = []
    ### Seu código inicia aqui ###	
    
    ### Seu código termina aqui ###
    return pg

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
    
    ### Seu código termina aqui ###
    return resultado

def fit_linear(x, y):
    '''
    Crie uma função que recebe duas listas de números x e y e retorna uma lista com os coeficientes da 
    equação linear [A, B], considerando que y = A + B*x

    Importante: Use a equação da regressão linear como mostrada no vídeo da aula
    e não importe bibliotecas extras.
    
    Test
    -----------
    >>> fit_linear([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
    [0, 1]
    
    >>> fit_linear([1, 2, 3, 4, 5], [11, 21, 31, 41, 51])
    [1, 10]
    '''
    A, B = 0, 0
    ### Seu código inicia aqui ###	
    
    ### Seu código termina aqui ###
    return A, B

def numpy_seno(inicial, final, n_elementos):
    '''
    Crie uma função que calcule o seno de um vetor 1D no formato ndarray do numpy
    com a quantidade de elementosigual a n_elementos, iniciando no valor inicial e 
    terminando no final (variáveis da função).

    Importante: A biblioteca numpy já está importada no início do programa, 
    não importe novamente ela nem adicione outra bibliteca.

    Test
    ------------
    >>> numpy_seno(0, 1, 11)
    array([0.        , 0.09983342, 0.19866933, 0.29552021, 0.38941834,
       0.47942554, 0.56464247, 0.64421769, 0.71735609, 0.78332691, 0.84147098])

    >>> numpy_seno(2, 3, 4)
    array([0.90929743, 0.72308588, 0.45727263, 0.14112001])

    >>> numpy_seno(0, 0, 4)
    array([0., 0., 0., 0.])
    '''
    vetor = None
    ### Seu código inicia aqui ###	
    
    ### Seu código termina aqui ###
    return vetor

def cria_ndarray(linhas, colunas, min, max):
    '''
    Crie uma matriz (numpy ndarray) com duas dimensões contendo a quantidade
    de linhas igual a "linhas" e colunas "colunas (parâmetros da função).
    Este ndarray deverá conter valores randomicos que sejam no máximo igual 
    ao parâmetro max e no mínimo igual ao min.

    Test
    ------------
    >>> cria_ndarray(2, 3, 1, 2)
    array([[1.67447204, 1.12368922, 1.8081746 ],
           [1.24781365, 1.4590983 , 1.17893834]])

    >>> cria_ndarray(3, 2, 3, 5)
    array([[4.1455903 , 3.49365518],
           [3.27691244, 3.25673547],
           [3.69063084, 3.42526315]])
    '''
    matrix = None
    ### Seu código inicia aqui ###	
    
    ### Seu código termina aqui ###
    return matrix

if __name__ == '__main__':
    print(progressao_aritmetica(1, 2, 4))
    print(soma_pa(1, 2, 4))
    print(progressao_geometrica(1, 2, 4))
    print(soma_pg(1, 2, 3))
    print(fibonacci(4))
    print(soma_fibonacci(4))
    print(primo(7))
    print(fit_linear([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))
    print(numpy_seno(0, 1, 11))
    print(cria_ndarray(2, 3, 1, 2))