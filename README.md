# Experimento - Problema do Caixeiro Viajante

Esse repositório é um experimento desenvolvido durante as aulas de Introdução a Teoria da Computação, com o objetivo de desenvolver resoluções para o problema tema.

Foram desenvolvidos três algoritmos:

- Aleatório
- Guloso
- Híbrido

Cada algortmo foi executo ao menos 30 vezes e com os valores obtidos, foi gerado uma média e devio padrão para se determinar a melhor solução.

Como data set foi utilizado as distâncias entre as capitais do Brasil. Dados disponíveis [neste link](http://www.i­ta­trans.­com.­br/dis­tan­ci­a.html).

Este projeto possui três Notebooks, cada um com um dos algoritmos e sua explicação, alem de um micro projeto em Python para permitir executar os algoritmos de forma local, através de uma CLI.

## Metas
- [x] Algoritmo Aleatório
- [x] Algoritmo Guloso
- [x] Algoritmo Híbrido
- [x] Cálculo da Média
- [x] Desvio Padrão
- [x] Comparação entre os algortmos
- [x] Plot dos resultados
- [ ] Mapa com a melhor rota descoberta*
- [ ] TXT com a melhor rota descoberta*

Esse repositório é um experimento desenvolvido durante as aulas de Introdução a Teoria da Computação

## Para executar o projeto

Estando na pasta do projeto execute os seguintes comandos.

```Bash
    pip3 install pipenv
    pipenv --three
    pipenv shell
    python3 -m src.main
```

Com isso você pode visualizar a pasta graficos onde estão os gráficos de desvio padrão de cada algoritmo.
