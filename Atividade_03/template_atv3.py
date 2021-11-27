import numpy as np
import sklearn
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

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


def avalia_modelo(resultados_reais, resultados_preditos):
    '''
    Crie uma função que avalia os resultados de um modelo e retorna as métricas acurácia, precisão, recall e F1:
    Ambas as variáveis de entrada (resultados_reais, resultados_preditos) são listas com n elementos e resultados
    de um teste fictício com as possibilidades 0 (Negativo) e 1 (Positivo).
    Ps. Os valores dos resultados abaixo estão com arredondamento na segunda casa decimal.
    
    
    Test
    -----------
    >>> avalia_modelo([0,0,0,0,1,1,1,1,1,1], [0,0,0,1,1,1,1,1,1,1])
    (0.9, 0.86, 1.0, 0.92)
    
    >>> avalia_modelo([0,0,0,0,1,1,1,1,1,1], [0, 0, 0, 0, 0, 1, 1, 1, 1, 1])
    (0.8, 1, 0.67, 0.80) 

    ''' 
    resultado = [None, None, None, None]
    ### Seu código inicia aqui ###	
    
    ### Seu código termina aqui ###
    return resultado


def K_vizinhos_proximos(X, y, k):
    '''
    Crie uma função que receba X e y (ambos ndarray's) com os dados de um dataset já preparado para utilização 
    com KNeighborsClassifier da biblioteca sklearn.
    
    * Separe os dados em treino e teste, com 20% dos dados randomizados na parte de teste (random_state=137).
    
    * Crie um classificador KNeighborsClassifier com 4 vizinhos
    
    * "treine" o classificador com o método KNeighborsClassifier.fit()
    
    * Efetue a predição nos dados de teste e retorne a acurária (inteiro)
    
    Test
    -----------
    >>> K_vizinhos_proximos([[0,0], [1,1], [2,2], [3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],[10,10]],
                            [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
                            3
                            )
    1.0   
    '''
    acc = None
    ### Seu código inicia aqui ###
    
    ### Seu código termina aqui ###
    return acc

def encontre_melhor_k(X, y):
    '''
    Crie uma função que utiliza a função escrita acima (K_vizinhos_proximos),
    e testa valores de k de 1 a 8 e encontra qual o melhor valor para um dataset
    X, y com formato igual ao da função K_vizinhos_proximos.
    Se todos houver mais de um resultado igual, retorne o menor de todos.
    
    Todos os datests de entrada terão pelo menos 10 dados.
    
    Test
    -----------
    >>> encontre_melhor([[0,0], [1,1], [2,2], [3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],[10,10]],
                            [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
    2
    '''
    best_k = None
    ### Seu código inicia aqui ###
    
    ### Seu código termina aqui ###
    return best_k


if __name__ == '__main__':
    print(avalia_modelo([0,0,0,0,1,1,1,1,1,1], [0,0,0,1,1,1,1,1,1,1]))
    print(K_vizinhos_proximos([[0,0], [1,1], [2,2], [3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],[10,10]],
                            [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
                            3
                            ))
    print(encontre_melhor_k([[0,0], [1,1], [2,2], [3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],[10,10]],
                            [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]))
