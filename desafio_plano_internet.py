# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:

def recomendar_plano(consumo):
  
# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal

    plano1 = 10
    plano2 = 20

    if consumo <= plano1:
        plano = "Plano Essencial Fibra - 50Mbps"
    
    elif consumo > plano1 and consumo <= plano2:
        plano = "Plano Prata Fibra - 100Mbps"
    
    elif consumo > plano2:
        plano = "Plano Premium Fibra - 300Mbps"

    else:
        plano = "Verificar"
    
# TODO: Retorne o plano de internet adequado:
    
    return plano

# Solicita ao usuário que insira o consumo médio mensal de dados:

consumo = float(input())

# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:

print(recomendar_plano(consumo))