# Aprendendo a voar!!  
A ideia principal do projeto é modelar e implementar uma rede neural artificial simples capaz de jogar o famoso Flappy Bird!! Em outras palavras, encontrar uma função capaz de determinar se o pássaro deve bater as asas ou não.  

## Metodologia  
A fim de tornar o processo de modelagem do problema um pouco mais simples, o jogo utilizado para obtenção dos dados e testes não se trata de uma versão perfeita do jogo original, mas sim uma versão simplificada que mantém a velocidade do pássaro e dos obstáculos sempre constante.  

Os dados gerados para o treinamento foram obtidos a partir da observação de uma partida real realizada por uma pessoa e foram armazenados nos arquivos ``data/data.txt`` e ``data/data1.txt``.  

A arquitetura da rede implementada contou com duas camadas escondidas, e para o treinamento foi utilizada como função de perda o Erro Quadrático Médio e como otimizador o Gradiente Descendente Estocástico.  

Por fim, a hipótese assumida é que, dado uma partida de Flappy Bird sob as condições impostas pela nossa implementação, deve haver uma função $f(y)$, onde $y$ é a distância vertical da posição do pássaro e o espaço livre entre os canos, tal que $f(y)$ indique se o botão de "pulo" deve ser pressionado ou não.  

<img src="https://github.com/user-attachments/assets/b6ae763a-a61b-4109-8f80-2de5dcfcc3a3" width="400">  

## Resultados  
Após alguns testes e ajustes na implementação da rede, foi possível verificar a convergência do modelo para a função esperada. Na avaliação final, o modelo foi colocado para jogar sozinho em uma cópia da versão utilizada para gerar os dados, disponível em ``flappy_learned.py``.  

<img src="https://github.com/user-attachments/assets/427b671e-8fc6-41cd-9fbf-2c696eed2038" width="400">  

<img src="https://github.com/user-attachments/assets/26994b40-49bf-4b32-a895-d714916116d4" width="400">  

## Referências  
[Programação Dinâmica - Deeplearning notebooks](https://colab.research.google.com/github/pgdinamica/deeplearning/blob/main/notebooks/Introdu%C3%A7%C3%A3o_ao_Pytorch.ipynb#scrollTo=VxBiabB9_Ui7)  
