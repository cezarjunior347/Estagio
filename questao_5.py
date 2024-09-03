
# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;



def inverter_string(s):
    # Utiliza slice para inverter a string
    return s[::-1]

# Entrada da string pelo usuário
entrada = input("Digite uma string para inverter: ")

# Inverte a string e exibe o resultado
#string_invertida = entrada[::-1] # fazendo direto sem precisar criar a funcao
string_invertida = inverter_string(entrada)

print(f"String invertida: {string_invertida}")


