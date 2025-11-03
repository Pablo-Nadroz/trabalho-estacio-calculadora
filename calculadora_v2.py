saida = ''
# Função adição
def adicao(num1, num2):
    return num1 + num2

# Cfunção subtração
def subtracao(num1, num2):
    return num1 - num2

# função multiplicação
def multiplicacao(num1, num2):
    return num1 * num2

# função divisão
def divisao(num1, num2):
    # Verifica se o divisor (num2) é igual a 0
    if num2 == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return num1 / num2

# --- Função Principal da Calculadora ---

def calculadora(num1, num2, operacao):
    # Converte a operação para minúsculas para facilitar a verificação
    op_lower = operacao.lower()

    # Variável para armazenar o resultado do cálculo
    resultado = None

    if op_lower == '+' or op_lower == 'adicao':
        resultado = adicao(num1, num2)

    elif op_lower == '-' or op_lower == 'subtracao':
        resultado = subtracao(num1, num2)

    elif op_lower == '*' or op_lower == 'multiplicacao':
        resultado = multiplicacao(num1, num2)

    elif op_lower == '/' or op_lower == 'divisao':
        # Para a divisão, o retorno já pode ser a mensagem de erro ou o resultado
        resultado = divisao(num1, num2)

    else:
        resultado = f"Operação '{operacao}' não reconhecida. Tente: +, -, *, /"

    return resultado


# --- Laço Principal de Execução ---

print("Bem-vindo(a) à Calculadora Nadroz")
print("====================================")

while saida.lower() != 'n':
    print("\n--- Novo Cálculo ---")
    try:
        # Pede ao usuario que digite o 1 numero
        primeiro_numero = float(input("Digite o PRIMEIRO número: "))

        # pede para o usuarieo digitar o 2 numero
        segundo_numero = float(input("Digite o SEGUNDO número: "))

        # pede ao usuario para escolher a operação de calculo
        operacao_matematica = input("Digite a OPERAÇÃO (+, -, *, / ou o nome dela): ")

        # chama função do calculo
        resultado = calculadora(primeiro_numero, segundo_numero, operacao_matematica)

        # Imprime o resultado do calculo
        print(f"\nResultado da operação: {resultado}")

        # exibe msg de erro em caso de digitos errados
    except ValueError:
        print("\n ERRO: Certifique-se de digitar números válidos.")

    print("------------------------------------")
    saida = input("Deseja continuar? Digite [S] para Sim ou [N] para Não: ")
    print("------------------------------------")

print("\n👋 Programa encerrado. Obrigado por usar a Calculadora")
