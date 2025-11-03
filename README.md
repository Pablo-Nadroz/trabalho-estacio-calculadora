# 🧮 Calculadora Simples em Python

Este é um projeto simples de uma calculadora em **Python** que realiza as quatro operações matemáticas básicas: adição, subtração, multiplicação e divisão. Foi desenvolvida com funções modulares para cada operação e uma função principal que gerencia o fluxo de cálculo e a escolha da operação pelo usuário.

## ✨ Funcionalidades

* **Adição** (`+` ou `adicao`)
* **Subtração** (`-` ou `subtracao`)
* **Multiplicação** (`*` ou `multiplicacao`)
* **Divisão** (`/` ou `divisao`)
* **Tratamento de Erro** para divisão por zero.
* **Loop de Execução** para realizar múltiplos cálculos.
* **Tratamento de Erro** para entradas não numéricas.

## ⚙️ Estrutura do Código

O código está organizado em três seções principais:

### 1. Funções de Operação

São as funções básicas que realizam o cálculo matemático.

| Função | Descrição |
| :--- | :--- |
| `adicao(num1, num2)` | Retorna a soma de `num1` e `num2`. |
| `subtracao(num1, num2)` | Retorna a diferença entre `num1` e `num2`. |
| `multiplicacao(num1, num2)` | Retorna o produto de `num1` e `num2`. |
| `divisao(num1, num2)` | Retorna o quociente de `num1` por `num2`, ou uma mensagem de erro se `num2` for **zero**. |

### 2. Função Principal da Calculadora

#### `calculadora(num1, num2, operacao)`

Esta função atua como o **roteador** do programa. Ela recebe os dois números e a operação desejada (que pode ser o símbolo ou o nome por extenso, como `+` ou `adicao`), e chama a função de operação correspondente.

* **Entradas:**
    * `num1` (float): O primeiro número.
    * `num2` (float): O segundo número.
    * `operacao` (string): O símbolo (`+`, `-`, `*`, `/`) ou nome da operação.
* **Saída:**
    * O resultado do cálculo (float ou string de erro, como no caso da divisão por zero ou operação inválida).

### 3. Laço Principal de Execução

Esta seção contém a lógica de interação com o usuário:

1.  Exibe uma mensagem de **Boas-vindas**.
2.  Inicia um *loop* `while` que continua executando até o usuário digitar `'N'` para sair.
3.  Dentro do *loop*:
    * Solicita o **primeiro número**.
    * Solicita o **segundo número**.
    * Solicita a **operação** desejada.
    * Utiliza um bloco `try-except ValueError` para garantir que as entradas para os números sejam válidas (tratamento de erro para entradas não numéricas).
    * Chama a função `calculadora` e imprime o resultado.
4.  Ao final de cada cálculo, pergunta ao usuário se ele deseja **continuar** ou **encerrar** o programa.

## Exemplo de Interação

<img width="556" height="513" alt="image" src="https://github.com/user-attachments/assets/3cbfa651-a1fc-47c4-8f9e-3f4638e52bf6" />
