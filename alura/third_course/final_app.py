from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello():
    return {'Hello': 'world'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Exibe uma lista de restaurantes
    
    Parametros:
    - `restaurante`: str - the name of the restaurant
    '''
   
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)
    if(response.status_code != 200):
        return {'Error': f'{response.status_code} - {response.text}'}

    if(restaurante is None): 
        return {'Dados': response.json()}

    
    dados_restaurantes = {}
    for item in response.json():
        nome = item['Company']
        if(nome == restaurante):
            if(nome not in dados_restaurantes):
                dados_restaurantes[nome] = []
            
            dados_restaurantes[nome].append({
                "item": item['Item'],
                "Price": item['price'],
                "description": item['description']
            })
    return {'Restaurantes': restaurante, 'Cardapio': dados_restaurantes}