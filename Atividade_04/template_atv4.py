import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Dense
from sklearn.utils import shuffle


'''
Informações sobre o como fazer a atividade:

* Use as bibliotecas já importadas no início do script. Não adicione ou altere os imports.

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



# verifica se é primo
def is_prime()


def carrega_dados():
    '''
    Crie uma função que carrega os dados do dataset mnist utilizando o módulo de datasets já disponível 
    em tensorflow.keras.datasets (já importado no início do script).
    
    A função deverá retornar os dados no formato de uma tupla com 4 elementos, sendo os dados 
    X de treino, os dados y de treino, os dados X de teste e os dados y de teste respectivamente, 
    (X_train, y_train, X_test, y_test)

    Test
    -----------
    >>> len(carrega_dados())
    4
    
    >>> carrega_dados()[0].shape
    (60000, 28, 28)

    >>> carrega_dados()[1].shape
    (60000,)

    >>> carrega_dados()[2].shape
    (10000, 28, 28)

    >>> carrega_dados()[3].shape
    (10000,)
    ''' 
    retorno = (None, None, None, None)
    ### Seu código inicia aqui ###	
    
    ### Seu código termina aqui ###
    return retorno


def emparalha_e_normaliza(X_train, y_train, X_test, y_test):
    '''
    Crie uma função que carrega receba os dados do mnist já gerados na função carrega_dados() e,
    utilizando o método shuffle do sklearn.utils (já importado no início do script), embaralhe os
    dados de treino e teste (separadamente) e depois mude o range dos dados para 0 a 1.

    No final, o retorno deverá ser no mesmo formato da função carrega_dados() (tupla com 4 elementos)

    Test
    -----------
    >>> len(emparalha_e_normaliza(*carrega_dados()))
    4
    
    >>> emparalha_e_normaliza(*carrega_dados())[0].shape
    (60000, 28, 28)

    >>> emparalha_e_normaliza(*carrega_dados())[0].max()
    1

    >>> emparalha_e_normaliza(*carrega_dados())[0].min()
    0

    >>> emparalha_e_normaliza(*carrega_dados())[1].shape
    (60000,)

    >>> emparalha_e_normaliza(*carrega_dados())[2].shape
    (10000, 28, 28)

    >>> emparalha_e_normaliza(*carrega_dados())[2].max()
    1

    >>> emparalha_e_normaliza(*carrega_dados())[2].min()
    1

    >>> emparalha_e_normaliza(*carrega_dados())[3].shape
    (10000,)
    ''' 
    retorno = (None, None, None, None)
    ### Seu código inicia aqui ###	
    
    ### Seu código termina aqui ###
    return retorno

def monta_modelo_1():
    '''
    Crie uma função que monta um modelo de rede neural sequencial capaz de receber os dados 
    já tratados nas funções anteriores e ser capaz de uma acurácia de pelo menos 85% nos dados
    de teste. 

    * O modelo a ser retornado deve ser compilado mas não treinado (com model.fit )
    
    Test
    -----------
    >>> type(monta_modelo_1())
    tensorflow.python.keras.engine.sequential.Sequential

    >>> monta_modelo_1().get_config()
    {'name': 'sequential_2',
        'layers': [{'class_name': 'InputLayer',
        'config': {'batch_input_shape': (None, 128),
        'dtype': 'float32',
        ...
    (Não vai ser exatamente isso, apenas para ter uma ideia)

    >>> monta_modelo_1().get_layer(index=-1).activation
     <function tensorflow.python.keras.activations.softmax(x)>


    '''
    model = None
    ### Seu código inicia aqui ###
    
    ### Seu código termina aqui ###
    return model

def monta_modelo_2():
    '''
    Similar ao monta_modelo_1, porém agora monte uma rede com pelo menos uma camada convolucional
    e tenha uma acurácia de pelo menos 92% nos dados de treino

    * O modelo a ser retornado deve ser compilado mas não treinado (com model.fit)
    
    Test
    -----------
    >>> type(monta_modelo_2())
    tensorflow.python.keras.engine.sequential.Sequential

    >>> monta_modelo_2().get_config()
    {'name': 'sequential_2',
        'layers': [{'class_name': 'InputLayer',
        'config': {'batch_input_shape': (None, 128),
        'dtype': 'float32',
        ...
    (Não vai ser exatamente isso, apenas para ter uma ideia)

    >>> monta_modelo_2().get_layer(index=-1).activation
     <function tensorflow.python.keras.activations.softmax(x)>


    '''
    model = None
    ### Seu código inicia aqui ###
    
    ### Seu código termina aqui ###
    return model
