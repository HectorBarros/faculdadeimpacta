# Faculdade Impacta - Jogo de Adivinhação em Python

Projeto prático desenvolvido para as atividades acadêmicas da **Faculdade Impacta Tecnologia**, implementando um jogo interativo de adivinhação de números no terminal com Python.

---

## 📌 Sobre o Projeto

O **Jogo de Adivinhação** é uma aplicação em terminal que desafia o usuário a descobrir um número secreto gerado aleatoriamente pelo computador entre 1 e 100. 

A cada tentativa, o programa fornece dicas indicando se o número sorteado é maior ou menor que o palpite fornecido. Ao acertar, o jogo finaliza e apresenta um relatório estatístico completo sobre o desempenho do jogador na partida.

---

## 🚀 Conceitos e Tecnologias Aplicadas

O código aborda conceitos fundamentais da lógica de programação em Python:

- **Biblioteca `random`**: Geração de números pseudoaleatórios via função `randint()`.
- **Estruturas de Repetição (`while True`)**: Controle de fluxo com laço contínuo até que a condição de parada (`break`) seja satisfeita.
- **Entrada e Conversão de Dados (`input` / `int`)**: Captura da resposta do usuário pelo teclado e conversão de string para número inteiro.
- **Estruturas Condicionais (`if / elif / else`)**: Comparação lógica entre o palpite e o número sorteado.
- **Listas (`list`)**: Armazenamento dinâmico do histórico de palpites com `.append()`.
- **Funções Nativas de Agregação**:
  - `len()`: Contagem do total de palpites.
  - `max()`: Identificação do maior número palpitado.
  - `min()`: Identificação do menor número palpitado.
  - `sum()`: Cálculo do somatório dos palpites para extração da média aritmética.
- **Formatação de Saída (`f-strings`)**: Apresentação formatada das estatísticas com precisão decimal (`{media_palpites:.2f}`).

---

## 🧩 Explicação do Código Passo a Passo

O código está estruturado em 4 etapas bem definidas:

### 1. Preparação
```python
import random

numero_sorteado = random.randint(1, 100)
palpites = []
```
- Importa o módulo `random`.
- Sorteia um número inteiro aleatório entre 1 e 100 (inclusivo) e armazena em `numero_sorteado`.
- Inicializa uma lista vazia `palpites` para registrar as jogadas.

### 2. Repetição e Entrada
```python
while True:
    palpite = int(input("Digite seu palpite (entre 1 e 100): "))
    palpites.append(palpite)
```
- Inicia um laço de repetição infinito (`while True`).
- Solicita ao usuário um palpite via `input()`, convertendo o texto para número inteiro com `int()`.
- Adiciona o número digitado à lista `palpites` através do método `.append()`.

### 3. Verificação do Palpite
```python
    if palpite < numero_sorteado:
        print("O número sorteado é maior")
    elif palpite > numero_sorteado:
        print("O número sorteado é menor")
    else:
        print("Parabéns! Você acertou!")
        break
```
- Se o palpite for menor que o número sorteado, exibe `"O número sorteado é maior"`.
- Se o palpite for maior, exibe `"O número sorteado é menor"`.
- Se for igual, exibe a mensagem de parabéns e executa o `break`, encerrando o laço `while`.

### 4. Estatísticas da Partida
```python
total_tentativas = len(palpites)
maior_palpite = max(palpites)
menor_palpite = min(palpites)
media_palpites = sum(palpites) / total_tentativas

print("\n=== Estatísticas da Partida ===")
print(f"1. Quantidade de tentativas: {total_tentativas}")
print(f"2. Palpites informados: {palpites}")
print(f"3. Maior palpite: {maior_palpite}")
print(f"4. Menor palpite: {menor_palpite}")
print(f"5. Média dos palpites: {media_palpites:.2f}")
```
- Calcula e exibe as métricas finais da rodada utilizando os valores coletados na lista.

---

## 💻 Como Executar

### Pré-requisitos
- Ter o **Python 3.x** instalado no computador.

### Executando o Jogo

1. Clone o repositório ou baixe o arquivo:
```bash
git clone https://github.com/HectorBarros/faculdadeimpacta.git
```

2. Acesse a pasta do projeto:
```bash
cd faculdadeimpacta
```

3. Execute o script Python:
```bash
python jogo_adivinhacao.py
```

---

## 🖥️ Exemplo de Execução

```text
Digite seu palpite (entre 1 e 100): 50
O número sorteado é maior
Digite seu palpite (entre 1 e 100): 75
O número sorteado é menor
Digite seu palpite (entre 1 e 100): 62
O número sorteado é maior
Digite seu palpite (entre 1 e 100): 68
Parabéns! Você acertou!

=== Estatísticas da Partida ===
1. Quantidade de tentativas: 4
2. Palpites informados: [50, 75, 62, 68]
3. Maior palpite: 75
4. Menor palpite: 50
5. Média dos palpites: 63.75
```

---

## 👤 Autor

- **Hector Barros**
- Repositório: [HectorBarros/faculdadeimpacta](https://github.com/HectorBarros/faculdadeimpacta)
