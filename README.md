# Aprendendo a voar!!
A ideia principal do projeto é modelar e implementar uma rede neural artificial simples capaz de jogar o famoso Flappy Bird!! Em outras palavras, encontrar uma função capaz de determinar se o passaro deve bater suas asas ou não.

## Metodologia
A fim de tornar o processo de modelagem do problema um pouco mais simples, o jogo utilizado para obtenção dos dados e testes não se trata de uma versão perfeita do jogo original, mas sim uma versão simplificada que mantém a velocidade do passaro e dos obstaculos sempre constantes.

Os dados gerados para o treinamento foram obtidos a partir da observação de uma partida real realizada por uma pessoa, e foram guardados nos arquivos ``data/data.txt`` e ``data/data1.txt``.

A arquitetura da rede implementada contou com duas camadas escondidas, e para o treinamento foi utilizado como função de perda o Erro Quadradico Médio e como otimizador o Gradiente Descendente Estocastico.

Por fim, a hipotese assumida é que dado uma partida de Flappy Bird, sob as condições impostas pela nossa implementação, deve haver uma função $f(y)$, onde $y$ é a distancia vertical da posição do passaro e o espaço livre entre os canos, tal que $f(y)$ indique se o botão de "pulo" deva ser pressionado ou não.
//Colocar gif do jogo aqui

## Resultados
Apos alguns testes e ajustes na implementação da rede foi possivel verificar a convergêncida do modelo para a função esperada. E em avaliação final, o modelo foi colocado para jogar sozinho em uma cópia da versão utilizada para gerar os dados, disponível em ``flappy_learned.py``.
//gif ia jogando
//png função modelada

## Referências
[Programação Dinamica - Deeplearning notebooks](https://colab.research.google.com/github/pgdinamica/deeplearning/blob/main/notebooks/Introdu%C3%A7%C3%A3o_ao_Pytorch.ipynb#scrollTo=VxBiabB9_Ui7)
