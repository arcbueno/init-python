from models.restaurant import Restaurant
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato

def main():
    seuJose = Restaurant('Seu José', 'Livre')
    bebida1 = Bebida('Suco de maçã', 5.0, 'Grande')
    prato1 = Prato('lasanha', 10.0, 'Massa')
    prato2 = Prato('Pizza', 10.0, 'Pizza de queijo') 
    
    seuJose.adicionar_no_cardapio(bebida1);
    seuJose.adicionar_no_cardapio(prato1);
    seuJose.adicionar_no_cardapio(prato2);
    
    seuJose.exibir_cardapio()
    print()
    bebida1.aplicar_desconto()

    seuJose.exibir_cardapio()    
    

    
    

if __name__ == '__main__':
    main()