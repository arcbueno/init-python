import os

restaurantes = [];

def main():
    print('Sabor express')
    exibir_opcoes()
    escolher_opcao()   

def finalizar_app():
    clear()
    print('Finalizando app')
    
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    
def clear():
    os.system('clear')

def cadastrar_restaurante():
    '''Responsável por cadastrar um novo restaurante'''
    clear()
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar\n')
    categoria = input('Digite a categoria do restaurante que deseja cadastrar\n')
    
    restaurantes.append({'Nome': nome_restaurante, 'Ativo': False, 'Categoria': categoria })
    print(f'Restaurante {nome_restaurante} cadastrado com sucesso\n')
    main()

def listar_restaurantes():
    '''Responsável por listar um novo restaurante'''
    clear()
    print('Os restaurantes cadastrados são:\n')
    for i  in restaurantes: 
        print(f' - {i["Nome"].ljust(20)}| {i["Categoria"].ljust(20)} |{"Ativado" if(i["Ativo"]) else "desativado"}')
    print('\n')
    main()

def ativar_restaurante():
    '''Responsável por alterar o estado de um restaurante'''
    clear()
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar\n')
    restaurante_existe = False
    for restaurante in restaurantes:
        if(restaurante['Nome'] == nome_restaurante):
            restaurante_existe = True
            restaurante['Ativo'] = not restaurante['Ativo']
    
    print('Restaurante alterado com sucesso') if(restaurante_existe)  else print('Restaurante não encontrado')
    main() 
        

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção\n\n'))
        match opcao_escolhida:
            case 1: 
                cadastrar_restaurante()
            case 2: 
                listar_restaurantes()
            case 3: 
                ativar_restaurante()
            case _: 
                finalizar_app()
    except: 
        finalizar_app()

if __name__ == '__main__':
    main()