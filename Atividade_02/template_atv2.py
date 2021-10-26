import math
import pandas as pd
from sklearn.model_selection import train_test_split


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

nome = '' # # coloque aqui o nome completo sem espaços (colocar '_' entre as palavras e.g. gustavo_voltani_von_atzingen) no formato de uma string
        # Mantenha o mesmo nome que você colocou na atividade 1 para facilitar a agregação de dados no final

### Seu código termina aqui ###


def entropia(na, nb):
    '''
    Crie uma função que recebe a quantidade (em inteiros) de dois elementos - na e nb - e retorne
    o valor da entropia do conjunto.
    
    Utilize math.log2(p) para calcular o valor do log base do de uma probabilidade.
    
    Test
    -----------
    >>> entropia(50, 50)
    1
    
    >>> entropia(10, 50)
    0.6500224216483541
    
    >>> entropia(10, 100)
    0.4394969869215134
    
    >>> entropia(0, 100)
    0.011397802630112312
    
    >>> entropia(10, 0)
    0.011397802630112312
    ''' 
    entropia = 1
    ### Seu código inicia aqui ###	
    
    ### Seu código termina aqui ###
    return entropia


def organize_data(file_name):
    '''
    Crie uma função que utiliza le um arquivo csv utilizando a biblioteca pandas
    e então organiza os dados apenas com as colunas:
    A, B, C, D, targuet (Removendo as colunas E e F) e retorne um dataframe (df)
    
    * Utilize o arquivo dados.csv como teste de entrada para a função
    
    * Utilize pandas como pd
    
    Test
    -----------
    >>> type(organize_data('data.csv'))
    pandas.core.frame.DataFrame
    
    >>> organize_data('data.csv').shape
    (200, 5)
    
    >>> organize_data('data.csv').columns
    Index(['A', 'B', 'C', 'D', 'y'], dtype='object')
    
    >>> organize_data('data.csv').loc[1].values
    array([9.74986214, 5.14024213, 5.86335541, 5.24703444, 1.0])
    
    >>> organize_data('data.csv').loc[100].values
    array([9.00177971, 4.42446467, 7.19523579, 5.72467708, 1.0])
    '''
    df = None
    ### Seu código inicia aqui ###
    
    ### Seu código termina aqui ###
    return df

def shuffle_split_data(df):
    '''
    Crie uma função que receba o dataframe com as colunas A, B, C, D, targuet,
    (gerado na função organize_data() ) e organize os dados em numpy arrays
    X_train, X_test, y_train, y_test, com X contendo as colunas A, B, C e D e 
    y a coluna targuet.
    Embaralhe os dados X e y com a train_test_split da biblioteca skelarn com o 
    random_state 33 e com 25% dos dados para treino e 75% para teste.
    
    Test
    -----------
    >>> len(shuffle_split_data(df))
    4
    
    >>> shuffle_split_data(df)[0].shape
    (150, 4)
    
    >>> shuffle_split_data(df)[1].shape
    (50, 5)
    
    >>> shuffle_split_data(df)[2].shape
    (150,)
    
    >>> shuffle_split_data(df)[3].shape
    (50,)
    '''
    X_train, X_test, y_train, y_test = None, None, None, None
    ### Seu código inicia aqui ###
    
    ### Seu código termina aqui ###
    return X_train, X_test, y_train, y_test


if __name__ == '__main__':
    print(entropia(50, 50))
    print(entropia(10, 100))
    df = organize_data()
    print(type(organize_data('data.csv')))
    print(organize_data('data.csv').shape)
    print(organize_data('data.csv').loc[1].values)
    print(shuffle_split_data(df)[0].shape)
    print(shuffle_split_data(df)[1].shape)
    print(shuffle_split_data(df)[2].shape)
    print(shuffle_split_data(df)[3].shape)