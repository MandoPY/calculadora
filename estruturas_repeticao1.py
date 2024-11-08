# variável com string vazia
entrada_idade = ''

# verificação
# loop while enquanto entrada_idade não for '0'
while not str(entrada_idade) == '0':
    # entrada do usuário
    entrada_idade = input('Digite um número qualquer ou 0 para sair: ')
    
    # imprime o numero digitado pelo usuário
    print('Número digitado:', entrada_idade)