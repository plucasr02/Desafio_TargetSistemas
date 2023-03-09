#Escreva um programa na linguagem que desejar onde calcule 
# o percentual de representação que cada estado teve dentro 
# do valor total mensal da distribuidora.

# Distribuidoras
sp = 67.83643
rj = 36.67866
mg = 29.22988
es = 27.16548
outros =19.84953

#valor total mensal
total = [sp, rj, mg, es, outros]
total_mensal = sum(total)
print(total)
print(total_mensal)

#porcentagem

por_sp = (sp/total_mensal) * 100
por_rj = (rj/total_mensal) * 100
por_mg = (mg/total_mensal) * 100
por_es = (es/total_mensal) * 100
por_outros = (outros/total_mensal) * 100

#print dos valores

print(f"O percentual de representação de SP foi: {round(por_sp, 2)}%")
print("---------------------------------------------------------------")
print(f"O percentual de representação de RJ foi: {round(por_rj, 2)}%")
print("---------------------------------------------------------------")
print(f"O percentual de representação de MG foi: {round(por_mg, 2)}%")
print("---------------------------------------------------------------")
print(f"O percentual de representação de ES foi: {round(por_es, 2)}%")
print("---------------------------------------------------------------")
print(f"O percentual de representação de Outros foi: {round(por_outros, 2)}%")
print("---------------------------------------------------------------")
print(f"O percentual total é de: {por_sp + por_rj + por_mg + por_es + por_outros}%")

