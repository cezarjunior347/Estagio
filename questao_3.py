

# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import pandas as pd


def calcular_faturamento(dados):
    # Filtrar dias com faturamento maior que 0
    dias_com_faturamento = dados[dados['valor'] > 0]

    # Calculando o menor e o maior valor de faturamento
    menor_faturamento = min(dias_com_faturamento['valor'])
    maior_faturamento = max(dias_com_faturamento['valor'])

    # Calculando a média mensal
    media_mensal = dias_com_faturamento['valor'].mean()

   
    # Contando os dias com faturamento acima da média
    #dias_acima_media = dias_com_faturamento[dias_com_faturamento['valor'] > media_mensal]['valor'].count()
    dias_acima_media = (dias_com_faturamento['valor'] > media_mensal).sum()

    return menor_faturamento, maior_faturamento, dias_acima_media

# Carregar dados do arquivo JSON
dados = pd.read_json('dados.json')

# Calcular os valores solicitados
menor_faturamento, maior_faturamento, dias_acima_media = calcular_faturamento(dados)

# Exibir resultados
print(f"Menor valor de faturamento: {menor_faturamento:.2f}")
print(f"Maior valor de faturamento: {maior_faturamento:.2f}")
print(f"Número de dias com faturamento superior à média: {dias_acima_media}")




