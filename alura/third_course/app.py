from models.restaurant import Restaurant
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato
import requests
import json



def main():
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)
    if(response.status_code != 200):
        print(response)
        return
    
    dados_restaurantes = {}
    for item in response.json():
        nome = item['Company']
        if(nome not in dados_restaurantes):
            dados_restaurantes[nome] = []
        
        dados_restaurantes[nome].append({
            "item": item['Item'],
            "Price": item['price'],
            "description": item['description']
        })
    
    for nome, itens in dados_restaurantes.items():
        nome_arquivo = f'{nome}.json'
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(itens, arquivo, indent=4)
            
    
    

if __name__ == '__main__':
    main()