# ================================================
# Calculadora de IMC
# Autor: Filipe Galter
# Calcula o IMC e retorna a classificação
# ================================================

def calcular_imc(peso, altura):
  
    imc = peso / (altura ** 2) #Fórmula para calcular o IMC

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obesidade"
      #classificações de IMC
      

    return imc, classificacao #para retornar IMC e a sua classificação
#Meus dados
peso = 70
altura = 1.70
imc, classificacao = calcular_imc(peso, altura)
print(f"IMC: {imc:.2f} - {classificacao}")
