# faturamento
faturamento_mensal = [22174.1664, 24537.6698, 26139.6134, 0, 0, 26742.6612, 0, 42889.2258, 46251.174, 11191.4722, 0, 0, 
                      3847.4823, 373.7838, 2659.7563, 48924.2448, 18419.2614, 0, 0, 35240.1826, 43829.1667, 18235.6852, 
                      4355.0662, 13327.1025, 0, 0, 25681.8318, 1718.1221, 13220.495, 8414.61]

# menor valor faturamento
min = min(faturamento_mensal)
print(f"Menor fator de faturamento ocorrido em um dia do mês: {min}")

# maior valor faturamento
max = max(faturamento_mensal)
print("-----------------------------------------------------------------------")
print(f"Maior fator de faturamento ocorrido em um dia do mês: {max}")

# Número de dias do mês
dias_mes = len(faturamento_mensal)
dias_sem_zero = [zero for zero in faturamento_mensal if zero != 0]

#media
media = sum(faturamento_mensal) / len(dias_sem_zero)
print("-----------------------------------------------------------------------")
print("A média mensal foi de:", round(media,2))

# faturamento diário > media mensal (numero de dias)
faturamento_diario = [dia for dia in faturamento_mensal if dia > media]
print("-----------------------------------------------------------------------")
print("O número de dias em que o valor de faturamento diário foi superior à média mensal:", len(faturamento_diario))
