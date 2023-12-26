print('Sabor express')

print('1. Cadastrar restaurante')
print('2. Listar restaurantes')
print('3. Ativar restaurante')
print('4. Sair\n')

opcao_escolhida = input('Escolha uma opção\n\n')

if(int(opcao_escolhida) != 4): 
    print(f'entrada: {opcao_escolhida}\n')
else: 
    print('saindo\n')


nome = 'Pedro'

for i in nome:
    print(i)
    