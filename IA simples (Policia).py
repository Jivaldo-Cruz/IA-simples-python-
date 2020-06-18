__autor__ = "Jivaldo Da Cruz"


lista_per = ["Telefonaste à vítima?", "Estiveste no local do crime?", "Moras perto da vítima?", "Devias algum dinheiro à vítima?", "Já trabalhaste com a vítima?"]

#contador da verdade e mentiras
cont_m = 0
cont_v = 0

print("As resposta tem de ser Sim/Não")
for per in range(len(lista_per)):
    print(lista_per[per])
    s_n = input(">>> ").lower()

    if(s_n == "sim"):
        cont_m += 1
    elif(s_n == "não" or s_n == "nao"):
        cont_v += 1
    else:
        cont_m += 1
        print("Se não digitaste o recomendado que é 'Sim/Não' vais contar como culpado!")

if(cont_v == 2):
    print("O individuo é considerado suspeito")
elif(cont_v > 2):
    print("O individuo é considerado inocente")
else:
    if(cont_m == 5):
        print("O individuo é considerado assassino")
    elif(cont_m == 3 or cont_m == 4):
        print("O individuo é considerado cúmplice")
