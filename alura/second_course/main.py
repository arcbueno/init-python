from models.restaurant import Restaurant


def main():
    papa_jonh = Restaurant('papa John', 'Italian')
    cicis_pizza = Restaurant('Cicis Pizzas', 'Italian')
    
    print(papa_jonh)
    print(cicis_pizza)
    print()
    papa_jonh.alterarEstado()
    print(papa_jonh)
    
    papa_jonh.receber_avaliacao('John', 10)
    
    

if __name__ == '__main__':
    main()